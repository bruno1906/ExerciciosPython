print('Quantos litros de tinta vc precisa para pintar uma parede?')
#Levando em conta que para cada 2 metros quadrados é necessario um litro de tinta
l=float(input('Qual a largura da parede?'))
a=float(input('Qual a altura da parede?'))
ar=l*a
t=ar/2
print('Para pintar essa parede vc vai precisar de {} litros de tinta!'.format(t))

