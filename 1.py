nome = str(input('Digite seu nome: ')).upper()

if nome == "PEDRO":
    print(f'Seu nome é bonito, {nome.title()}!.')

elif nome == "LUCAS" or nome == "MARIA" or nome == "João":
    print(f'Seu nome é muito popular no Brasil, {nome.title()}.')

elif nome in "LUIZA JULIA CARLA BEATRIZ":
    print(f'Belo nome feminino, {nome.title()}.')

else:
    print(f'Seu nome não é lindo como o do Pedro, {nome.title()}.')

print(f'Tenha um bom dia, {nome.title()}.')
