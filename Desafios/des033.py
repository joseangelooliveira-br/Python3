a = int(input('Digite 1º numero inteiro: '))
b = int(input('Digite 2º numero inteiro: '))
c = int(input('Digite 3º numero inteiro: '))
#verificando o menor numero digitado
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor =c
# verificando o maior numero digitado
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior =c
print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))