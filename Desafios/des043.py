peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura **2)
print('Seu IMC é de {:.1f}.'.format(imc))
if imc < 18.5:
    print('Abaixo do normal.')
elif 18.5 <= imc < 25:
    print('Peso normal.')
elif 25 <= imc < 30:
    print('Sobrepeso.')
elif 30 <= imc < 40:
    print('Peso Obeso.')
elif imc >= 40:
    print('Obesidade morbida.')