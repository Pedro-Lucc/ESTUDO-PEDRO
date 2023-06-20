import math

num = float(input('digite um número: '))
inteiro = math.trunc(num)

print(f'O número digitado é {num} e sua porção inteira é {inteiro}')

# OU PODE SER FEITO DESSE JEITO

print(f'O número digitado é {num} e sua porção inteira é {int(inteiro)}')
