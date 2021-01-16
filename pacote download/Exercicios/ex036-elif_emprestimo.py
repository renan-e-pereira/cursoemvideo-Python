''' CORRIGIDO
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''
from time import sleep
print('-=-'*7)
print('Empréstimo bancário')
print('-=-'*7)
casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual o seu salário? '))
tempo = float(input('Em quantos anos deseja pagar? '))
print('Processando...')
sleep(1)
prestacao = casa / (tempo*12)
print('Prestação: R$ {:.2f}'.format(prestacao))
if prestacao < .30 * salario:
    print('Parabéns, o seu empréstimo foi aceito!')
elif prestacao > .30 * salario:
    print('Lamento, mas o seu empréstimo foi recusado.')
else:
    print('Erro!')