# EXPLICANDO O RETURN
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


#NESTE CASO, O "R1, R2 E R3" SÃO POSTOS PARA QUE POSSAM SER ALOCADOR EM
#UMA RESPOSTA JÁ COM OS CÁLCULOS DA FUNÇÃO, POIS SE NÃO FOREM DEFINIDOS
#NÃO SERÁ POSSÍVEL IMPRIMI-LOS

r1 = somar(3, 2, 1)
r2 = somar(3, 2)
r3 = somar(3)

print(f'os resultados foram {r1}, {r2} e {r3}')