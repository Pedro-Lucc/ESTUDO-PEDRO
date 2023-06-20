sexo = str(input('Digite qual é o seu sexo (M ou F): ')).upper()

while sexo != "M" and sexo != "F":
    sexo = input('Dados inválidos. Por favor, digite novamente: ')

print(f"sexo {sexo} registrado com sucesso!")
