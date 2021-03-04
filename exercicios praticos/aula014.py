'''
for c in range (1, 10):
    print(c)
print('FIM')
'''
'''
c = 1
while c < 10:
    print(c +1)
    c += 1
print('FIM')
'''
'''
n = 1
while n != 0:
    n = int(input('Digite um valor inteiro diferente de 0: '))
print('FIM')
'''
'''
n = 0
r = 'S'
while r == 'S':
    n = int(input('Digite um Valor: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('FIM')
'''
n = 1
par = 0
impar = 0
tot = 0
while n != 0:
    n = int(input('Digite um valor inteiro: '))

    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
        tot = par + impar
print('De um total de {} numeros, {} são pares e {} são impares'.format(tot, par, impar))
print('Acabou')
