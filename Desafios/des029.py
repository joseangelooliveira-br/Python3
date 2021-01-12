veloc = float(input('Qual é a velocidade atual do carro? '))

if veloc <= 80:
    print('Tenha um bom dia. Dirija com segurança!')
else:
    print('MULTADO ! voce excedeu o limite de 80km/h.\nO valor de sua multa é R${}'.format(((veloc)-80)*7))
print('fim')