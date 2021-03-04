frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print('\033[32mVocê digitou a frase:\033[m {}.'.format(frase))
print('\033[32mVocê digitou a frase:\033[m {}.'.format(palavras))
print('\033[32mVocê digitou a frase:\033[m {}.'.format(junto))
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso +=junto[letra]
print(junto)
print(inverso)
if junto == inverso:
    print('A frase é um PALINDROMO.')
else:
    print(junto, inverso, 'Não é um PALINDROMO.')
