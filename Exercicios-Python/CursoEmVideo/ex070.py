print('-'*20)
print('Loja super baratão'.upper())
print('-'*20)
sp=0
cp=0
menor=0
c=0
barato=''
while True:
    nome=str(input('Nome do Produto: '))
    preço=float(input('Preço: R$'))
    c=c+1
    sp=sp+preço
    r=str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if preço>1000:
        cp=cp+1
    if c==1:
        menor = preço
        barato=nome
    else:
        if preço < menor:
            menor=preço
            barato=nome
    if r=='N':
        break
print('O total da compra foi R${}'.format(sp))
print('Temos {} produtos custando mais de R$1000.00'.format(cp))
print(print('O produto mais barato foi {} que custou R${:.2f}.'.format(barato,menor)))
