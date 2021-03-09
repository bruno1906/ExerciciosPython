sexo = str(input('Qual seu sexo? [M/F]')).strip().upper()[0]
while sexo not in 'MF':
    sexo=str(input('Resposta invalida,digite novamente:')).strip().upper()[0]
print('Resposta valida')
