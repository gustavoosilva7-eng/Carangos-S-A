import os; os.system("cls")
 
calendario = {"Segunda-feira": 0, 
              "Terça-feira": 0, 
              "Quarta-feira": 0, 
              "Quinta-feira": 0, 
              "Sexta-feira": 0, 
              "Sábado": 0, 
              "Domingo": 0}

def producao():
    print("Produção do Turno: ")
    for dia in calendario.keys():
    
        producao = int(input(f"Digite a produção do turno  para {dia}: "))
        print("Produção do turno registrada com sucesso.")
        calendario[dia] = producao
    total = 0
    media = 0
    input("Pressione Enter para continuar...")
    os.system("cls")
    print("Produção do Turno ")
    print(calendario)
    input("Pressione Enter para continuar...")
    os.system("cls")
    
    print("Produção total do turno :")
    total = sum(calendario.values())
    print(total)
    input("Pressione Enter para continuar...")
    os.system("cls")
    
    
    print("Produção média do turno :")
    media = total / 7
    print(f"{media:.2f}")
    input("Pressione Enter para continuar...")
    os.system("cls")
    return media, total

        
def escala_turno():
    print("Escala de Turno")
    print("1. Turno Manhã")
    print("2. Turno Tarde")
    print("3. Turno Noite")
    print("4. Calcular capacidade de produção")
    print("5. Voltar ao menu principal")
    turno = input("Escolha o turno: ")
    os.system("cls")
    if turno == '1':
        print("1. Registrar produção para o Turno Manhã")
        print("2. Simular produção para o Turno Manhã")
        opcao = input("Escolha uma opção: ") 
        os.system("cls")
        if opcao == '1':               
                print("Turno Manhã selecionado.")
                producao()
                relatorio_producao()
                input("Pressione Enter para continuar...")
        if opcao == '2':
                print("Simulando produção para o Turno Manhã...")
                print("1. Simular produção mensal: ")
                print("2. Simular produção anual: ")
                opcao_simulacao = input("Escolha uma opção de simulação: ") 
                os.system("cls")
                if opcao_simulacao == '1':
                    print("Simulando produção mensal para o Turno Manhã...")
                    total = producao()
                    producao_mensal = total * 30 
                    print(f"Produção mensal simulada: {sum(producao_mensal):.2f}")
                    relatorio_producao()
                    input("Pressione Enter para continuar...")
                elif opcao_simulacao == '2':
                    print("Simulando produção anual para o Turno Manhã...")
                    total = producao()
                    producao_anual = total * 365
                    print(f"Produção anual simulada: {sum(producao_anual):.2f}")
                    relatorio_producao()
                    input("Pressione Enter para continuar...")
    elif turno == '2':
        os.system("cls")
        print("1. Registrar produção para o Turno Tarde")
        print("2. Simular produção para o Turno Tarde")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            os.system("cls")
            print("Turno Tarde selecionado.")
            producao()
        elif opcao == '2':
            os.system("cls")        
            print("Simulando produção para o Turno Tarde...")
            print("1. Simular produção mensal: ")
            print("2. Simular produção anual: ")
            opcao_simulacao = input("Escolha uma opção de simulação: ") 
            if opcao_simulacao == '1':
                os.system("cls")    
                print("Simulando produção mensal para o Turno Tarde...")
                total = producao()
                producao_mensal = total * 30 
                print(f"Produção mensal simulada: {sum(producao_mensal):.2f}")
                relatorio_producao()
                input("Pressione Enter para continuar...")
            elif opcao_simulacao == '2':
                os.system("cls")
                print("Simulando produção anual para o Turno Tarde...")
                total = producao()
                producao_anual = total * 365
                print(f"Produção anual simulada: {sum(producao_anual):.2f}")
                relatorio_producao()
                input("Pressione Enter para continuar...")                
    elif turno == '3':
        os.system("cls")
        print("Turno Noite selecionado.")
        print("1. Registrar produção para o Turno Noite")
        print("2. Simular produção para o Turno Noite")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            os.system("cls")
            print("Turno Noite selecionado.")
            producao()
        elif opcao == '2':
            os.system("cls")
            print("Simulando produção para o Turno Noite...")
            print("1. Simular produção mensal: ")
            print("2. Simular produção anual: ")
            opcao_simulacao = input("Escolha uma opção de simulação: ") 
            if opcao_simulacao == '1':
                os.system("cls")
                print("Simulando produção mensal para o Turno Noite...")
                total = producao()
                producao_mensal = total * 30 
                print(f"Produção mensal simulada: {sum(producao_mensal):.2f}")
                relatorio_producao()
                input("Pressione Enter para continuar...")
            elif opcao_simulacao == '2':
                os.system("cls")
                print("Simulando produção anual para o Turno Noite...")
                total = producao()
                producao_anual = total * 365
                print(f"Produção anual simulada: {sum(producao_anual):.2f}")
                relatorio_producao()
                input("Pressione Enter para continuar...")  
    elif turno == '4':
        os.system("cls")
        capacidade_producao()
    elif turno == '5':
        os.system("cls")
        print("Voltando ao menu principal...")
        return  
    else:
        print("Opção inválida. Por favor, escolha um turno válido.")
def capacidade_producao():
    capacidade_padrao = 500
    print("Capacidade de Produção")
    print("1. Calcular capacidade de produção com 2 turnos ativos")
    print("2. Calcular capacidade de produção com 3 turnos ativos")
    turno = input("Escolha o turno: ")
    os.system("cls")
    if turno == '1':
        print("******Calculando capacidade de produção com 2 turnos ativos******")
        capacidade = capacidade_padrao
        print(f"Capacidade de produção mensal com 2 turnos ativos: {capacidade:.2f}")
        input("Pressione Enter para continuar...")
        os.system("cls")
    elif turno == '2':
        print("******Calculando capacidade de produção com 3 turnos ativos******")
        capacidade = capacidade_padrao + (capacidade_padrao * 0.50)
        print(f"Capacidade de produção mensal com 3 turnos ativos: {capacidade:.2f}")
        input("Pressione Enter para continuar...")
        os.system("cls")
    else:
        print("Opção inválida. Por favor, escolha um turno válido.")
def relatorio_producao():
    print("******Relatório de Produção******")
    print(calendario)
    print(f"Produção total do turno : {sum(calendario.values()):.2f}")
    print(f"Produção média do turno : {sum(calendario.values())/7:.2f}")
    print(f"Capacidade de produção mensal com 2 turnos ativos: {500:.2f}")
    print(f"Capacidade de produção mensal com 3 turnos ativos: {500 + (500 * 0.50):.2f}")
    print(f"Produção mensal simulada: {sum(calendario.values()) * 30:.2f}   ")
    print(f"Produção anual simulada: {sum(calendario.values()) * 365:.2f}   ")
    print("******Fim do Relatório de Produção******")
    input("Pressione Enter para continuar...")
    os.system("cls")
    return