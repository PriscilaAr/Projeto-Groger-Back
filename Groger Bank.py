print('Bem Vindo ao GROGER BANK, para continuar cadastre as seguintes informações: ')

nome = input('Digite seu nome completo: ')
idade = int(input('Digite sua idade: '))
saldo = float(input('Digite o seu saldo: '))

resposta = int(input(' Digite (1) para saque \n Digite (2) para depósito \n Digite (3) para empréstimo \n Digite (4) para visualizar informações \n Digite (Qualquer outro texto ou número) para sair \n'))

if resposta == 1:
    saque = float(input('Digite o valor do saque: '))
    if saque > saldo:
        print('Não foi possivel realizar o saque')
    else:
        print(saldo - saque)

elif resposta == 2:
    deposito = int(input('Digite o valor do depósito: '))
    if deposito > 5000:
        print('O limite do depósito é 5000')
    else:
        print(saldo + deposito)

elif resposta == 3:
    emprestimo = int(input('Digite o valor do empréstimo: '))
    if emprestimo > saldo:
        print('Empréstimo não concedido')
    else:
        print(emprestimo + saldo)

elif resposta == 4:
    print('Nome: ' + str(nome))
    print('Idade: ' + str(idade))
    print('Saldo: ' + str(saldo))

else:
    print('Espero ter te ajudado')