v=int(input('Qual era a velocidade do carro?'))
if v>=81:
    print('Vc foi multado!')
    print('Sua multa vai custar R${}'.format((v-80)*7))

else:
    print('Você não foi multado')

