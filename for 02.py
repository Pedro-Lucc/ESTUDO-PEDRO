# programa para mostrar todos os números pares no intervalo de 0 a 50
# uso do for + range para definir o intervalo
# o terceiro argumento do range serve para pular de 2 em 2, já que a proposta é par
# o end=' ' serve para deixar todos os valores do print na mesma linha

print('os numeros pares que estão entre 0 e 50 são: ')
for par in range(0, 52, 2):
    print(par, end=' ')
