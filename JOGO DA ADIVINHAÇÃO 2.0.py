from random import randint
from pyfiglet import Figlet
from termcolor import colored

numSec = randint(0, 10)
acertou = False
palpites = 0

titulo = Figlet(font='slant')
print(colored(titulo.renderText("ADIVINHACAO")))

while not acertou:
    tentativa = int(input("\nTente adivinhar o número secreto: "))
    palpites += 1
    if tentativa == numSec:
        acertou = True
    else:
        if tentativa < numSec:
            print('O número secreto é MAIOR!')

        elif tentativa > numSec:
            print('O número secreto é MENOR!')

print(F'Você acertou o número secreto!!! NUMERO SECRETO = {numSec}')
print(f'Quantidade de tentativas: {palpites}')

