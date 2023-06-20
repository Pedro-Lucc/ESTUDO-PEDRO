cidade = str(input('Digite o nome da cidade: ')).replace("-"," ").split()
print(cidade[0].upper() == "SANTO")


# O ".strip" foi usado para evitar que dê erro caso uma pessoa coloque várias vezes espaços antes e depois da frase

# O "cidade[:5]" foi usado para limitar à palavra "santo", já que ela possui 5 letras, assim não seria possível escolher
# outra palavra

# O ".upper" foi usado para caso alguém digitar "Santo" de uma forma diferente, com maiúsculas ou minúsculas

# O "== "SANTO" " foi usado para conferir se a palavra digitada foi "SANTO", pois ela já foi transformada em maiúscula.
