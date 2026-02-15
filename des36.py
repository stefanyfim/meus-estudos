casa= int(input('Valor da casa: R$'))
salario= int (input('Salario do comprador: R$'))
anos= int (input('Quantos anos de financiamento? '))
prestacao= casa/ (anos*12)
minimo= salario*30 /100

print ('Para pagar uma casa de R${} em {} anos.'.format(casa,anos),end='')
print ('a prestação será de R${}'.format(prestacao))

if prestacao<= minimo:
    print ('Empréstimo pode ser CONCEDIDO!')
else:
    print ('Empréstimo NEGADO!')