# 🚗 Carangos S/A - Sistema de Gestão Industrial e Estoque

O **Carangos S/A** é uma aplicação em Python desenvolvida para automatizar e gerir os processos operacionais, de estoque e financeiros de uma fábrica. O sistema conta com uma arquitetura modular e integração com o banco de dados relacional **MySQL** para persistência segura de dados.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Banco de Dados:** MySQL
- **Driver de Conexão:** `mysql-connector-python`
- **IDE / Ferramentas:** VS Code, MySQL Workbench, Git

---

## 📐 Arquitetura do Projeto

O projeto foi estruturado seguindo o princípio da separação de responsabilidades em módulos independentes:

```text
Carangos-S-A/
├── Estoque/
│   └── Estoque.py        # Gestão e cadastro de produtos no MySQL
├── Financeiro/
│   └── Financeiro.py     # Cálculos de custos fixos, margem e precificação
├── Operacional/
│   └── Operacional.py    # Escala de turnos e controle de produção
├── database.py           # Módulo centralizado de conexão com o banco
├── main.py               # Menu principal e fluxo da aplicação
└── README.md

