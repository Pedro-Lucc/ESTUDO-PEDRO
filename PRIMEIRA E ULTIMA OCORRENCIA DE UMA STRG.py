fraseComAcent = str(input("Digite uma frase: \n")).strip().lower()
a = fraseComAcent.count("a") + fraseComAcent.count("ã") + fraseComAcent.count("á") + fraseComAcent.count(
    "à") + fraseComAcent.count("â")
# Foi usado uma transformação da frase para que pudesse pegar todos os tipos de "a"

print(f'\nQuantas vezes apareceu a letra "A"?')
print(f'RESPOSTA: Apareceram {a} vezes a letra "A"\n')

print(f'Em que posição apareceu a primeira letra?')
print(f'RESPOSTA: A primeira letra apareceu na posição {fraseComAcent.find("a") + 1}\n')
# Foi usado o "find" para fazer a contagem da posição da primeira letra
# O "+1" foi utilizado para mostrar uma posição mais entendivel, ou seja, a posição não é 0 e sim 1


print(f'Em que posição ela apareceu pela última vez?')
print(f'RESPOSTA: A última letra apareceu pela última vez na posição {fraseComAcent.rfind("a") + 1}')
# A mesma lógica do "find" foi usada, só que, para termos o último termo foi usado a letra "r" para começar de trás para
# frente
