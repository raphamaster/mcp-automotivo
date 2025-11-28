"""
MCP REAL com Google Gemini - Análise inteligente do banco de dados
Sistema que integra LLM (Google Gemini) com banco de dados para análise de dados
em linguagem natural.
"""

import warnings
# Suprime os warnings do Google API
warnings.filterwarnings("ignore", category=FutureWarning, module="google.api_core")

import google.generativeai as genai
from database import DatabaseConnection
import pandas as pd
from tabulate import tabulate
import json
import os
from dotenv import load_dotenv
from datetime import datetime, date
from decimal import Decimal

class MCPGemini:
    """
    Classe principal do Motor de Consulta Personalizada (MCP)
    Integra Google Gemini com banco de dados MariaDB para análise de dados
    """
    
    def __init__(self):
        # Carrega variáveis de ambiente do arquivo .env
        load_dotenv()
        
        # Configuração da API do Google Gemini
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("❌ GEMINI_API_KEY não encontrada no arquivo .env")
        
        # Inicializa a configuração da API Gemini
        genai.configure(api_key=api_key)
        
        # Lista de modelos Gemini para tentativa de conexão (em ordem de preferência)
        model_names = [
            'models/gemini-2.0-flash',  # Modelo rápido e eficiente
            'models/gemini-2.0-flash-001',
            'models/gemini-2.0-flash-lite',
            'models/gemini-pro-latest',
            'models/gemini-flash-latest'
        ]
        
        # Tenta conectar com cada modelo até encontrar um que funcione
        for model_name in model_names:
            try:
                self.model = genai.GenerativeModel(model_name)
                print(f"✅ Modelo carregado com sucesso: {model_name}")
                break
            except Exception as e:
                print(f"❌ Modelo {model_name} falhou: {e}")
                continue
        else:
            # Fallback: se nenhum modelo funcionar, tenta o modelo básico
            try:
                self.model = genai.GenerativeModel('models/gemini-2.0-flash')
                print("✅ Usando fallback: gemini-2.0-flash")
            except Exception as e:
                raise ValueError(f"❌ Nenhum modelo Gemini funcionou: {e}")
        
        # Conexão com o banco de dados MariaDB
        self.db = DatabaseConnection()
        self.connected = self.db.connect()  # Estabelece conexão
        self.schema_info = None  # Cache para o schema do banco
        
    def serialize_value(self, value):
        """
        Converte valores complexos para tipos serializáveis em JSON
        Necessário porque alguns tipos do MySQL não são nativamente serializáveis
        """
        if value is None:
            return None
        elif isinstance(value, (datetime, date)):
            return value.isoformat()  # Converte datas para string ISO
        elif isinstance(value, Decimal):
            return float(value)  # Converte Decimal para float
        elif isinstance(value, (bytes, bytearray)):
            return value.hex()  # Converte bytes para hexadecimal
        elif hasattr(value, '__dict__'):
            return str(value)  # Converte objetos para string
        else:
            return value  # Mantém tipos básicos (string, int, etc.)
    
    def serialize_schema(self, schema):
        """
        Converte todo o schema do banco para formato serializável em JSON
        Isso permite enviar a estrutura do banco para o Gemini
        """
        serialized_schema = {}
        
        # Itera por cada tabela no schema
        for table_name, table_info in schema.items():
            serialized_schema[table_name] = {}
            
            # Serializa informações das colunas
            if 'columns' in table_info and table_info['columns']:
                serialized_columns = []
                for column in table_info['columns']:
                    # Converte cada valor da coluna para tipo serializável
                    serialized_column = {k: self.serialize_value(v) for k, v in column.items()}
                    serialized_columns.append(serialized_column)
                serialized_schema[table_name]['columns'] = serialized_columns
            
            # Serializa chaves estrangeiras (relacionamentos entre tabelas)
            if 'foreign_keys' in table_info and table_info['foreign_keys']:
                serialized_fks = []
                for fk in table_info['foreign_keys']:
                    serialized_fk = {k: self.serialize_value(v) for k, v in fk.items()}
                    serialized_fks.append(serialized_fk)
                serialized_schema[table_name]['foreign_keys'] = serialized_fks
            
            # Serializa dados de exemplo (amostra de registros)
            if 'sample_data' in table_info and table_info['sample_data']:
                serialized_samples = []
                for sample in table_info['sample_data']:
                    serialized_sample = {k: self.serialize_value(v) for k, v in sample.items()}
                    serialized_samples.append(serialized_sample)
                serialized_schema[table_name]['sample_data'] = serialized_samples
        
        return serialized_schema
    
    def get_database_schema(self):
        """
        Obtém dinamicamente o schema completo do banco de dados
        Inclui: tabelas, colunas, chaves estrangeiras e dados de exemplo
        """
        # Usa cache para evitar consultas repetidas ao banco
        if self.schema_info:
            return self.schema_info
            
        schema = {}
        
        try:
            # Obtém lista de todas as tabelas do banco
            tables_query = "SHOW TABLES"
            tables_result = self.db.execute_query(tables_query)
            
            print(f"📋 Encontradas {len(tables_result)} tabelas no banco")
            
            # Para cada tabela, obtém sua estrutura completa
            for table_row in tables_result:
                table_name = list(table_row.values())[0]
                print(f"  📊 Obtendo schema da tabela: {table_name}")
                
                # Obtém estrutura das colunas da tabela
                describe_query = f"DESCRIBE {table_name}"
                columns_result = self.db.execute_query(describe_query)
                
                # Chaves estrangeiras (simplificado - poderia ser expandido)
                foreign_keys = []
                
                # Obtém amostra de dados reais da tabela (2 registros)
                sample_query = f"SELECT * FROM {table_name} LIMIT 2"
                sample_result = self.db.execute_query(sample_query)
                
                # Armazena todas as informações da tabela
                schema[table_name] = {
                    'columns': columns_result or [],
                    'foreign_keys': foreign_keys or [],
                    'sample_data': sample_result or []
                }
            
            # Serializa o schema para formato JSON
            self.schema_info = self.serialize_schema(schema)
            print("✅ Schema serializado com sucesso")
            return self.schema_info
            
        except Exception as e:
            print(f"❌ Erro ao obter schema: {e}")
            return {}
    
    def generate_sql_with_gemini(self, question, schema):
        """
        Usa o Google Gemini para gerar SQL baseado na pergunta em linguagem natural
        e no schema do banco
        """
        
        try:
            # Converte o schema para string JSON
            schema_str = json.dumps(schema, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"❌ Erro ao serializar schema: {e}")
            return None
        
        # Prompt engenheirado para o Gemini - instruções específicas para gerar SQL
        prompt = f"""
        Você é um especialista em SQL e análise de dados. 
        Baseado no schema do banco abaixo, gere uma query SQL para responder à pergunta.

        SCHEMA DO BANCO:
        {schema_str}

        PERGUNTA: {question}

        REGRAS:
        1. Use apenas MySQL/MariaDB syntax
        2. Retorne apenas o SQL, sem explicações
        3. Use LIMIT quando apropriado para evitar queries muito pesadas
        4. Considere relacionamentos entre tabelas
        5. Use nomes de colunas e tabelas exatos do schema
        6. Para produtos mais vendidos, some as quantidades da tabela itens_venda

        Retorne APENAS o código SQL, nada mais.
        SQL:
        """
        
        try:
            print("🤖 Consultando Gemini para gerar SQL...")
            # Envia o prompt para o Gemini e obtém a resposta
            response = self.model.generate_content(prompt)
            sql = response.text.strip()
            
            # Limpa o SQL (remove blocos de código markdown se existirem)
            if sql.startswith('```sql'):
                sql = sql.replace('```sql', '').replace('```', '').strip()
            elif sql.startswith('```'):
                sql = sql.replace('```', '').strip()
            
            print(f"🔍 SQL gerado pelo Gemini:\n{sql}")
            return sql
            
        except Exception as e:
            print(f"❌ Erro ao gerar SQL com Gemini: {e}")
            return None
    
    def execute_and_analyze(self, question, sql):
        """
        Executa o SQL gerado no banco de dados e usa o Gemini para analisar os resultados
        """
        try:
            print("🗄️ Executando query no banco...")
            # Executa a query SQL no banco de dados
            results = self.db.execute_query(sql)
            
            if results is None:
                return "❌ Erro ao executar a query no banco de dados"
            
            print(f"📊 Query retornou {len(results)} registros")
            
            # Converte resultados para DataFrame do pandas para facilitar manipulação
            df = pd.DataFrame(results)
            
            if len(results) == 0:
                return "📭 Nenhum resultado encontrado para esta consulta."
            
            # Prepara os dados em formato tabular para análise do Gemini
            results_str = tabulate(df, headers='keys', tablefmt='plain', showindex=False)
            
            # Prompt para análise dos resultados pelo Gemini
            analysis_prompt = f"""
            PERGUNTA ORIGINAL: {question}
            
            RESULTADOS DA CONSULTA:
            {results_str}
            
            Analise estes resultados e forneça:
            1. Uma explicação clara do que os dados mostram
            2. Insights relevantes para a pergunta original  
            3. Observações importantes ou padrões detectados
            4. Recomendações se aplicável

            Responda em português de forma natural e útil.
            Seja conciso e direto ao ponto.
            """
            
            print("🤖 Consultando Gemini para análise dos resultados...")
            analysis_response = self.model.generate_content(analysis_prompt)
            analysis = analysis_response.text
            
            # Formata a resposta final para o usuário
            final_response = f"""
🔍 **PERGUNTA**: {question}

📊 **RESULTADOS**:
{tabulate(df, headers='keys', tablefmt='pretty', showindex=False)}

💡 **ANÁLISE DO GEMINI**:
{analysis}

📋 **Total de registros**: {len(results)}
            """
            
            return final_response
            
        except Exception as e:
            return f"❌ Erro durante execução/análise: {e}"
    
    def process_question(self, question):
        """
        Processa uma pergunta completa: do português para SQL, execução e análise
        Fluxo principal: Schema → Geração SQL → Execução → Análise → Resposta
        """
        if not self.connected:
            return "❌ Erro de conexão com o banco de dados"
        
        print(f"🔄 Processando: '{question}'")
        
        try:
            # 1. Obtém o schema do banco (estrutura das tabelas)
            schema = self.get_database_schema()
            if not schema:
                return "❌ Não foi possível obter o schema do banco"
            
            # 2. Usa Gemini para converter pergunta em português para SQL
            sql = self.generate_sql_with_gemini(question, schema)
            if not sql:
                return "❌ Não foi possível gerar SQL para esta pergunta"
            
            # 3. Executa o SQL e analisa os resultados com Gemini
            return self.execute_and_analyze(question, sql)
            
        except Exception as e:
            return f"❌ Erro no processamento: {e}"
    
    def close(self):
        """Fecha todas as conexões abertas (banco de dados)"""
        if self.connected:
            self.db.disconnect()

# Interface principal do sistema
def main():
    """
    Função principal que gerencia a interação com o usuário
    Loop interativo para receber perguntas e mostrar respostas
    """
    try:
        print("🚗 MCP REAL com Google Gemini - Sistema de Análise de Dados")
        print("=" * 60)
        
        # Inicializa o sistema MCP
        mcp = MCPGemini()
        
        # Loop principal de interação
        while True:
            print("\n" + "=" * 50)
            question = input("\n❓ Faça sua pergunta sobre os dados (ou 'sair'): ").strip()
            
            # Comandos para sair do sistema
            if question.lower() in ['sair', 'exit', 'quit']:
                break
            
            # Ignora entradas vazias
            if not question:
                continue
            
            # Processa a pergunta e exibe a resposta
            print("\n🔄 Analisando sua pergunta...")
            response = mcp.process_question(question)
            print(f"\n{response}")
        
        # Encerra o sistema gracefulmente
        mcp.close()
        print("\n👋 Obrigado por usar o MCP com Gemini!")
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        print("💡 Verifique sua chave da API Gemini no arquivo .env")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()