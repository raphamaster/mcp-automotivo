-- =============================================
-- PROJETO MCP - SISTEMA DE VENDAS AUTOMOTIVAS
-- CRIAÇÃO DAS TABELAS
-- =============================================

-- Tabela de Fornecedores
CREATE TABLE fornecedores (
    id_fornecedor INT AUTO_INCREMENT PRIMARY KEY,
    nome_fornecedor VARCHAR(100) NOT NULL,
    contato VARCHAR(100),
    telefone VARCHAR(20),
    email VARCHAR(100),
    endereco TEXT,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Categorias de Produtos
CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nome_categoria VARCHAR(50) NOT NULL,
    descricao TEXT
);

-- Tabela de Produtos (Peças Automotivas)
CREATE TABLE produtos (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome_produto VARCHAR(100) NOT NULL,
    descricao TEXT,
    id_categoria INT,
    id_fornecedor INT,
    preco_custo DECIMAL(10,2),
    preco_venda DECIMAL(10,2),
    estoque INT DEFAULT 0,
    codigo_barras VARCHAR(50),
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria),
    FOREIGN KEY (id_fornecedor) REFERENCES fornecedores(id_fornecedor)
);

-- Tabela de Vendedores
CREATE TABLE vendedores (
    id_vendedor INT AUTO_INCREMENT PRIMARY KEY,
    nome_vendedor VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    telefone VARCHAR(20),
    data_admissao DATE,
    comissao DECIMAL(5,2) DEFAULT 0.05
);

-- Tabela de Clientes
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome_cliente VARCHAR(100) NOT NULL,
    tipo_cliente ENUM('Pessoa Física', 'Oficina', 'Revenda') DEFAULT 'Pessoa Física',
    cpf_cnpj VARCHAR(20),
    email VARCHAR(100),
    telefone VARCHAR(20),
    endereco TEXT,
    cidade VARCHAR(50),
    estado CHAR(2),
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Vendas
CREATE TABLE vendas (
    id_venda INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_vendedor INT,
    data_venda DATETIME DEFAULT CURRENT_TIMESTAMP,
    valor_total DECIMAL(10,2),
    forma_pagamento ENUM('Dinheiro', 'Cartão Crédito', 'Cartão Débito', 'PIX', 'Boleto'),
    status_venda ENUM('Concluída', 'Cancelada', 'Pendente') DEFAULT 'Concluída',
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_vendedor) REFERENCES vendedores(id_vendedor)
);

-- Tabela de Itens da Venda
CREATE TABLE itens_venda (
    id_item INT AUTO_INCREMENT PRIMARY KEY,
    id_venda INT,
    id_produto INT,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10,2),
    subtotal DECIMAL(10,2),
    FOREIGN KEY (id_venda) REFERENCES vendas(id_venda),
    FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
);

-- =============================================
-- ÍNDICES PARA MELHOR PERFORMANCE
-- =============================================

CREATE INDEX idx_vendas_data ON vendas(data_venda);
CREATE INDEX idx_vendas_cliente ON vendas(id_cliente);
CREATE INDEX idx_vendas_vendedor ON vendas(id_vendedor);
CREATE INDEX idx_produtos_categoria ON produtos(id_categoria);
CREATE INDEX idx_produtos_fornecedor ON produtos(id_fornecedor);
CREATE INDEX idx_itens_venda_produto ON itens_venda(id_produto);
CREATE INDEX idx_itens_venda_venda ON itens_venda(id_venda);

-- =============================================
-- VERIFICAÇÃO DAS TABELAS CRIADAS
-- =============================================

-- Comando para verificar se todas as tabelas foram criadas
SHOW TABLES;

-- Comando para ver a estrutura de uma tabela específica
-- DESCRIBE nome_da_tabela;