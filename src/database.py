"""
Módulo de conexão com o banco de dados MariaDB
"""
import mysql.connector
from mysql.connector import Error
import pandas as pd

class DatabaseConnection:
    """Classe para gerenciar a conexão com o banco de dados"""
    
    def __init__(self):
        self.connection = None
        self.config = {
            'host': 'localhost',
            'port': 3306,
            'database': 'automotivo_db',
            'user': 'automotivo_user',
            'password': 'automotivo123'
        }
    
    def connect(self):
        """Estabelece conexão com o banco de dados"""
        try:
            self.connection = mysql.connector.connect(**self.config)
            if self.connection.is_connected():
                print("✅ Conexão com o banco de dados estabelecida com sucesso!")
                return True
        except Error as e:
            print(f"❌ Erro ao conectar com o banco de dados: {e}")
            return False
    
    def disconnect(self):
        """Fecha a conexão com o banco de dados"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("✅ Conexão com o banco de dados fechada.")
    
    def execute_query(self, query, params=None):
        """
        Executa uma query e retorna os resultados
        
        Args:
            query (str): Query SQL a ser executada
            params (tuple): Parâmetros para a query (opcional)
        
        Returns:
            list: Lista de resultados ou None em caso de erro
        """
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params or ())
            result = cursor.fetchall()
            cursor.close()
            return result
        except Error as e:
            print(f"❌ Erro ao executar query: {e}")
            print(f"Query: {query}")
            return None
    
    def execute_query_dataframe(self, query, params=None):
        """
        Executa uma query e retorna um DataFrame do pandas
        
        Args:
            query (str): Query SQL a ser executada
            params (tuple): Parâmetros para a query (opcional)
        
        Returns:
            pandas.DataFrame: DataFrame com os resultados ou None em caso de erro
        """
        try:
            df = pd.read_sql(query, self.connection, params=params)
            return df
        except Error as e:
            print(f"❌ Erro ao executar query: {e}")
            return None
    
    def test_connection(self):
        """Testa a conexão e exibe informações das tabelas"""
        if not self.connect():
            return False
        
        try:
            # Verifica tabelas existentes
            query = "SHOW TABLES"
            tables = self.execute_query(query)
            
            print("\n📊 TABELAS NO BANCO DE DADOS:")
            print("-" * 30)
            for table in tables:
                table_name = list(table.values())[0]
                print(f"• {table_name}")
            
            # Conta registros em cada tabela
            print("\n📈 CONTAGEM DE REGISTROS:")
            print("-" * 30)
            for table in tables:
                table_name = list(table.values())[0]
                count_query = f"SELECT COUNT(*) as total FROM {table_name}"
                count_result = self.execute_query(count_query)
                if count_result:
                    total = count_result[0]['total']
                    print(f"• {table_name}: {total} registros")
            
            return True
            
        except Error as e:
            print(f"❌ Erro ao testar conexão: {e}")
            return False
        finally:
            self.disconnect()

# Função auxiliar para uso rápido
def get_database_connection():
    """Retorna uma instância da conexão com o banco"""
    db = DatabaseConnection()
    if db.connect():
        return db
    return None

# Teste da conexão (executa apenas quando o arquivo é rodado diretamente)
if __name__ == "__main__":
    print("🧪 Testando conexão com o banco de dados...")
    db = DatabaseConnection()
    db.test_connection()