CREATE DATABASE IF NOT EXISTS carangos_sa;
USE carangos_sa;
SELECT DATABASE();

-- 1. Criar o Banco de Dados
CREATE DATABASE IF NOT EXISTS carangos_sa;

-- 2. Selecionar o Banco para uso
USE carangos_sa;

-- 3. Criar a tabela de PRODUTOS (para o módulo Estoque)
CREATE TABLE IF NOT EXISTS produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL UNIQUE,
    nome VARCHAR(100) NOT NULL,
    data_fabricacao DATE,
    fornecedor VARCHAR(100),
    quantidade INT NOT NULL,
    valor_compra DECIMAL(10, 2) NOT NULL,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Criar a tabela de DESPESAS (para o módulo Financeiro)
CREATE TABLE IF NOT EXISTS despesas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    agua DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    luz DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    salarios DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    impostos DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    data_registro DATE NOT NULL
);

SELECT * FROM carangos_sa.produtos;