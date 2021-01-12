frase = str(input('Digite um frase: ')).strip().lower()
print('A letra "A" aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira letra "A" aparece na posição {} da frase.'.format(frase.find('a')+1))
print('A ultima letra "A" aparece na posição {} da frase.'.format(frase.rfind('a')+1))