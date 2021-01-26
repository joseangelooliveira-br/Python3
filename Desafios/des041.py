from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de seu nascimento: '))
idade = atual - nasc
print('O atleta tem {} de idade.'.format(idade))
if idade <= 9:
    print('Classificação Mirim.')
elif idade <= 14:
    print('Classificação Infantil')
elif idade <= 19:
    print('Classificação Junior.')
elif idade <= 25:
    print('classicação Senior.')
elif idade > 25:
    print('Classcificação Master.')
