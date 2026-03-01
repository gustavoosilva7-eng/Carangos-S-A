import os; os.system("cls")
import Operacional as o
despesas = {
    "Água": 0,
    "Luz": 0,
    "Salários": 0,
    "Impostos": 0
}

def menu_financeiro():
       
    while True:
        print("Bem-vindo ao menu financeiro!")
        print("1. Calcular custos de produção")
        print("2. Calcular custos por produto")
        print("3. Calcular lucro")
        print("4. Voltar ao menu principal")
        opcao_financeiro = input("Escolha uma opção: ")
        os.system("cls")
        match opcao_financeiro:
            case '1':
                calcular_custos()
            case '2':
                calcular_custos_por_produto()
            case '3':
                calcular_preco_venda()
            case '4':
                os.system("cls")
                break
    
def ler_despesas():
    despesas["Água"] = float(input("Água: R$"))
    despesas["Luz"] = float(input("Luz: R$"))
    despesas["Salários"] = float(input("Salários: R$"))
    despesas["Impostos"] = float(input("Impostos: R$"))
    return sum(despesas.values())
    
def calcular_custos():
    input("Digite os custos mensais de produção:")
    despesas = ler_despesas()
    custos_fixos = sum(despesas.values())
    print(f"Custo fixo mensal: R${custos_fixos:.2f}")
    print(f"Custo fixo anual: R${custos_fixos*12:.2f}")
    input("Pressione Enter para continuar...")
def calcular_custos_por_produto():
    input("Digite os custos mensais de produção:")
    custos_fixos = ler_despesas()
    print(f"Custo fixo mensal: R${custos_fixos:.2f}")
    media, total = o.producao()
    producao_mensal = total * 30
    custo_medio_por_carro = custos_fixos / producao_mensal
    print(f"Custo médio por produto: R${custo_medio_por_carro:.2f}")
    input("Pressione Enter para continuar...")
def calcular_preco_venda():
    input("Digite os custos mensais de produção:")
    custos_fixos = ler_despesas()
    print(f"Custo fixo mensal: R${custos_fixos:.2f}")
    media, total = o.producao()
    producao_mensal = total * 30
    custo_medio_por_carro = custos_fixos / producao_mensal
    preco_venda = custo_medio_por_carro * 1.5  
    print(f"Preço de venda com 50% de lucro: R${preco_venda:.2f}")
    input("Pressione Enter para continuar...")