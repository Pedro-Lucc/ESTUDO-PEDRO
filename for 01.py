# faça um programa que mostre na tela uma contagem regressiva para o estouro
# de fogos de artifio, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
print("É QUASE ANO NOVO, JÁ JÁ VAI COMEÇAR A CONTAGEM DA VIRADA!!!!")
print('VAMOS COMEÇAR A CONTAGEM!!!')

for c in range(10, 0, -1):
    print(c)
    sleep(0.8)
print('FELIZ ANO NOVOOOOO!!!!!')
