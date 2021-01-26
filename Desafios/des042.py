print('-=-'*20)
print('Analizador de Triângulos')
print('-=-'*20)
r1 = float(input('Digite o 1º segmento: '))
r2 = float(input('Digite o 2º segmento: '))
r3 = float(input('Digite o 3º segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(' Os segmentos {}, {} e {} formam um triangulo.'.format(r1, r2, r3))
    if r1 == r2 == r3:
        print('Equilatero.')
    elif r1 != r2 != r3 != r1:
        print('Escaleno.')
    else:
        print('Esoceles.')
else:
    print(' Os segmentos {}, {} e {} não formam um triangulo.'.format(r1, r2, r3))
