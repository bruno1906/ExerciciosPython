casa=float(input('Qual o valor da sua casa? R$'))
salario=float(input('Qual o valor do seu salario? R$'))
anos=int(input('Em quantos anos vc quer pagar sua casa?'))
mensalidade=casa/(anos*12)
psalario=salario*0.3
print('Sua mensalidade é de {:.2f}.'.format(mensalidade))
if mensalidade<psalario:
    print('PARABÉNS,seu emprestimo foi aprovado!')
else:
    print('Que pena, seu emprestimo foi negado!')
