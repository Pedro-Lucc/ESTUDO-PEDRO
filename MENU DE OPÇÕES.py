from pyfiglet import Figlet
from termcolor import colored
from time import sleep

Titulo = Figlet(font='slant')
print(colored(Titulo.renderText("MENU"), "red"))

print('\033[1mVOCÊ TERÁ AS SEGUINTES OPÇÕES NO MEU    '
      '* ADIÇÃO    '
      '* SUBTRAÇÃO    '
      '* MULTIPLICAÇÃO    '
      '* DIVISÃO    \033[m\n')


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

while True:
    print('[ 1 ] SOMA')
    print('[ 2 ] SUBTRAÇÃO')
    print('[ 3 ] MULTIPLICAÇÃO')
    print('[ 4 ] DIVISÃO')
    print('[ 5 ] SAIR DO MENU')

    escolha = int(input('\nEscolha uma opção: '))

    if escolha == 1:
        soma = num1 + num2
        print(f'{num1} + {num2} = {soma}\n')

    elif escolha == 2 :
        subtracao = num1 - num2
        print(f'{num1} - {num2} = {subtracao}\n')

    elif escolha == 3:
        multiplicacao = num1 * num2
        print(f'{num1} * {num2} = {multiplicacao}\n')

    elif escolha == 4:
        divisao = num1 / num2
        print(f'{num1} / {num2} = {divisao}\n')

    elif escolha == 5:
        print('FINALIZANDO O MENU...')
        sleep(1)
        break
    else:
        print("ERRO - ESCOLHA NOVAMENTE\n")
