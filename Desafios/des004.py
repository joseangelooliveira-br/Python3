print('{} Desafio 004 {}'.format(10*'=',10*'='))
nome = input('Digite Algo :')
print('Tipo primitivo de "{}". É {}'.format(nome,type(nome)))
print('Somente tem espaços?',nome.isspace())
print('É um numero?',nome.isnumeric())
print('É um alfabeto?',nome.isalpha())
print('É alfanumerico?',nome.isalnum())
print('esta em minuscalas?',nome.islower())
print('Está em amiusculas?',nome.isupper())
print('esta capitulada?',nome.istitle())



