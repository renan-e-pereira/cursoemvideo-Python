'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem de acordo com a média
atingida:
- abaixo de 5.0 = Reprovado
- 5.0 - 6.9 = Recuperação
- 7 e acima = aprovado
'''
from time import sleep
nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
media = (nota1 + nota2) / 2
print('Analisando notas...')
sleep(1)
if media >= 7:
    print('Parbéns, você passou! Com média {}.'.format(media))
elif media < 5:
    print('Você reprovou, boa sorte da próxima vez. Sua média foi {}.'.format(media))
else:
    print('Você está em recuperação. Sua média foi {}.'.format(media))
