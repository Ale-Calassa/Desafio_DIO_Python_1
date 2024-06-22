menu = """
=======================================
Escolha a operação que deseja realizar
    [a] depositar
    [b] sacar
    [c] extrato
    [d] sair
=======================================
Digite sua opção: 
"""
saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "a":
        valor_deposito = float(input("Informe o valor que será depositado!"))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Valor depositado: R$ {valor_deposito:.2f}\n"
            print("Depósito realizado com sucesso!")

        else:
            print("O valor não é válido, sua operação será cancelada!")

    elif opcao == "b":
        valor_saque = float(input("Informe o valor que será sacado!"))

        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saque = numero_saque >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo suficiente!")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite!")

        elif excedeu_saque:
            print("Operação falhou! Número máximo de saques excedido!")

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saque += 1

        else:
            print("Operação falhou! O valor informado é invalido!")

    elif opcao == "c":
        print("\n=====EXTRATO=====")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("====================")

    elif opcao == "d":
        break

    else:
        print("Operação inválida! Favor selecionar novamente a opção desejada")