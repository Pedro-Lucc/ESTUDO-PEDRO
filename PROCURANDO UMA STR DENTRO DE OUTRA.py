# 1º versão
nome = str(input('Digite o seu nome? ')).strip()
print(f'Seu nome tem "Silva"? {"SILVA" in nome.upper()}\n')

# 2º versão
nome = str(input("Qual é seu nome completo? ")).strip()
print('seu nome tem silva? {}\n'.format("silva" in nome.lower()))

# 3º versão
nome = str(input('Qual o seu nome inteiro? ')).strip()
divisãoNomes = nome.upper().split()
print(f'O seu nome tem "Silva"? {"SILVA" in divisãoNomes}\n')

# 4º versão
nome = str(input('Qual o seu nome inteiro? ')).strip().upper().split()
print(f'O seu nome tem "Silva"? {"SILVA" in nome}\n')












































