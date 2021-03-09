p=int(input('Digite o primeiro termo:'))
r=int(input('Digite a razão:'))
c=1
termo=p
total=0
mais=10
while mais != 0:
    total=total+mais
    while c<=total:
        print('{} - '.format(termo),end='')
        termo=termo+r
        c=c+1
    print('PAUSA')
    mais=int(input('Quantos termos você quer mostrar a mais?'))
print('Progressão finalizada com {} termos mostrados.'.format(total))