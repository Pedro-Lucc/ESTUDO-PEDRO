#DEFININDO UMA FUNÇÃO COM UMA VARIÁVEL OPCIONAL

#TODOS OS ARGUMENTOS PODEM SER VARIÁVEIS OPCIONAIS
def somar(a, b, c=0):
    '''
    -> faz a soma dos três valores e mostra o resultado na tela
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    '''
    s = a + b + c
    print(f'a soma vale {s}')

somar(3, 2, 5)
somar(3,3)
