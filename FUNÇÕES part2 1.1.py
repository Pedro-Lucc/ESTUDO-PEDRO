#ESCOPODE VARIÁVEI
def teste(b):
    #neste caso, declarando a GLOBAL aqui, ela funcionará tanto dentro
    #da função quanto fora, ou  seja, se eu declarar qualquer "a" dentro da
    #função como global, ele será o chefe de tudo e todos fora da função serão
    #obsoletos.
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


#o a aqui é GLOBAL, então ele vai poder entrar dentro da função
a = 5
teste(a)
print(f'Afora vale {a}')