nome = input('Digite seu nome completo: ').strip()
# NESSE CASO, PARA EVITAR QUE HAJA EXCESSO DE ESPAÇOS NO COMEÇO E NO FINAL, USA-SE .strip

separa = nome.split()

print(f'Seu nome em maiúsculas é: {nome.upper()}')
print(f'Seu nome em minúculas é: {nome.lower()} ')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')

# AQUI FOI USADO " - nome.count(" ") " PARA EVITAR QUE A CONTAGEM INCLUA OS ESPAÇOS ENTRE O NOME E O SOBRENOME

print(f'Seu primeiro nome é {separa[0]} e ele tem {nome.find(" ")} letras')

# O "separa[0]" SERVE PARA PEGAR O PRIMEIRO NOME, JÁ QUE, O NOME INTEIRO FOI SEPARADO E SALVO EM UMA LISTA, ASSIM
# PERMITINDO QUE FOSE POSSÍVEL PEGAR O PRIMEIRO NOME

# O "nome.find(" ")" SERVE PARA PEGAR O PRIMEIRO NOME E FAZER A CONTAGEM DELE 