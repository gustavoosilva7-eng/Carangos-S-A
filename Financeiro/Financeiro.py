import os
from database import conectar
import Operacional.Operacional as o

# Função para salvar a despesa lançada no banco de dados
def salvar_despesa_banco(agua, luz, salarios, impostos):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        
        sql = """
            INSERT INTO despesas (agua, luz, salarios, impostos, data_registro) 
            VALUES (%s, %s, %s, %s, CURDATE())
        """
        cursor.execute(sql, (agua, luz, salarios, impostos))
        conexao.commit()
        print("✅ Despesas registradas no banco MySQL!")
    except Exception as err:
        print(f"❌ Erro ao salvar despesas no banco: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()

def menu_financeiro():
    while True:
        print("=== MENU FINANCEIRO ===")
        print("1. Calcular custos de produção")
        print("2. Calcular custos por produto")
        print("3. Calcular preço de venda e lucro")
        print("4. Voltar ao menu principal")
        
        opcao_financeiro = input("\nEscolha uma opção: ")
        os.system("cls" if os.name == "nt" else "clear")
        
        match opcao_financeiro:
            case '1':
                calcular_custos()
            case '2':
                calcular_custos_por_produto()
            case '3':
                calcular_preco_venda()
            case '4':
                break
            case _:
                print("Opção inválida. Por favor, escolha uma opção válida.\n")

def ler_despesas():
    print("--- DIGITE OS CUSTOS MENSAIS DE PRODUÇÃO ---")
    try:
        agua = float(input("Água: R$ "))
        luz = float(input("Luz: R$ "))
        salarios = float(input("Salários: R$ "))
        impostos = float(input("Impostos: R$ "))
        
        # Salva o lançamento no MySQL
        salvar_despesa_banco(agua, luz, salarios, impostos)
        
        total_despesas = agua + luz + salarios + impostos
        return total_despesas
    except ValueError:
        print("❌ Valor inválido digitado. Assumindo R$ 0.00.")
        return 0.0

def calcular_custos():
    custos_fixos = ler_despesas()
    print(f"\nCusto fixo mensal: R${custos_fixos:.2f}")
    print(f"Custo fixo anual: R${custos_fixos * 12:.2f}")
    input("\nPressione Enter para continuar...")

def calcular_custos_por_produto():
    custos_fixos = ler_despesas()
    print(f"\nCusto fixo mensal: R${custos_fixos:.2f}")
    
    # Chama o módulo operacional para pegar a produção
    media, total = o.producao()
    producao_mensal = total * 30
    
    if producao_mensal > 0:
        custo_medio_por_carro = custos_fixos / producao_mensal
        print(f"Custo médio por produto: R${custo_medio_por_carro:.2f}")
    else:
        print("⚠️ Produção mensal é igual a 0. Não foi possível calcular o custo por produto.")
        
    input("\nPressione Enter para continuar...")

def calcular_preco_venda():
    custos_fixos = ler_despesas()
    print(f"\nCusto fixo mensal: R${custos_fixos:.2f}")
    
    media, total = o.producao()
    producao_mensal = total * 30
    
    if producao_mensal > 0:
        custo_medio_por_carro = custos_fixos / producao_mensal
        preco_venda = custo_medio_por_carro * 1.5  # 50% de margem
        print(f"Custo por unidade: R${custo_medio_por_carro:.2f}")
        print(f"Preço de venda sugerido (50% lucro): R${preco_venda:.2f}")
    else:
        print("⚠️ Produção mensal é igual a 0. Não foi possível calcular o preço de venda.")
        
    input("\nPressione Enter para continuar...")