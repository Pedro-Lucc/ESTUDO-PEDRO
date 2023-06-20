print('=-' * 8)
print('RADAR VIRTUAL')
print('=-' * 8)

velocidade = float(input('\nQual é a velocidade do carro? '))

if velocidade <= 80:
    print('A velocidade estava dentro do pradrão. Tenha um bom dia!')
else:
    multa = (velocidade - 80) * 7
    print(f'Excedeu o limite de velocidade. Você foi multado em R${multa:.2f} por dirigir acima de 80Km/h')
