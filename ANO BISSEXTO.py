ano = int(input('Digite o ano de preferência. E 0 (zero) para o ano atual: '))
c = 2020 - ano

if c == 4 or -4:
    print(f'Esse ano é bissexto!')
else:
    print(f'Esse ano não é bissexto!')