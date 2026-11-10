from database import conectar
import os


produtos = {}

def menu_estoque():
    while True:
        print("1. Cadastrar produto")
        print("2. Pesquisar produto")
        print("3. Calcular custos do estoque")
        print("4. Voltar ao menu principal")
        opcao_estoque = input("Escolha uma opção: ")
        os.system("cls")
        
        match opcao_estoque:
            case '1':
                cadastrar_produto()
            case '2':
                pesquisar_produto()
            case '3':
                custos_estoque()
            case '4':
                break
            case _:
                print("Opção inválida. Por favor, escolha uma opção válida.")

def cadastrar_produto():

    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    data_fabricacao = input("Digite a data de fabricação do produto (dd/mm/aaaa): ")
    fornecedor = input("Digite o nome do fornecedor do produto: ")
    try:
        quantidade = int(input("Digite a quantidade do produto: "))
        valor_compra = float(input("Digite o valor de compra do produto: "))
    except ValueError:
        print("❌ Quantidade ou valor de compra inválidos.")
        return

    # Chama a função ajustada para gravar no MySQL
    salvar_produto(codigo, nome, data_fabricacao, fornecedor, quantidade, valor_compra)


def pesquisar_produto():
    codigo = input("Digite o código do produto: ")
    for produto in produtos.values():
        if produto['Codigo'].lower() == codigo.lower() or produto['Nome'].lower() == codigo.lower():
            print(f"Produto encontrado: {produto}")
            return produto
    print("Produto não encontrado.")
    return None

def custos_estoque():
    total_custo = 0
    produto = pesquisar_produto()
    if produto:
        total_custo = produto["Quantidade"] * produto["Valor de Compra"]
        print(f"Custo Semanal do estoque: R${total_custo*7:.2f}")
        print(f"Custo Mensal do estoque: R${total_custo*30:.2f}")
        
        print(f"Custo Anual do estoque: R${total_custo*365:.2f}")
    else:
        print("Não foi possível calcular o custo do estoque.")

from datetime import datetime

def salvar_produto(codigo, nome, data_fabricacao, fornecedor, quantidade, valor_compra):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        
        # Converte a data de 'dd/mm/aaaa' para o formato do MySQL 'aaaa-mm-dd'
        data_obj = datetime.strptime(data_fabricacao, "%d/%m/%Y").date()
        
        sql = """
            INSERT INTO produtos (codigo, nome, data_fabricacao, fornecedor, quantidade, valor_compra) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (codigo, nome, data_obj, fornecedor, quantidade, valor_compra)
        
        cursor.execute(sql, valores)
        conexao.commit()
        print("✅ Produto salvo no MySQL com sucesso!")
        
    except Exception as err:
        print(f"❌ Erro ao salvar produto no MySQL: {err}")
        
    finally:
        # Garante que as conexões serão fechadas mesmo em caso de erro
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()