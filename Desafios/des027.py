n = str(input('digite seu nome Completo:')).strip()
nome = n.split()
print('nome é {}'.format(n))
print('nome é {}'.format(nome))
print('Seu primeiro nome é {}'.format(nome[0]))
print('seu ultimo nome é {}'.format(nome[len(nome)-1]))
print(len(nome))