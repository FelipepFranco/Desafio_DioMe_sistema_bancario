saldo = 500.0
opcoes = 4
saquesDiarios = 0

while opcoes != 0:
    opcoes = int(input('''
    ###### Escolha uma  opção ######
            1 - Efetuar Saque 
            2 - Efetuar Depósito
            3 - Consultar extrato
            0 - Sair
    '''))

    if opcoes == 1:
        valor = float(input("Digite o valor para sacar:  "))
        if saquesDiarios < 3:
            if valor > saldo:
                print("Saldo insuficiente")
            elif valor <= 0:
                print("Valor incorreto")
            elif valor <= saldo:
                saldo -= valor
                print(f"Novo saldo: R${saldo}")
                saquesDiarios += 1
                print(f"Saques diarios: R${saquesDiarios}")
        else:
            print("Você atingiu o limite de 3 saques diários")

    elif opcoes == 2:
        valor = float(input("Digite o valor para depositar:  "))
        if valor <= 0:
            print("Valor incorreto")
        else:
            saldo += valor
            print(f"Novo saldo: R${saldo}")
    elif opcoes == 3:
        print(f"Seu saldo: R${saldo}")

print("Obrigado pela preferência")
