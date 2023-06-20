import random

n1 = input('nome 1 é: ')
n2 = input('nome 2 é: ')
n3 = input('nome 3 é: ')
n4 = input('nome 4 é: ')

lista = [n1, n2, n3, n4]
random.shuffle(lista)

print(f'A ORDEM DA LISTA SERÁ:\n {lista} ')


