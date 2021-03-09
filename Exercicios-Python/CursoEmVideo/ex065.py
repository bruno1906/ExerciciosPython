n =0
s=0
c=0
o= 'S'
while o in 'S':
    n = int(input('Digite um numero:'))
    s=s+n
    c=c+1
    if c==1:
        maior=menor=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n
    o=str(input('Quer continuar?[S/N]').upper())
print('A media entre os {} valores digitados foi {}'.format(c,(s/c)))
print('O maior valor foi {} e o menor foi {}'.format(maior,menor))




