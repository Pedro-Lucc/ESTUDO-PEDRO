import random

nome1 = input('DIGITE O PRIMEIRO NOME: ')
nome2 = input('DIGITE O SEGUNDO NOME: ')
nome3 = input('DIGITE O TERCEIRO NOME: ')
nome4 = input('DIGITE O QUARTO NOME: ')

lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)

print(f'O NOME ESCOLHIDO FOI: {escolhido}')

