valor=float(input('Qual o valor do produto: R$'))
pagamento=float(input('A vista dinheiro/cheque:1\nA vista no cartão:2\nAté 2x no cartão:3\n3x ou mais no cartão:4\nQual a forma de pagamento?'))
p10=valor*0.1
d10=valor-p10
p5=valor*0.05
d5=valor-p5
p20=valor*0.2
a20=valor+p20
if pagamento==1:
    print('Você teve um desconto de {} e seu valor final é de {}'.format(p10, d10))
elif pagamento==2:
    print('Você teve um desconto de {} e seu valor final é {}.'.format(p5, d5))
elif pagamento==4:
    print('Você teve um acrescimo de {} e seu valor final é de {}'.format(p20, a20))
else:
    print('Você pagara {}.'.format(valor))
