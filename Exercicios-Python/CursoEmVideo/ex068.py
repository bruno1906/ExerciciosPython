import random
n=0
c=random.randint(1, 10)
pi=0
s=0
contador=0
print('=-'*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*20)
while True:
    n=int(input('Digite um valor:'))
    pi=str(input('Par ou impar? [P/I]')).upper().strip()[0]
    c = random.randint(1, 10)
    s=n+c
    print('-'*20)
    print('Você jogou {} e o computador {}.Total de {}. '.format(n,c,s),end='')
    contador=contador+1
    if pi == 'P' :
        if s%2==0:
            print('DEU PAR')
            print('-'*20)
            print('Você ganhou!')
            print('Vamos jogar denovo!')
            print('-'*20)
        else:
            print('DEU IMPAR')
            print('-' * 20)
            print('Você perdeu!')
            print('-' * 20)
            print('GAME OVER! Você venceu {}.'.format(contador-1))
            break
    if pi == 'I':
        if s%2==1:
            print('DEU IMPAR')
            print('-' * 20)
            print('Você ganhou!')
            print('Vamos jogar denovo!')
            print('-' * 20)
        else:
            print('DEU PAR')
            print('-' * 20)
            print('Você perdeu!')
            print('-' * 20)
            print('GAME OVER! Você venceu {}.'.format(contador-1))
            break
