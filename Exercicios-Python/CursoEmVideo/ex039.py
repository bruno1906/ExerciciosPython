from datetime import date
atual=date.today().year
ano=int(input('Qual sua data de nascimento?'))
sexo=str(input('Você é homem ou mulher?'))

if atual-ano<18:
    print('Vc ainda vai se alistar daqui a {}.'.format(18-(atual-ano)))
elif atual-ano==18:
    print('Você deve se alistar imediatamente!')
elif sexo==('mulher'):
    print('Você não precisa se alistar')
else:
    print('Você deveria ter se alistado a {}.'.format((atual-ano)-18))
