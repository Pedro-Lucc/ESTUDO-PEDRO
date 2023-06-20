primeiro = float(input('Digite o primeiro valor: '))
segundo = float(input('Digite o segundo valor: '))
terceiro = float(input('Digite o terceiro valor: '))

# DEFININDO QUEM É O MAIOR
maior = primeiro
if segundo > primeiro and segundo > terceiro:
    maior = segundo
if terceiro > primeiro and terceiro > segundo:
    maior = terceiro

# DEFININFO QUEM É O MENOR
menor = primeiro
if segundo < primeiro and segundo < terceiro:
    menor = segundo
if terceiro < primeiro and terceiro < segundo:
    menor = terceiro

# PRINTANDO OS RESULTADOS
print(f'O maior valor foi o {maior:.0f}')
print(f'O menor valor foi o {menor:.0f}')

