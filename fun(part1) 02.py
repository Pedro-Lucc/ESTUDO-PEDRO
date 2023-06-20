#FUNÇÃO PARA ADAPTAR AS LINHAS COM UM TEXTO
def escreva(texto):
    tam = len(texto)
    print('-' * tam)
    print(texto)
    print('-' * tam)

texto = input('DIGITE UM TEXTO: ')
escreva(texto)


#escreva("ola mundo")
#escreva("macaco")
#escreva("mouse")
#escreva("a cidade de são paulo é muito suja")