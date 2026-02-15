print ('{:= ˆ 40}'.format('LOJAS STEFANY"S'))
preço= int(input('Preço das compras: R$'))
print ('FORMAS DE PAGAMENTO:')
print ('''[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

option= int (input('Qual é a sua opção?'))

if option == 4:
    parcela=int (input('Quantas parcelas?'))
    total= preço + (preço*20/100)
    juros=total/parcela
    print ('Sua compra será parcelada em {}x de R${} COM JUROS.'.format(parcela,juros))
elif option==1:
    total= preço - (preço*10/100)
elif option==2:
    total= preço - (preço*5/100)
elif option==3:
    total= preço 

print ('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
