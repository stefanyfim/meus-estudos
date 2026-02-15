n1= int(input ('Leia o primeiro número: '))
n2= int(input ('Leia o segundo número: '))

if n1 > n2:
    print ('O {} é o maior valor'.format(n1))
elif n2 > n1:
    print ('O {} é o maior valor'.format(n2))
elif n1==n2:
    print ('Não existe valor maior, os dois são iguais')