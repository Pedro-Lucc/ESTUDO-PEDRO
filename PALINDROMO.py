frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

'''for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''

if junto == inverso:
    print(f'\n{junto} = {inverso}')
    print('A FRASE É UM PALÍNDROMO')
else:
    print(f'\n{junto} ≠ {inverso}')
    print('A FRASE NÃO É UM PALÍNDROMO')

