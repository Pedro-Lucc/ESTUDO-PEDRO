def contador(* num):
    #DEFINDO A VARIÁVEL "TAM" DE ACORDO COM O TAMANHO RECEBIDO PELO ARGUMENTO DA FUNÇÃO
    #ELA SERVE PARA CONTAR QUANTOS NÚMERO EXISTEM NO ARGUMENTO DAS TUPLAS.
    tam = len(num)
    print(f'recebi os valores {num} e são {tam} numeros')


contador(2, 3, 5)
contador(2, 3, 4, 5, 5)
contador(8, 9, 10, 11, 12, 13)
