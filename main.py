import Operacional as t
import os; os.system("cls")
import Estoque as e
while True:
    print("Bem-vindo ao sistema de controle de produção da fábrica!")
    print("1. Registrar produção")
    print("2. Gerenciar estoque")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")
    os.system("cls")
    match opcao:
        case '1':
            t.escala_turno()
        case '2':
            e.menu_estoque()
        case '3':
            print("Saindo do sistema...")
            break
        case _:
            print("Opção inválida. Por favor, escolha uma opção válida.")