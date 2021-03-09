n=c=s=0
while True:
    n=int(input('Digite um numero: (999 para parar)'))
    if n==999:
        break
    s=s+n
    c=c+1
print('A soma dos {} valores digitados foi {}.'.format(c,s,end))
