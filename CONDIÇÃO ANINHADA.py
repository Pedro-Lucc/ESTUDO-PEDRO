nome = input('QUAL É O SEU NOME? ')

if nome == "Pedro":
    print('NOSSA QUE NOME LINDO!')
elif nome == 'João' or nome == 'Maria' or nome == 'Gustavo':
    print('SEU NOME É FOFO!!!')
elif nome in 'Ana Paula Lucia':
    print('QUE NOME FEMININO LINDO!!!')
else:
    print('SEU NOME É LEGAL')
print(f'TENHA UM ÓTIMO DIA, {nome.upper()}')

