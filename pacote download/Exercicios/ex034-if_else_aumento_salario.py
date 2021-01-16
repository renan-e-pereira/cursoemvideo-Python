''' CORRIGIDO
Escreva um program que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento pe de 15%.
'''
from time import sleep
s = float(input('Salário: R$ '))
print('Calculando aumento...')
sleep(1)
if (s > 0) and (s > 1250):
    sa = s * 1.10
    print('Salário atualizado: R${:.2f}'.format(sa))
else:
    if (s > 0) and (s <= 1250):
        sa = s * 1.15
        print('Salário atualizado: R${:.2f}'.format(sa))
    else:
        print('Valor inválido!')