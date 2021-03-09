import random

n1=str(input('Primeiro aluno:'))
n2=str(input('Segundo alunp:'))
n3=str(input('TErceiro aluno:'))
n4=str(input('Quarto aluno:'))
l=[n1, n2, n3, n4]
random.shuffle(l)
print('A ordem de apresentação será {}!'.format(l))


