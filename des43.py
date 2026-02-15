print ('-=-='*7)
senha= int(input ('Digite a senha: '))
print ('-=-='*7)

if senha==220808:
    print ("SENHA CORRETA")
else:
    print ("SENHA INCORRETA")

nome= str(input ('Qual é o seu nome? '))
peso= float(input('Qual é o seu peso? '))
alt= float (input('Qual é a sua altura? '))

imc= peso//(alt**2)

if imc <=18.5:
    print (f'{nome}, Você está abaixo do peso!')
elif imc <=25:
    print (f'{nome},PARABÉNS, Seu peso é ideal!')
elif imc <=30:
    print (f'{nome}, Você está em sobrepeso!')
elif imc <=40:
    print (f'{nome}, Você está em Obesidade!')
else:
    print (f'{nome}, Você está em Obesidade Mórbida.')