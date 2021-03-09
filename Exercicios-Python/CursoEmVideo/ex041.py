from datetime import date
atual=date.today().year
ano=int(input('Em que ano você nasceu?'))
idade=atual-ano
if idade<=9:
    print('Você nasceu em {},tem {} anos e  sua categoria atual é MIRIM.'.format(ano, idade))
elif 9<idade<=14:
    print('Você nasceu em {},tem {} anos e  sua categoria atual é INFANTIL.'.format(ano, idade))
elif 14<idade<=19:
    print('Você nasceu em {},tem {} anos e  sua categoria atual é JUNIOR.'.format(ano, idade))
elif 19<idade<=25:
    print('Você nasceu em {},tem {} anos e  sua categoria atual é SENIOR .'.format(ano, idade))
else:
    print('Você nasceu em {},tem {} e sua categoria atual é MASTER'.format(ano, idade))
