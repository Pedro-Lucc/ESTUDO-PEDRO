# EXERCÍCIO DE MOSTRAR A TABUADA DE UM NUMERO INSERIDO USANDO FOR
# DEFININDO UMA VARIÁVEL PARA QUE POSSA TER A ENTRADA DO NÚMERO
NUM = int(input(("DIGITE UM NÚMERO PARA SABER A TABUADA: ")))

# CRIANDO UM FOR PARA FAZER O MOLDE DA TABUADA DE 1 A 10
for c in range(1, 11):
    # PRINT PARA FAZER A RESOLUÇÃO DO CÁLCULO
    # MOSTRAR QUAL O NÚMERO SOLICITADO PELO USUÁRIO -----> f"{tabuada}
    # MOSTRAR UM RANGE DE 1 A 10 -----> {c}
    # FAZER O CÁLCULO DA OPERAÇÃO, PEGANDO A COLOCAÇÃO DA TABUADA E O NUMERO INSERIDO -------> {c * tabuada}
    print(f"{NUM} x {c} = {c * NUM}")