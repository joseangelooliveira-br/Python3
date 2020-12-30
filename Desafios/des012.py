precoatual = float(input('Digite o preço do Produto: R$ '))
Desconto = float(input('Digite o valor de desconto: % '))
novopreço = precoatual-(precoatual*Desconto/100)
print('Preço do produto com desconto será de R${:.2f}'.format(novopreço))