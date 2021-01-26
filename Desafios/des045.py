from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[0] Pedra.
[1] Papel.
[2] Tesoura.
''')
jogador = int(input('Qual sua jogada: '))
print('-=-'*10)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}.'.format(itens[jogador]))
print('-=-'*10)
if computador == 0:
    if jogador == 0:
        print('empate')
    elif jogador == 1:
        print('jogador ganhou')
    elif jogador == 2:
        print('computador ganhou')
    else:
        print('jogada invalida.')

elif computador == 1:
    if jogador == 0:
        print('computador ganhou')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('jogador ganhou')
    else:
        print('jogada invalida.')

elif computador == 2:
    if jogador == 0:
        print('jogador ganhou')
    elif jogador == 1:
        print('computador ganhou')
    elif jogador == 2:
        print('empate')
    else:
        print('jogada invalida.')