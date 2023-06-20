print('=~' * 20)
print('ANALISANDO A EXISTÊNCIA DE TRIÂNGULOS')
print('=~' * 20)

r1 = float(input('\nDigite o primeiro segmento de reta: '))
r2 = float(input('Digite o segundo segmento de reta: '))
r3 = float(input('Digite o terceiro segmento de reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'\nO triângulo PODE existir!!!\n')

    if r1 == r2 == r3:
        print('O triângulo é EQUILÁTERO!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo é ISÓCELES!')
    elif r1 != r2 or r1 != r3 or r2 != r3:
        print('O triângulo é ESCALENO')

else:
    print(f'O triângulo NÃO PODE existir!!!')

