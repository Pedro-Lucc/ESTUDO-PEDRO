from time import sleep

def contador(inicio, fim, passo):
    print(f'contagem de {inicio} até o {fim} pulando de {passo} em {passo}')
    sleep(1.0)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end='', flus=True)
            sleep(0.5)
            cont += passo
        print('FIM')
    else:
        cont = 1
        while cont >= fim:
            print(f'{cont}', end='', flus=True)
            sleep(0.5)
            print('FIM')


inicio = input("INICIO: ")
fim = input('FIM: ')
passo = input('PASSO: ')
contador(inicio, fim, passo)
