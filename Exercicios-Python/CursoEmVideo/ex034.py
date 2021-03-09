s=int(input('Qual seu salario?'))
if s>1250:
    p=s*0.1
    ns=s+p
    print('Você recebeu um aumento de {:.2f} e seu novo salaraio é {:.2f}.'.format(p, ns))
else:
    p2=s*0.15
    ns2=s+p2
    print('Você recebeu um aumento de {:.2f} e seu novo salario é {:.2f}.'.format(p2, ns2))

