peso = float(input('Qual o seu pesos (Kg)? '))
altura = float(input('Qual é a sua altura (m)? '))

imc = peso / (altura ** 2)


if imc < 18.5:
    print(f'IMC de {imc:.1f}. Você está ABAIXO DO PESO')

elif 18.5 >= imc < 25:
    print(f'IMC de {imc:.1f}. Você está com o PESO IDEAL')

elif 25 >= imc < 30:
    print(f'IMC de {imc:.1f}. Você está com SOBREPESO')

elif 30 <= imc < 40:
    print(f'IMC de {imc:.1f}. Você está com OBESIDADE')

else:
    print(f'IMC de {imc:.1f}. Você está com OBESIDADE MÓRBIDA')



