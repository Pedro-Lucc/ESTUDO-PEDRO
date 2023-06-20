from datetime import date

anoNascimento = int(input('Qual o seu ano de nascimento: '))
atual = date.today().year
idade = atual - anoNascimento

if idade <= 9:
    print(f'Você tem {idade} anos, sua classe é MIRIM!')
elif idade > 9 and idade <= 14:

    print(f'Você tem {idade} anos, sua classe é INFANTIL!')
elif idade > 14 and idade <= 19:

   print(f'Você tem {idade} anos, sua classe é JUNIOR!')
elif idade > 19 and idade <= 25:

    print(f'Você tem {idade} anos, sua classe é SÊNIOR!')
else:
    print(f'Você tem {idade} anos, sua classe é MASTER!')

