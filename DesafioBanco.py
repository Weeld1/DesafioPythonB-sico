menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    
    """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("\nInforme o valor desejado:"))
        
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito de: R$ {deposito:.2f}\n"
        else:
            print("\nFalha na operação. Valor informado é inválido")

    elif opcao == "s":
        saque = float(input("Informe o valor desejado:"))

        limite_saques = numero_saques >= LIMITE_SAQUES
        
        if saldo < saque:
            print("\nFalha na operação. Saldo insuficiente.")
            print(f"\nO saldo restante é de R$ {saldo:.2f}")
        
        elif saque > 500:
            print ("\nFalha na operação. Excedeu o limite de saque")

        elif limite_saques:
            print("\nFalha na operação. Limite de saques excedido.")

        elif saque > 0 and saque <=500:
            saldo -= saque
            extrato += f"Saque de: R$ {saque:.2f}\n"
            numero_saques += 1

        else:
            print("\nFalha na operação. Valor informado é inválido")

    elif opcao =="e":
        print("\n-------------- EXTRATO --------------")
        print("Não foi realizado movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("-------------------------------------")
    
    elif opcao == "q":
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")