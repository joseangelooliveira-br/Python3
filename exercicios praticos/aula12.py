nome = str(input('Digite seu nome: ')).strip()
if nome.lower() == "angelo":
    print('Que nome Lindo!')
elif nome.lower() == 'pedro' or nome.lower() == 'joão' or nome.lower() == 'jose' or nome.lower() == 'antonio':
    print('{} é um nome mascúlino comum no Brasil.'.format(nome))
elif nome.lower() in 'ana maria joana bete':
    print('{} é um nome feminino comum no Brasil.'.format(nome))
else:
    print('{} não é um nome comum.'.format(nome))
print('Bom dia, {}!'.format(nome))