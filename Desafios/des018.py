import math
angulo = float(input('Digite um angulo qualquer:'))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print('Para o angulo {} o seno será {:.2f} e o cosseno será {}.'.format(angulo, sen, cos))
print('Para o angelo {} a tangente será de {}.'.format(angulo, tang))

