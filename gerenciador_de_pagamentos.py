print('{:=^40}'.format('Lojas de cachaça artesanal'))
preço = float(input('Preço das compras: R$ '))
print('''Formas de pagamento:
[1] À vista dinheiro/cheque
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))

if opção == 1:
    total = preço - (preço * 10 / 100)
    print('Sua compra será de R$ {:.2f} com 10% de desconto.'.format(total))
elif opção == 2:
    total = preço - (preço * 5 / 100)
    print('Sua compra será de R$ {:.2f} com 5% de desconto.'.format(total))
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} sem juros.'.format(parcela))
elif opção == 4:
    totparc = int(input('Quantas parcelas? '))
    total = preço + (preço * 20 / 100)
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R$ {:.2f} com juros.'.format(totparc, parcela))
else:
    print('Opção inválida de pagamento')

print('Total a pagar: R$ {:.2f}'.format(total))
