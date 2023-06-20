# FATIAMENTO DE STRINGS

frase = 'Curso em Vídeo Python\n'

print(frase.upper())
print('mostra a localização da string 3')
print(frase[3])
print('\nmostra um print valor entre 3 a 13, sendo que o valor vai somente até o 12')
print(frase[3:13])
print('\nmostra um print do começo da frase, com a primeira letra, até o caractere 12, sendo que o 13 não entra')
print(frase[:13])
print('\nmostra um valor de 13 até o último caractere')
print(frase[13:])
print('\nmostra um valor do primeiro caractere até o 14 e pulando de 2 em 2')
print(frase[1:15:2])
print('\nmostra um valor do primeiro até o último caractere, só que pulando de 2 em 2')
print(frase[::2])

print('=~' * 30)


# PARA FAZER A CONTAGEM DE LETRAS NA FRASE "CURSO EM VÍDEO PYTHON
print('\nPARA FAZER A CONTAGEM DE LETRAS NA FRASE "CURSO EM VÍDEO PYTHON')
print(frase.count('o'))

print('=~' * 30)
# PARA SABER O TAMANHO DA FRASE

print('\nPARA SABER O TAMANHO DA FRASE')
print(len(frase))

print('=~' * 30)

# PARA TRANSFORMAR ELA INTEIRAMENTE EM MINÚCULA E MAIÚSUCULA

print('\nPARA MAIÚSCULA')
print(frase.upper())

print('\nPARA MINÚCULA')
print(frase.lower())

print('=~' * 30)

# PARA SABER O TAMANHO DA FRASE

print('\nPARA SABER O TAMANHO DA FRASE')
print(len(frase))

# USANDO O STRIP PARA REMOVER OS ESPAÇOS

print('\nPARA SABER O TAMANHO DA FRASE SEM OS ESPAÇOS')
print(len(frase.strip()))

print('=~' * 30)

# PARA TROCAR UMA PALAVRA PELA OUTRA
print('\nPARA TROCAR UMA PALAVRA PELA OUTRA')
print(frase.replace("Python", 'Android'))

print('=~' * 30)

# PARA ACHAR A POSIÇÃO DA PALAVRA
print('PARA ACHAR A POSIÇÃO DA PALAVRA')
print(frase.find("Vídeo"))

print('=~' * 30)

# PARA CRIAR UMA LISTA COM AS PALAVRAS DENTRO DA FRASE

print('PARA CRIAR UMA LISTA DAS PALAVRAS DENTRO DA FRASE')
print(frase.split())