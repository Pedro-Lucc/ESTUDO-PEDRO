nome = str(input('Qual é seu nome? ')).title()
turma = float(input('Qual é a sua turma? '))
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota2 + nota1) / 2

if media < 5:
    print(f'VOCÊ ESTÁ REPROVADO, {nome} da turma {turma}')
elif media >= 5 and media < 7:
    print(f'VOCÊ ESTÁ DE RECUPERAÇÃO, {nome} da turma {turma}')
elif media >= 7:
    print(f'VOCÊ ESTÁ APROVADO, {nome} da turma {turma}')
print(f'Sua média semestral foi: {media}')