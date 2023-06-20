# PROGRAMA PARA LER 6 NUMEROS E MOSTRAR A SOMA DOS PARES SOMENTE. CASO O VALOR DA SOMA SEJA IMPAR, DESCONSIDERAR
# CRIANDO VARIÁVEIS PARA PODER USA-LAS NO FOR
soma = 0
cont = 0

# CRIANDO UM FOR PARA DETERMINAR O QUANTO DE VEZES QUE O EVENTO IRÁ SE REPETIR
for numero in range(1, 7):
    # PEDINDO PARA QUE O USUÁRIO INSIRA OS 6 NÚMEROS
    num = int(input(f'Digite o {numero}º número: '))
    # IF ALOCADO PARA SABER SE O NÚMERO É PAR
    # CASO SAIBA, ELE SERÁ SOMADO
    # O "cont" SERVE PARA SABER QUANTOS NÚMEROS PARES FORAM INFORMADOS
    if num % 2 == 0:
        soma += num
        cont += 1
print(f"informando {cont} números pares a soma deles é {soma}")


# PROGRAMA PARA LER 6 NUMEROS E MOSTRAR A SOMA DOS PARES SOMENTE. CASO O VALOR DA SOMA SEJA IMPAR, DESCONSIDERAR
# CRIANDO VARIÁVEIS PARA PODER USA-LAS NO FOR
soma = 0
cont = 0

# CÓDIGO LIMPO
for numero in range(1, 7):
    num = int(input(f'Digite o {numero}º número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f"informando {cont} números pares a soma deles é {soma}")