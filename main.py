menu = {
    "d": "Depósito",
    "s": "saque",
    "e": "Extrato",
    "q": "Sair"
}

extrato = ""
LIMITE = 500
LIMITE_SAQUES = 3
numero_saques = 0
numero_depositos = 0
saldo = 0

while True:
    opcao = input(f"{menu}\n")

    if opcao == "d":
        valor = float(input("Informe o valor do depósito:\n"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido!")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque:\n"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > LIMITE
        excedeu_saques = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Seu saldo é insuficiente!")

        elif excedeu_limite:
            print("Operação falhou! Você ultrapassou o limite de saques!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido!")

    elif opcao == "e":
        print("\n====================EXTRATO====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("\n===============================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida! Por favor, selecione novamente a operação desejada.")
