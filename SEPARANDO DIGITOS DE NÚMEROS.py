n = float(input('Digite um número: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

# Aqui o cálculo vai pegar a divisão inteira e o resultado será dividido pelo resto da divisão, assim dando o número necessário

print(f'Analisando o número {n:.0f}')
print(f'Unidade = {u:.0f}')
print(f'Dezena = {d:.0f}')
print(f'Centena = {c:.0f}')
print(f'Milhar = {m:.0f}')