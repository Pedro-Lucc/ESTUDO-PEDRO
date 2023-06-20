from random import randint
print('======== \033[1;36mBEM-VINDO AO PEDRA PAPEL E TESOURA\033[m ======== ')

itens = ('Pedra', 'Papel', 'Tesoura')
escolhaC = randint(0, 2)


print('SUAS OPÇÕES SÃO:'
      '\n[ 0 ] PEDRA'
      '\n[ 1 ] PAPEL'
      '\n[ 2 ] TESOURA\n')

escolhaJ = int(input('QUAL A SUA ESCOLHA? '))
print(f'O computador escolheu \033[1;32m{itens[escolhaC].upper()}\033[m')
print(f'O jogador escolheu \033[1;31m{itens[escolhaJ].upper()}\033[m\n')

if escolhaC == 0:
    if escolhaJ == 0:
        print('\033[1m EMPATOU \033[m')

    elif escolhaJ == 1:
        print(f'\033[1;31m{itens[escolhaJ].upper()}\033[m ganha de \033[1;32m{itens[escolhaC].upper()}\033[m')

    elif escolhaJ == 2:
        print(f'\033[1;32m{itens[escolhaC].upper()}\033[m ganha de \033[1;31m{itens[escolhaJ].upper()}\033[m')


elif escolhaC == 1:
    if escolhaJ == 1:
        print('\033[1mEMPATOU \033[m')
        print(f'\033[1;31m{itens[escolhaJ].upper()}\033[m empata com \033[1;32m{itens[escolhaC].upper()}\033[m')

    elif escolhaJ == 2:
        print(f'\033[1;31m{itens[escolhaJ].upper()}\033[m ganha de \033[1;32m{itens[escolhaC].upper()}\033[m')

    elif escolhaJ == 0:
        print(f'\033[1;32m{itens[escolhaC].upper()}\033[m ganha de \033[1;31m{itens[escolhaJ].upper()}\033[m')


elif escolhaC == 2:
    if escolhaJ == 2:
        print('\033[1m EMPATOU \033[m')

    elif escolhaJ == 0:
        print(f'\033[1;31m{itens[escolhaJ].upper()}\033[m ganha de \033[1;32m{itens[escolhaC].upper()}\033[m')

    elif escolhaJ == 1:
        print(f'\033[1;32m{itens[escolhaC].upper()}\033[m ganha de \033[1;31m{itens[escolhaJ].upper()}\033[m')