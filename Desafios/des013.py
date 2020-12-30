salatual = float(input('Digite o valor de seu salario: R$ '))
aumento = float(input('Digite o valor de aumento: % '))
novosalario = salatual+(salatual*aumento/100)
print('Seu novo salario será de R${:.2f}'.format(novosalario))