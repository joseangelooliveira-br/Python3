n1 = int(input('Digite o 1º numero: '))
n2 = int(input('Digite o 2º numero: '))
s = n1+n2
m = n1*n2
d = n1/n2
d1 = n1//n2
e = n1**n2
print('A soma é {}, a multiplicação é {} \n e a divisão é {:.3f}.'.format(s,m,d),end='')
print('A divisão inteira é {} e a exponenciação é {}.'.format(d1,e))
