soma = 0
cont = 0
somat = 0
contt = 0
for c in range(1, 7):
   num = int(input('Digite o {}º valor: '.format(c)))
   somat += num
   contt += 1
   if num % 2 == 0:
        soma += num
        cont += 1
print("voce digitou {} números e a soma deles é {}.".format(contt, somat))
print('Voce digitou {} números pares e a soma deles é {}.'.format(cont, soma))
