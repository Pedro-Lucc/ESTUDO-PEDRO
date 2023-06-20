# criação de um programa que calcula a soma de todos os numeros impares multiplos de 3 entre 1 e 500


# criação de uma variável para que possa acumular valores para a soma dos mesmos
soma = 0
print("OS NÚMEROS IMPARES MULTIPLOS DE 3 ENTRE 0 E 500 SÃO: ")


# for para definir o intervalor entre os números. Ele foi colocado entre 1 e 501
# pq só assim ele pegará os números ímpares entre esses valores
for impares in range(1, 501, 2):

    # o % 3 == 0 é para pegar os que são multiplos por 3
    if impares % 3 == 0:

        # essa operação foi feita para somar todos os números impares multiplos de 3
        soma += impares
    print(impares)
print(f"A soma de todos os valores é {soma}")
