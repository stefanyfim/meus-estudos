from datetime import date
nome= str (input('Qual é o seu nome?'))
ano= float(input('Ano de nascimento: '))
atual= date.today().year
resultado= atual-ano
print ('{} você nasceu em {:.0f}, tem {:.0f} anos em {:.0f}.'.format(nome,ano,resultado,atual),end='')
if resultado==18:
    print (' Você tem que se alistar imediatamente!')
elif resultado>18:
    print (' Você ja deveria ter se alistado.')
elif resultado<18:
    print(' Você ainda não precisa se alisar.')

