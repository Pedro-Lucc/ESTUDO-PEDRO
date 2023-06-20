from random import randint

print('=-' * 25)
print('!!!! TENTE ADIVINHAR O NÚMERO SECRETO !!!!')
print('=-' * 25)

n = int(input('Digite um número: '))
numSec = randint(0, 10)

if n != numSec:
    print('QUE PENA, VOCÊ ERROU O NÚMERO SECRETO ;(')
else:
    print('PARABÉNS!!!! VOCÊ ACERTOU O NÚMERO SECRETO!!!!')
