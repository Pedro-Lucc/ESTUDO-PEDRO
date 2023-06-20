n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: ')

print('[ 1 ] converter para \033[1;31m BINÁRIO \033[m')
print('[ 2 ] converter para \033[1;32m HEXADECIMAL \033[m')
print('[ 3 ] converter para \033[1;33m OCTAL \033[m')

opção = int(input('\nSua opção: '))

if opção == 1:
    print(f'Convertendo o número {n} para \033[1;31m BINÁRIO \033[m --> {bin(n)[2:]}')
elif opção == 2:
    print(f'Convertendo o número {n} para \033[1;32m HEXADECIMAL \033[m --> {hex(n)[2:]}')
else:
    print(f'Convertendo o número {n} para \033[1;33mOCTAL \033[m --> {oct(n)[2:]}')
