dinheiro = float(input('Quanto de dinheiro você tem? R$'))
dolar = 5.20
euro = 5.24
libraEstrelina = 6.22
iene = 0.0038
pesoArgentino = 0.043


cd = dinheiro / dolar
ce = dinheiro / euro
cl = dinheiro / libraEstrelina
ci = dinheiro / iene
cp = dinheiro / pesoArgentino

print(f'Você tem ${cd:.2f} Dolares')
print(f'Você tem ${ce:.2f} Euros')
print(f'Você tem ${cl:.2f} Libras Estrelina')
print(f'Você tem ${ci:.2f} Ienes')
print(f'Você tem ${cp:.2f} Pesos Argentinos')
