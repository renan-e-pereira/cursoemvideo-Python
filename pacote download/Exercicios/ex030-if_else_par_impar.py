''' CORRIGIDO
Crie um program que leia um número inteiro e mostre se ele é par ou ímpar
'''
from time import sleep
n = int(input('Digite um número inteiro: '))
print('Verificando se número é par ou ímpar...')
sleep(1)
if n % 2 == 0:
    print('Número é par.')
else:
    print('Número é ímpar.')
