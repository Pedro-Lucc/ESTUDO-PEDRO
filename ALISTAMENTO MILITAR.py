from datetime import date

print('~~~~ \033[1;32mALISTAMENTO MILITAR \033[m~~~~\n')

atual = date.today().year                        # MOSTRA O ANO ATUAL
nascimento = int(input('Ano de nascimento: '))   # PEDE O ANO DE NASCIMENTO
idade = atual - nascimento                       # CALCULA A IDADE DA PESSOA
alistamento = nascimento + 18                    # CALCULANDO O ANO DE ALISTAMENTO


if idade == 18:
    print(f'\nVoce deve se alistar!')

elif idade < 18:
    tempoParaAlistamente = alistamento - (2000 + idade)
    print(f'\nVoce ainda nao precisa se alistar. Faltam {tempoParaAlistamente}')

elif idade > 18:
    tempoParaAlistamente = alistamento - (2000 + idade)
    print(f'\nVoce deveria ter se alistado há {tempoParaAlistamente * (-1)} anos')





'''''
if idade == 18:
    print(f'Você DEVE se alistar. Procure a Junta Militar mais próxima!')

elif idade < 18:
    saldo = 18 - idade
    print(f'Você ainda NÃO PRECISA se alistar! Falta(am) {saldo} ano(os).')

elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos!')

'''''
