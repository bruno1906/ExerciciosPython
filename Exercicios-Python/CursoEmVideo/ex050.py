soma=0
cont=0
for c in range(1,7):
    n=int(input('Digite o {} numero:'.format(c)))
    cont=cont+1
    if n%2==0:
        soma=soma+n
print('Você informou {} numeros e a soma dos pares é {}.'.format(cont, soma))



