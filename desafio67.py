# DESAFIO 67 TABUADA


while True:
    n = int(input("\nTabuada desejada: "))
    if n < 0:
        break
    for c in range(1, 11):
        print(f"{n} x {c} = {c*n}")
print('NÃO PODE NÚMERO NEGATIVO!')