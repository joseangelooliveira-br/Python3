print('{:=^40}'.format('LOJAS ANGELO'))
preco = float(input('Valor total das compras:R$ '))
print('''Formas de Pagamento:
[1] à vista dinheiro/cheques.
[2] à vista no cartão.
[3] 2x no cartão.
[4] 3x ou mais no cartão.''')
opcao = int(input('Qual a opção de Pagamento: '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
    print('Voce terá 10% de desconto, sua compra de R${:.2f}, sairá por R${:.2f}'.format(preco,total))
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print('Voce terá 5% de desconto, sua compra de R${:.2f}, sairá por R${:.2f}'.format(preco,total))
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra de R${:.2f}, terá parcelas de R${:.2f}'.format(total, parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparcelas = int(input('quantas parcelas voce deseja: '))
    parcela = total / totparcelas
    print('Sua compra de R${:.2f}, terá parcelas de R${:.2f}, totalizando R${:.2f}'.format(preco, parcela, total))
else:
    print('Voce selecionou opção inexistente.')