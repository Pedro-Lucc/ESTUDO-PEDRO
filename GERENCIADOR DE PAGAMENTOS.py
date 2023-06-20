print('====== LOJAS PEDRINHO ====== ')
preço = float(input('Preço do produto: R$'))

print('\nQual será a forma de pagamento?'
      '\n[ 1 ] À VISTA NO DINHEIRO'
      '\n[ 2 ] À VISTA NO CARTÃO DE CRÉDITO'
      '\n[ 3 ] EM ATÉ 2x NO CARTÃO'
      '\n[ 4 ] 3x OU MAIS NO CARTÃO')

escolha = int(input('\nQual será a opção de pagamento? '))

if escolha == 1:
    pagamento = preço - (preço * 0.1)
    print(f'O valor da compra será de R${pagamento:.2f}')

elif escolha == 2:
    pagamento = preço - (preço * 0.05)
    print(f'O valor da compra será de R${pagamento:.2f}')

elif escolha == 3:
    pagamento = preço / 2
    print(f'\nO valor da compra será de R${preço:.2f}'
          f'\nSendo o valor da parcela R${pagamento:.2f}')

elif escolha == 4:
    pagamento = preço + (preço * 0.2)
    tparcelas = int(input('Quantas parcelas? '))
    parcelas = pagamento / tparcelas
    print(f'\nO valor da compra será de R${pagamento:.2f}'
          f'\nSendo o valor da parcela R${parcelas:.2f} ')
else:
    print('\033[1;31mOPÇÃO INVÁLIDA\033[m')