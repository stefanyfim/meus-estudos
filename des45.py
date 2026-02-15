from random import randint

print ('Suas opções: ')
print ('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ]TESOURA''')

jogador= int (input('Qual é a sua jogada?'))
computador= randint(0,2)
print ('''JO
KEN
PO!!!''')

print ('-=-='*4)
if computador==0: print ('Computador jogou PEDRA.')
elif computador==1: print ('Computador jogou PAPEL.')
elif computador==2: print ('Computador jogou TESOURA.')

if jogador==0: print ('Jogador jogou PEDRA.')
elif jogador==1: print ('Jogador jogou PAPEL.')
elif jogador==2: print ('Jogador jogou TESOURA.')

else:
    print ('O jogo empatou TENTE NOVAMENTE.')
print ('-=-='*4)

if jogador==0 and computador==2 or jogador==1 and computador==0 or jogador==2 and computador==1:
    print ('JOGADOR VENCE!! Meus parabéns.')
else:
    print ('O COMPUTADOR VENCEU :( Tente novamente!')