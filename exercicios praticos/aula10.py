'''
nome = str(input('Qual seu nome?'))
if nome == 'Angelo':
    print('Que nome lindo.')
else:
    print('Seu nome é bonito.')
print('Bom dia, {}!'.format(nome))
'''
n1 = float(input('Digite a 1º nota: '))
n2 = float(input('Digite a 2º nota: '))
m = (n1+n2)/2
print('Sua nota média foi {:.2f}.'.format(m))
if m >= 5:
    print('Voce foi aprovado.')
else:
    print('Voce foi reprovado.')