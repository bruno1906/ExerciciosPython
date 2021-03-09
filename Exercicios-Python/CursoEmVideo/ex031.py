km=int(input('Quantos Km terá a sua viagem?'))
if km<=200:
    n=km*0.5
    print('Sua viagem vai custar {}!'.format(n))
else:
    h=km*0.45
    print('Sua viagem vai custar {}!'.format(h))

