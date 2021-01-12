salario = float(input('Qual o sálario do funcionário? '))
if salario <= 1250:
    novosal = salario + (salario * 15 / 100)
else:
    novosal = salario + (salario * 10 / 100)
print('O novo salario será de R${:.2f}'.format(novosal))