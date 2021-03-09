#n=input('Digite seu nome completo:')
#d=n.split()
#r1=d[0]
#r2=d[2]
#print('Primeiro nome é {}'.format(r1))
#Essa tinha sido minha soluçao

n=str(input('Digite seu nome completo:')).strip()
nome=n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))
