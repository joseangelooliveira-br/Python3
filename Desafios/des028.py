from random import randint
from time import sleep
computador = randint(0, 5) #faz um sorteio entre 0 e 5.
print('-=-'*20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('digite um numero entre 0 e 5 :'))
print('PROCESSANDO...')
sleep(2)
if computador == jogador:
    print('Voce ganhou, tambem havia pensado em {}.'.format(computador))
else:
    print('voce pedeu pois eu havia pensado em {}.'.format(computador))
print('Vamos continuar jogando?')