n=int(input('Quantos dias ficou com o carro?'))
km=float(input('Quantos kilometros foram percorridos com o carro?'))
pn=n*60
pkm=km*0.15
v=pn+pkm
print('Valor a pagar:R${:.2f}!'.format(v))


