def menu():
    print('''  ======= MENU =======
    [1] depositar
    [2] sacar
    [3] extrato
    [0] sair
======================
''')
menu()

valor = 0
saldo = 0
limite_saque = 500
extrato = ''
LIMITE_SAQUES = 3
saques = 0

def depositar(saldo, extrato, valor, /):
    valor = float(input('Informe o valor para deposito: '))

    if valor >= 1:
        saldo += valor
        extrato += f'Deposito: R$ {valor:.2f}\n'
        print('Deposito realizado com sucesso. ')
    else:
        print('Informe um número válido. ')

    return saldo, extrato

def sacar(*, saldo, valor, extrato):
    valor = float(input('Informe o valor para saque: ' ))
    global limite_saque
    global LIMITE_SAQUES
    global saques

    if valor <= saldo:

        if saques <= LIMITE_SAQUES and valor <= limite_saque:
            print('Saque realizado com sucesso. Retire o dinheiro no local indicado.')

            if valor > 0:
                saques += 1
                saldo -= valor
                limite_saque -= valor
                extrato += f'Saque: R$ {valor:.2f}\n'            
        else:
            print('Você excedeu o limite de saques diários.')

    else:
        print('Você não possui saldo suficiente. Tente um valor menor.')    
    return (saldo, extrato)
    

def exibir_extrato(saldo, extrato, /):
    print('========== Extrato ==========')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'Saldo: R$ {saldo:.2f}')
    print('-' * 29)
    return extrato

while True:
    opcao = int(input('Informe a opção desejada: '))

    if opcao == 1: #opção depositar
        saldo, extrato = depositar(saldo, extrato, valor)       
    
    elif opcao == 2: #opção sacar
        saldo, extrato = sacar(saldo = saldo, valor = valor, extrato = extrato)
              
                
    
    elif opcao == 3: #opção extrato
        exibir_extrato(saldo, extrato)
        
    
    elif opcao == 0:
        print('Obrigado por usar nossos serviços.')
        break

    else:
        print('Digite uma opção válida. ')