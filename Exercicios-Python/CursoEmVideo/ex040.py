print('Calculo de media do aluno')
n1=float(input('Digite a nota do aluno:'))
n2=float(input('Digite a ssegunda nota:'))
media=(n1+n2)/2
if media<5:
    print('REPROVADO!')
elif media>=7:
    print('APROVADO!')
else:
    print('RECUPERAÇÃO!')
