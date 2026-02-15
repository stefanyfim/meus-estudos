nome= str(input('Qual é o seu nome?'))
if nome== 'Stefany':
    print ('Que nome lindo!')

elif nome== 'Pedro' or nome== 'Maria' or nome== 'Paulo':
    print ('Seu nome é popular por aqui')

elif nome in 'Ana Claudia Jéssica Juliana':
    print ('Belo nome feminino')

elif nome in 'Gustavo Jorge João':
    print ('Belo nome masculino')

else:
    print ('Uai nome nada ver tio!')
print ('Tenha um bom dia {}'.format(nome))