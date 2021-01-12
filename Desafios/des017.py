'''
co = float(input('Digite o comprimento do cateto oposto:'))
ca = float(input('Digite o comprimento do cateto adjacente:'))
hip = (ca**2 + co**2)**(1/2)
print('A hipotenusa ira medir {}.'.format(hip))
'''
'''
import math
co = float(input('Digite o comprimento do cateto oposto:'))
ca = float(input('Digite o comprimento do cateto adjacente:'))
hip = math.hypot(ca,co)
print('A hipotenusa ira medir {}.'.format(hip))
'''
'''
from math import hypot
co = float(input('Digite o comprimento do cateto oposto:'))
ca = float(input('Digite o comprimento do cateto adjacente:'))
hip = hypot(ca,co)
print('A hipotenusa ira medir {}.'.format(hip))
'''
from math import hypot
co = float(input('Digite o comprimento do cateto oposto:'))
ca = float(input('Digite o comprimento do cateto adjacente:'))
print('A hipotenusa ira medir {}.'.format(hypot(ca, co)))
