a = int(input('Primeiro numero:'))
b = int(input('Segundo numero:'))
c = int(input('Terceiro numero:'))
# VErificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando qual o maior
maior = b
if a > b and a > c:
    maior = a
if c > a and c > b:
    maior = c
print('O menor numero é {}.'.format(menor))
print('O maior numero é {}.'.format(maior))
