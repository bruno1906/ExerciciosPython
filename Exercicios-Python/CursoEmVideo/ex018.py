import math

n=float(input('Digite um numero qualquer:'))
cos=math.cos(math.radians(n))
sen=math.sin(math.radians(n))
tang=math.tan(math.radians(n))
print('O seno,cosseno e tangente de {} são respectivamente {:.3f}, {:.3f}, {:.3f}!'.format(n, sen, cos, tang))

