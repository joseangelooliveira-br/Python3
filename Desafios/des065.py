resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / quant
print('Voce digitou {} numeros, {} é a soma dos mesmos e a média é {:.2f}'.format(quant, soma, media))
print('O maior número foi {} e o menor número foi {}.'.format(maior, menor))
print('ACABOU')