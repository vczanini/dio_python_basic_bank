#Variaveis

menu = """
Selecione a operação:
1: depositar
2: verificar extrato
3: sacar
4: sair
"""

saldo = 0
limite_saque = 500
quantidade_saques = 0
mensagem_extrato = ""
movimentacao = 'N'

while True:
    escolha = input(menu)
    
    if escolha == "1":
        valor = float(input("Informe o valor do depósito"))
        
        if valor > 0:
            saldo += valor
            mensagem_extrato += f"Depósito: + R$ {valor:.2f}\n"
            if movimentacao =='N':
                movimentacao = 'S'
        else:
            print("Erro na operação! digite apenas os números.")
    elif escolha == "2":
        if movimentacao == 'N':
            print("Não foram feitas movimentações ainda!")
        else:
            print("EXTRATO!!\n")
            print(f"{mensagem_extrato}\n")
            print(f"Saldo: {saldo}")
    elif escolha == "3":
        valor = float(input("Informe o valor do saque"))
        if valor > 0:
            if valor > 500:
                print("Valor maior que o limite de 500 reais")
            elif quantidade_saques == 3:
                print("Já foram realizado os 3 saques diarios.")
            elif valor > saldo:
                print("Saldo insuficiente para o saque")
            else:
                saldo -= valor
                mensagem_extrato += f"saque: - R$ {valor:.2f}\n"
                quantidade_saques += 1
        else:
            print("Erro na operação! digite apenas os números.")
    elif escolha == "4":
        break;
    else:
        print("Escolha indisponivel\n")