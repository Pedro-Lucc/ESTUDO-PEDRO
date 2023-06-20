d = float(input('Digite a distância da viagem: '))

if d <= 200:
    c = d * 0.50
    print(f'A viagem será de {d:.0f}Km')
    print(f'O preço da passagem é R${c:.2f}')

else:
    c = d * 0.45
    print(f'A viagem será de {d:.0f}Km')
    print(f'O preço da passagem é R$ {c:.2f} ')