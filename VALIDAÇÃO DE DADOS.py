print("\033[1;32mVALIDAÇÃO DO SEXO \033[m")

sexo = str(input("DIGITE QUAL O SEU SEXO [M/F]: ")).upper().strip()

while sexo not in "MF":
    sexo = str(input("ERROS - DIGITE NOVEMENTE O SEXO [M/F]: "))

if sexo == 'F':
    print('O sexo escolhido foi: FEMININO')

elif sexo == 'M':
    print('O sexo escolhido foi: MASCULINO ')


