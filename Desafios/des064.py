num = 0
tot = 0
cont = 0
total = 0
num = int(input('Digite um número[para parar digite 999]: '))
while num != 999:
    cont += 1
    tot += num
    num = int(input('Digite um número[para parar digite 999]: '))
print('{} foram deigitados e seu total é {}.'.format(cont, tot))
print('ACABOU')