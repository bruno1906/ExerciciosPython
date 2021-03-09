import math

co=float(input('Qual o comprimento do cateto oposto?'))
ca=float(input('Qual o comprimento do cateto adjacente?'))
h=math.hypot(ca, co)
print('O valor da hipotenusa é {:.2f}!'.format(h))

