produto = float(input('Qual o valor do produto? '))
desconto = produto * 0.05
descontado = produto - desconto

print(f'O desconto de 5% no valor R${produto:.2f} será de R${desconto:.2f}')
print(f'O valor do produto com o desconto será de R${descontado:.2f}')

