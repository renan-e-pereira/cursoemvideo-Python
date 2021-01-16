''' CORRIGIDO
Desafio:
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu
'''
from random import randint
from time import sleep
n = int(input('Digite um número inteiro de 0 a 5: '))
if (n >=0) and (n <= 5):
    esc = randint(0, 5)
    print('Pensando...')
    sleep(2)
    print('Número escolhido: {}'.format(esc))
    if n == esc:
        print('Você venceu!')
    else:
        print('Você perdeu, tente novamente.')
else:
    print('Número inválido! Preste atenção às regras e tente novamente.')