imovel = float(input('Digite o valor do imovel: '))
salario = float(input('Digite o valor do salario: '))
anos = int(input('Digite o prazo para pagamento em anos: '))
prestacao = imovel/(anos * 12)
print('O valor da prestção será de R${:.2f}'.format(prestacao))
if prestacao > (salario * 30) / 100:
    print('Seu financiamento foi negado.')
else:
    print('Seu financiamento foi aprovado.')
