p=int(input('Digite o primeiro termo:'))
r=int(input('Digite a razão:'))
c=1
termo=p
while c<=10:
    print('{} - '.format(termo),end='')
    termo=termo+r
    c=c+1
print('FIM')





#for c in range(1,11):
    #print(p+(c-1)*r)