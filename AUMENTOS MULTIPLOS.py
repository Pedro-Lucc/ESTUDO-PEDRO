salario = float(input('Qual o seu salário? R$ '))

if salario <= 1250.00:
    aumento15 = salario * 0.15
    soma = aumento15 + salario
    print(f'Quem ganhava um salário de R${salario:.2f} passará a ganhar R${soma:.2f}')
else:
    aumento10 = salario * 0.10
    soma = aumento10 + salario
    print(f'Quem ganhava um salário de R${salario:.2f} passará a ganhar {soma:.2f}')
