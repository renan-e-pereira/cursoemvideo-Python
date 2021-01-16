''' CORRIGIDO
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
'''
from time import sleep
d = float(input('Distância (Km): '))
print('Calculando passagem..')
sleep(1)
if (d > 0) and (d <= 200):
    print('Preço: R${:.2f}'.format(d*0.5))
else:
    if (d > 0) and (d > 200):
        print('Preço: R${:.2f}'.format(d*0.45))
    else:
        print('Distância zero ou negativa.')