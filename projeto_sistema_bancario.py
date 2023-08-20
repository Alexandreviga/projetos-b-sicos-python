menu = '''  ======= MENU =======
    [1] depositar
    [2] sacar
    [3] extrato
    [0] sair
======================
'''
print(menu)

saldo = 0
limite_saque = 500
extrato = ''
LIMITE_SAQUES = 3
saques = 0

while True:
    opcao = int(input('Informe a opção desejada: '))


    if opcao == 1: #opção depositar
        valor = float(input('Informe o valor para deposito: ' ))

        if valor >= 1:
            print('Deposito realizado com sucesso. ')
            print()
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'        
        else:
            print('Informe um número válido. ')
            
    
    elif opcao == 2: #opção sacar
        valor = float(input('Informe o valor para saque: ' ))

        if valor <= saldo: 

            if saques <= limite_saque and valor <= limite_saque:
                print('Saque realizado com sucesso. Retire o dinheiro no local indicado.')
                saques += 1
                saldo -= valor
                limite_saque -= valor
                extrato += f'Saque: R$ {valor:.2f}\n'
            else:
                print('Você excedeu o limite de saques diários.')

        else:
            print('Você não possui saldo suficiente. Tente um valor menor.')
    
    elif opcao == 3: #opção extrato
        print('========== Extrato ==========')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}')
        print('-' * 29)
    
    elif opcao == 0:
        print('Obrigado por usar nossos serviços.')
        break

    else:
        print('Digite uma opção válida. ')
            




   


        
        
