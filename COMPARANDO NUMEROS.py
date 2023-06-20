print('\033[1;31m  COMPARANDO\033[m NÚMEROS\n')

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

if n1 > n2:
    print('\nO \033[1;36mPRIMEIRO0\033[m número é maior')
    print(f'{n1:.0f} > {n2:.0f}')
elif n2 == n1:
    print('OS números são \033[1mIGUAIS\033[m')
    print(f'{n1:.0f} = {n2:.0f}')
else:
    print(f'O \033[1;33mSEGUNDO\033[m número é maior')
    print(f'{n2:.0f} > {n1:.0f}')
