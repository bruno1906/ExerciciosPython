import random
from time import sleep
c=1
computador = random.randint(0, 10) #Faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei?')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
while computador != jogador:
    jogador=int(input('ERRADO! Tente novamente:'))
    c=c+1
print('ACERTOU!!! Você tentou {} vezes até acertar!'.format(c))
#if jogador==computador:
    #print("PARABENS! Você conseguiu me vencer")
#else:
    #print('GANHEI! Eu pensei no numero {}'.format(computador))