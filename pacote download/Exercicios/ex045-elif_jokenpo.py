from random import randint
from time import sleep
print('=' * 5 + ' Vamos jogar Jokenpô ! ' + '=' * 5)
pc = randint(1, 3)
esc = int(input('[1] - Pedra\n'
                '[2] - Papel\n'
                '[3] - Tesoura\n'
                'Escolha: '))
if pc == 1:
    pc = 'Pedra'
elif pc == 2:
    pc = 'Papel'
elif pc == 3:
    pc = 'Tesoura'
if esc == 1:
    esc = 'Pedra'
elif esc == 2:
    esc = 'Papel'
elif esc == 3:
    esc = 'Tesoura'
print('Jokeeenpô...\n')
sleep(1)
print(' Máquina     Usuário\n'
      '  {}  x  {}'.format(pc, esc))
if pc == esc:
    print('Empate!')
elif pc == 'Pedra' and esc == 'Papel':
    print('Você venceu !')
elif pc == 'Papel' and esc == 'Tesoura':
    print('Você venceu !')
elif pc == 'Tesoura' and esc == 'Pedra':
    print('Você venceu !')
else:
    print('Você perdeu, tente novamente!')

