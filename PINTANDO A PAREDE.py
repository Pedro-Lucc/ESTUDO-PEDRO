print('=== DESCOBRINDO A METRAGEM DA PAREDE ===\n')
largura = float(input('Qual a largura da parede? '))
comprimento = float(input('Qual o comprimento da parede? '))


area = largura * comprimento
tinta = area / 2

print(f'\nA parede tem:\n{largura}m de largura')
print(f'{comprimento}m de comprimento')
print(f'{area}m² de área')
print(f'A quantidade de tinta necessária será de {tinta}L')