'''
km = int(input('Digite a distancia de sua viagem em quilometros: '))
if km <= 200:
    print('Voce pagara R$ {} por sua passagem.'.format(km*.50))
else:
    print('Voce pagara R$ {} por sua passagem.'.format(km * .45))

print('Você esta proximo de iniciar um viajem de {} km.'.format(km))
'''

km = int(input('Digite a distancia de sua viagem em quilometros: '))
print('Você esta proximo de iniciar um viajem de {} km.'.format(km))
if km <= 200:
    preco = km * .50
else:
    preco = km * .45
print('Voce pagara R$ {} por sua passagem.'.format(preco))
