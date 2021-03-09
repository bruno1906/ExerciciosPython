from datetime import date
atual=date.today().year
somamaior=0
somamenor=0
for c in range(1,7):
    idades=int(input('Em que ano a {} pessoa nasceu?'.format(c)))
    idade=atual-idades
    print('A pessoa tem {} anos'.format(idade))
    if idade>=18:
        somamaior=somamaior+1
    else:
        somamenor=somamenor+1
print('Ao todo tivemos {} pessoas maiores de idade'.format(somamaior))
print('E tambem tivemos {} pessoas menores de idade'.format(somamenor))




