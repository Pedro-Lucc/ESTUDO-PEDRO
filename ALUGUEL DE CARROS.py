# carro custa R$60 por dia
# a cada Km rodado o valor cobrado será R$0.15

dias = int(input('Quantidade de dias alugado? '))
km = float(input('Quantidade de Km rodados? '))

preço = (dias * 60) + (km * 0.15)

print(f'O preço total a ser pago é R${preço:.2f}')
print(f'\nsendo:\nR${dias * 60:.2f} o valor dos dias\nR${km * 0.15:.2f} o valor da quilometragem')