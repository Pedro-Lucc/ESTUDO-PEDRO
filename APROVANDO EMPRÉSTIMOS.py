casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quanto tempo será pago? (anos) '))

prestação = casa / (anos * 12)
mini = salario * 0.3

print(f'\nValor da casa R${casa:.2f}')
print(f'Seu salario R${salario:.2f}')
print(f'A prestação será de R${prestação:.2f}')

if prestação <= mini:
    print(f'O empréstimo pode ser \033[1;32mCONCEDIDO! ')
else:
    print(f'O empréstimo foi \033[0;31mNEGADO!')




