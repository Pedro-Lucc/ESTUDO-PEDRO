primeiro = int(input('QUAL O PRIMEIRO TERMO? '))
razao = int(input('QUAL A RAZÃO? '))
décimo = primeiro + (10 - 1) * razao

for c in range(primeiro, décimo + razao, razao):
    print(f'{c}', end=' → ')
    # print('{}'.format(c), end='→ ')
print('ACABOU')
