# 🚗 MCP – Sistema de Análise de Dados Automotivos

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![MariaDB](https://img.shields.io/badge/MariaDB-11.4-orange.svg)
![Google%20Gemini](https://img.shields.io/badge/Google%20Gemini-AI-yellow.svg)
![Docker](https://img.shields.io/badge/Docker-Container-green.svg)

**Sistema inteligente de análise de dados utilizando Google Gemini e MariaDB**

*Projeto desenvolvido para fins de estudo e portfólio.*

</div>

## 📋 Sobre o Projeto

Este é um projeto **MCP (Model Context Protocol)** que demonstra a integração entre um modelo de IA generativa (**Google Gemini**) e um banco de dados **MariaDB**, permitindo realizar análises de dados usando linguagem natural.

### 🎯 Objetivos Educacionais

- Demonstrar na prática a comunicação entre LLMs e bancos de dados  
- Implementar um sistema completo de análise utilizando NLP  
- Criar um ambiente funcional com **Docker + Python + SQL**  
- Servir como material de estudo em IA aplicada e engenharia de dados  

## 🏗️ Arquitetura do Sistema

```
projeto-mcp-automotivo/
├── 📁 database/
│   └── dados_fake_completo.sql
├── 📁 src/
│   ├── database.py
│   ├── mcp_gemini.py
│   ├── requirements.txt
│   └── .env
├── docker-compose.yml
└── README.md
```

## 🚀 Tecnologias Utilizadas

- **Python 3.10+**
- **MariaDB 11.4**
- **Google Gemini 2.0 Flash**
- **Docker**
- **pandas**

## ⚙️ Funcionalidades

### 🔍 Análise com Linguagem Natural  
- Perguntas diretas em português  
- Geração automática de queries SQL  
- Execução e interpretação inteligente dos resultados  

## 🛠️ Instalação Rápida

```bash
git clone https://github.com/raphamaster/projeto-mcp-automotivo.git
cd projeto-mcp-automotivo

# Subir banco de dados via Docker
docker-compose up -d

# Instalar dependências do Python
pip install -r src/requirements.txt

# Executar o sistema
python src/mcp_gemini.py
```

## 💡 Como Usar

Exemplos de perguntas simples:

```
"Qual o faturamento total?"
"Quais são os 5 produtos mais vendidos?"
"Quem são os melhores vendedores?"
```

Perguntas mais elaboradas para testar a LLMs:

```
"Qual categoria de produtos tem a melhor margem de lucro (diferença entre preço de venda e custo) e quantas unidades foram vendidas de cada categoria no último mês?"

"Quais clientes do tipo 'Oficina' têm o maior ticket médio e qual a frequência de compras deles? Mostre também o valor total gasto por cada um."

"Como evoluiu o faturamento mensal nos últimos 6 meses? Mostre a variação percentual mês a mês e identifique se há alguma tendência de crescimento ou queda."

"Compare a performance dos vendedores considerando não apenas o faturamento, mas também o número de vendas realizadas e o tempo que cada um está na empresa. Quem tem a melhor eficiência?"

"Quais produtos têm alta demanda (muitas vendas) mas estoque baixo, representando risco de ruptura? E quais têm estoque alto mas pouca saída, representando capital parado?"

"Qual é o produto 'carro-chefe' de cada categoria em termos de faturamento?"

"Existe correlação entre o valor da venda e a forma de pagamento escolhida?"

"Quais vendedores são mais eficientes em vender produtos de alta margem?"
```

### 📘 Projeto desenvolvido para aprendizado prático  
Sinta-se à vontade para explorar, modificar e ampliar o sistema.
