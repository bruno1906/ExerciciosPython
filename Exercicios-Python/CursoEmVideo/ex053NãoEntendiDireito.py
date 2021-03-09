frase=str(input('Digite uma frase:')).strip().upper()
palavras=frase.split()
junto=''.join(palavras)
inverso=junto[::-1]
#Outra maneira de fazer:
#inverso=''
#for letra in range(len(junto)-1,-1,-1):
    #inverso=inverso+junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso==junto:
    print('Temos um palindromo!')
else:
    print('A frase não é um palindromo')



