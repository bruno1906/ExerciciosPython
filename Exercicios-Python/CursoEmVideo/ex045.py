import random

print('-*-'*20)
print('PEDRA PAPEL TESOURA')
print('-*-'*20)
jogador=int(input('PEDRA:1\nTESOURA:2\nPAPEL:3\nEscolha PEDRA PAPEL ou TESOURA:'))
p=4
pa=6
t=5
lista=[p,pa,t]
computador=random.choices(lista)

print('A escolha do computador foi {}!'.format(computador))
if jogador==1 and computador==5:
    print('PARABENS,você ganhou!')
elif jogador==3 and computador==4:
    print('PARABENS,você ganhou!')
elif jogador==2 and computador==6:
    print('PARABENS,você ganhou!')
else:
    print('Você perdeu!')
