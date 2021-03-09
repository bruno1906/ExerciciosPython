n1=int(input('Digite um valor:'))
n2=int(input('Digite outro valor:'))
r=int(input('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]sair do programa\nOque você deseja fazer:'))
while r!=5:
    if r==1:
        print(n1+n2)
        r=int(input('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]sair do programa\nOque você deseja fazer:'))
    if r==2:
        print(n1*n2)
        r = int(input('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]sair do programa\nOque você deseja fazer:'))
    if r==3:
        if n1>n2:
            print('{} é o maior numero.'.format(n1))
        else:
            print('{} é o maior numero.'.format(n2))
        r = int(input('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]sair do programa\nOque você deseja fazer:'))
    if r==4:
        n1 = int(input('Digite um valor:'))
        n2 = int(input('Digite outro valor:'))
        r = int(input('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]sair do programa\nOque você deseja fazer:'))

