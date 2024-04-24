from datetime import datetime

menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        print("\n\nDepósito")
        valor = float(input("Qual o valor que deseja depositar? ").replace(",", "."))
        if valor >0:
            saldo += valor
            timed = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
            extrato += f"Deposito de R${valor:.2f} as {timed} \n" #Concatenando string com int
            print(f"\n\nDepósito de R${valor:.2f} realizado com sucesso! \n\n")
        else:
            print("\n\nOperação inválida, por favor insira um valor positivo \n\n")
    

    elif opcao == "s":
        print("\n\nSaque")
        valor = float(input("Qual o valor que deseja sacar? ").replace(",", "."))
        if valor <= 500 and valor > 0:
            if numero_saques < LIMITE_SAQUES: #se eu colocar o = ele vai permitir 4 saques
                if valor <= saldo:
                    print(f"\n\nSaque de R${valor:.2f} realizado com sucesso! \n\n")
                    saldo -= valor
                    numero_saques += 1
                    times = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
                    extrato += f"Saque de R${valor:.2f} as {times}\n"
                else:
                    print("\n\nOperação inválida, por favor insira um valor menor que o saldo \n\n")
            else:
                print("\n\nOperação inválida, você já atingiu o limite de saques \n\n")
        else:
            print("\n\nOperação inválida, por favor insira um valor inteiro positivo maior que R$0 e menor que R$500\n\n")


    elif opcao == "e":
        print("========================EXTRATO========================\n\n")
        print(f"Foram realizados {numero_saques} saques")
        print(f"Seu saldo é: R$ {saldo} ")
        print("Não foram realizadas movimentaçõs." if not extrato else extrato)
        print("\n\n========================FIM========================")

    elif opcao == "q":
        break

    else:
        print("\n\nOperação inválida, por favor selecione novamente a operação desejada\n\n")
    