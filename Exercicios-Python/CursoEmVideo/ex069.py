contadorh=0
contadorih=0
contadorim=0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    i=int(input('Idade:'))
    s=str(input('Sexo: [M/F] ')).upper().strip()[0]
    print('-'*20)
    r=str(input('Quer continuar? [S/N]')).upper().strip()[0]
    print('-'*20)
    if s=='M':
        contadorh=contadorh+1
    if i>18:
        contadorih=contadorih+1
    if i<20 and s=='M':
        contadorim=contadorim+1
    if r=='N':
        break
print('Total de pessoas com mais de 18 anos: {}'.format(contadorih))
print('Foram cadastrados um total de {} homens'.format(contadorh))
print('E temos {} mulheres com menos de 20 anos'.format(contadorim))
