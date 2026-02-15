num1= float(input('Primeira nota: '))
num2= float(input('Segunda nota: '))
media= (num1+num2)//2

if media <=5 and media<7:
    print ('O aluno está em RECUPERAÇÃ0.')
elif media>=7:
    print ('O aluno está APROVADO!!')
elif media <5 :
    print ('O aluno está REPROVADO! Tente novamente')
 


print ('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format (num1, num2, media))