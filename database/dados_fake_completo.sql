-- =============================================
-- PROJETO MCP - SISTEMA DE VENDAS AUTOMOTIVAS
-- DADOS FAKE COMPLETOS
-- =============================================

-- 1. FORNECEDORES
INSERT INTO fornecedores (nome_fornecedor, contato, telefone, email, endereco) VALUES
('AutoParts Brasil', 'Carlos Silva', '(11) 9999-8888', 'vendas@autoparts.com.br', 'Rua Industrial, 123 - São Paulo/SP'),
('Peças Premium', 'Ana Oliveira', '(21) 7777-6666', 'contato@pecaspremium.com.br', 'Av. das Nações, 456 - Rio de Janeiro/RJ'),
('MotorMax', 'Roberto Santos', '(31) 5555-4444', 'vendas@motormax.com.br', 'Rua Tecnológica, 789 - Belo Horizonte/MG'),
('Suspensão Total', 'Fernanda Lima', '(41) 3333-2222', 'fernanda@suspensaototal.com.br', 'Av. Automotiva, 321 - Curitiba/PR'),
('Freios & Mais', 'Paulo Costa', '(51) 1111-0000', 'paulo@freiosemais.com.br', 'Rua Segurança, 654 - Porto Alegre/RS');

-- 2. CATEGORIAS
INSERT INTO categorias (nome_categoria, descricao) VALUES
('Motor', 'Peças relacionadas ao sistema do motor'),
('Suspensão', 'Componentes do sistema de suspensão'),
('Freios', 'Sistema de frenagem e componentes'),
('Elétrica', 'Sistema elétrico e eletrônico'),
('Transmissão', 'Componentes do sistema de transmissão'),
('Arrefecimento', 'Sistema de arrefecimento do motor'),
('Exaustão', 'Sistema de escapamento e exaustão');

-- 3. PRODUTOS
INSERT INTO produtos (nome_produto, descricao, id_categoria, id_fornecedor, preco_custo, preco_venda, estoque, codigo_barras) VALUES
('Filtro de Óleo', 'Filtro de óleo sintético premium', 1, 1, 12.50, 25.90, 100, '789123456001'),
('Pastilha de Freio Dianteira', 'Pastilha cerâmica para freio dianteiro', 3, 5, 45.00, 89.90, 50, '789123456002'),
('Amortecedor Dianteiro', 'Amortecedor hidráulico original', 2, 4, 120.00, 249.90, 30, '789123456003'),
('Bateria 60Ah', 'Bateria selada 60 amperes', 4, 2, 180.00, 359.90, 25, '789123456004'),
('Correia Dentada', 'Kit correia dentada completo', 5, 3, 85.00, 169.90, 40, '789123456005'),
('Radiador Alumínio', 'Radiador em alumínio original', 6, 1, 220.00, 439.90, 15, '789123456006'),
('Velas de Ignição', 'Jogo com 4 velas iridium', 1, 2, 60.00, 119.90, 80, '789123456007'),
('Disco de Freio', 'Disco de freio ventilado', 3, 5, 75.00, 149.90, 35, '789123456008'),
('Mola Espiral', 'Kit molas esportivas', 2, 4, 150.00, 299.90, 20, '789123456009'),
('Alternador', 'Alternador 90A original', 4, 3, 300.00, 599.90, 10, '789123456010'),
('Embreagem Completa', 'Kit embreagem completo', 5, 1, 200.00, 399.90, 18, '789123456011'),
('Vela de Ignição', 'Vela de ignição simples', 1, 2, 8.00, 19.90, 150, '789123456012'),
('Sensor ABS', 'Sensor do sistema ABS', 3, 5, 40.00, 79.90, 45, '789123456013'),
('Bucha Suspensão', 'Bucha de suspensão dianteira', 2, 4, 15.00, 34.90, 90, '789123456014'),
('Fusível 15A', 'Caixa com 10 fusíveis 15A', 4, 3, 5.00, 12.90, 200, '789123456015');

-- 4. VENDEDORES
INSERT INTO vendedores (nome_vendedor, email, telefone, data_admissao, comissao) VALUES
('João Silva', 'joao.silva@empresa.com', '(11) 98888-1111', '2022-01-15', 0.06),
('Maria Santos', 'maria.santos@empresa.com', '(11) 97777-2222', '2022-03-20', 0.07),
('Pedro Oliveira', 'pedro.oliveira@empresa.com', '(11) 96666-3333', '2021-11-10', 0.05),
('Ana Costa', 'ana.costa@empresa.com', '(11) 95555-4444', '2023-02-01', 0.06),
('Carlos Lima', 'carlos.lima@empresa.com', '(11) 94444-5555', '2022-07-15', 0.05);

-- 5. CLIENTES
INSERT INTO clientes (nome_cliente, tipo_cliente, cpf_cnpj, email, telefone, endereco, cidade, estado) VALUES
('Roberto Alves', 'Pessoa Física', '123.456.789-00', 'roberto.alves@email.com', '(11) 91111-1111', 'Rua A, 100 - Centro', 'São Paulo', 'SP'),
('Oficina Master', 'Oficina', '12.345.678/0001-90', 'contato@oficinamaster.com.br', '(11) 92222-2222', 'Av. B, 200 - Industrial', 'São Paulo', 'SP'),
('AutoCenter Total', 'Revenda', '23.456.789/0001-91', 'vendas@autocentertotal.com.br', '(11) 93333-3333', 'Rua C, 300 - Comercial', 'São Paulo', 'SP'),
('Fernanda Martins', 'Pessoa Física', '234.567.890-11', 'fernanda.martins@email.com', '(11) 94444-4444', 'Alameda D, 400 - Jardins', 'São Paulo', 'SP'),
('Mecânica Rápida', 'Oficina', '34.567.890/0001-92', 'orcamento@mecanicarapida.com.br', '(11) 95555-5555', 'Rua E, 500 - Centro', 'São Paulo', 'SP'),
('Peças & Cia', 'Revenda', '45.678.901/0001-93', 'contato@pecasecia.com.br', '(11) 96666-6666', 'Av. F, 600 - Industrial', 'São Paulo', 'SP'),
('Lucas Rodrigues', 'Pessoa Física', '345.678.901-22', 'lucas.rodrigues@email.com', '(11) 97777-7777', 'Rua G, 700 - Residencial', 'São Paulo', 'SP'),
('AutoServiço Premium', 'Oficina', '56.789.012/0001-94', 'servicos@autopremium.com.br', '(11) 98888-8888', 'Alameda H, 800 - Comercial', 'São Paulo', 'SP');

-- 6. VENDAS
INSERT INTO vendas (id_cliente, id_vendedor, data_venda, valor_total, forma_pagamento, status_venda) VALUES
(1, 1, '2024-01-15 09:30:00', 145.80, 'Cartão Crédito', 'Concluída'),
(2, 2, '2024-01-16 14:15:00', 529.70, 'PIX', 'Concluída'),
(3, 3, '2024-01-17 11:00:00', 319.60, 'Boleto', 'Concluída'),
(4, 1, '2024-01-18 16:45:00', 89.90, 'Dinheiro', 'Concluída'),
(5, 4, '2024-01-19 10:20:00', 689.60, 'Cartão Débito', 'Concluída'),
(6, 2, '2024-01-20 13:30:00', 239.50, 'PIX', 'Concluída'),
(7, 5, '2024-01-21 15:00:00', 179.80, 'Cartão Crédito', 'Concluída'),
(1, 3, '2024-01-22 08:45:00', 399.90, 'Boleto', 'Concluída'),
(2, 1, '2024-01-23 12:00:00', 149.90, 'Cartão Débito', 'Concluída'),
(3, 4, '2024-01-24 17:30:00', 599.90, 'PIX', 'Concluída');

-- 7. ITENS_VENDA
INSERT INTO itens_venda (id_venda, id_produto, quantidade, preco_unitario, subtotal) VALUES
(1, 1, 2, 25.90, 51.80),
(1, 12, 3, 19.90, 59.70),
(1, 15, 2, 12.90, 25.80),
(2, 3, 1, 249.90, 249.90),
(2, 9, 1, 299.90, 299.90),
(3, 2, 2, 89.90, 179.80),
(3, 8, 1, 149.90, 149.90),
(4, 2, 1, 89.90, 89.90),
(5, 4, 1, 359.90, 359.90),
(5, 6, 1, 439.90, 439.90),
(6, 5, 1, 169.90, 169.90),
(6, 7, 1, 119.90, 119.90),
(7, 10, 1, 599.90, 599.90),
(8, 11, 1, 399.90, 399.90),
(9, 8, 1, 149.90, 149.90),
(10, 10, 1, 599.90, 599.90);

-- =============================================
-- VERIFICAÇÃO DOS DADOS INSERIDOS
-- =============================================

-- Contagem de registros por tabela
SELECT 'Fornecedores' as Tabela, COUNT(*) as Total FROM fornecedores
UNION ALL SELECT 'Categorias', COUNT(*) FROM categorias
UNION ALL SELECT 'Produtos', COUNT(*) FROM produtos
UNION ALL SELECT 'Vendedores', COUNT(*) FROM vendedores
UNION ALL SELECT 'Clientes', COUNT(*) FROM clientes
UNION ALL SELECT 'Vendas', COUNT(*) FROM vendas
UNION ALL SELECT 'Itens Venda', COUNT(*) FROM itens_venda;

-- Visualização de amostra dos dados
SELECT '=== AMOSTRA DE PRODUTOS ===' as Info;
SELECT p.nome_produto, c.nome_categoria, f.nome_fornecedor, p.preco_venda 
FROM produtos p 
LEFT JOIN categorias c ON p.id_categoria = c.id_categoria 
LEFT JOIN fornecedores f ON p.id_fornecedor = f.id_fornecedor 
LIMIT 5;

SELECT '=== AMOSTRA DE VENDAS ===' as Info;
SELECT v.id_venda, c.nome_cliente, vd.nome_vendedor, v.data_venda, v.valor_total 
FROM vendas v 
LEFT JOIN clientes c ON v.id_cliente = c.id_cliente 
LEFT JOIN vendedores vd ON v.id_vendedor = vd.id_vendedor 
LIMIT 5;