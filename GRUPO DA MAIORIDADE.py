from datetime import date

atual = date.today().year
tmenor = 0
tmaior = 0

for p in range(0, 7, 1):
    p += 1
    nasc = int(input(f'Em que ano a {p}º pessoa nasceu? '))
    idade = atual - nasc

    if idade <= 21:
        tmenor += 1
    else:
        tmaior += 1

print(f'\nA quantidade de pessoas MAIORES DE IDADE é {tmaior}')
print(f'A quantidade de pessoas MENORES DE IDADE é {tmenor}')
