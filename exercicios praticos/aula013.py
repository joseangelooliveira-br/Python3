'''
for c in range(0,5):
    print('Oi')
print('fim')
'''
'''
for c in range(0, 6):
    print(c)
print('fim')
print(c)
'''
'''
for c in range(0, 11, 2):
    print(c)
print('fim')
'''
'''
for c in range(10, 0, -2):
    print(c)
'''
'''
n = int(input('Digite um número inteiro qualquer: '))
for c in range(0, n+1, 2):
    print(c)
'''
'''
i = int(input('Inicio: '))
f = int(input('fim: '))
p = int(input('passo: '))
for c in range(i, f+1, p):
    print(c)
'''
total = 0
for c in range(0, 4):

    n = float(input('Digite um número qualquer: '))
    total += n
print('A soma será {:.2f}'.format(total))