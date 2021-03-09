print('-*'*30)
print('Sequência de Fibonacci')
print('-*'*30)
t=int(input('Quantos termos você quer mostrar?'))
t1=0
t2=1
print('{} - {}'.format(t1,t2),end='')
c=3
while c<=t:
    t3=t1+t2
    print('- {}'.format(t3), end='')
    t1=t2
    t2=t3
    c=c+1