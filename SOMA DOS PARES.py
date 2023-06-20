soma = 0
cont = 0
for numeros in range(1, 7):
    n = int(input(f"Digite o {numeros}º valor: "))
    if n % 2 == 0:
        soma += n
        cont += 1

print(f'\nA soma dos números pares é {soma}')
print(f'Você informou {cont} números pares')

