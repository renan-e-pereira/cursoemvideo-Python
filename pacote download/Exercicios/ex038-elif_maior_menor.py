'''
Escreva um program que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe maior, os dois são iguais
'''
cores = {'limpa': '\033[m',
        'verde': '\033[32m',
        'azul': '\033[34m',
         'amarelo': '\033[33m'}
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
if n1 > n2:
    print('O {}primeiro{} valor é {}maior{}.'
          .format(cores['verde'], cores['limpa'], cores['azul'], cores['limpa']))
elif n2 > n1:
    print('O {}segundo{} valor é {}maior{}.'
          .format(cores['amarelo'], cores['limpa'], cores['azul'], cores['limpa']))
elif n1 == n2:
    print('Não existe valor {}maior{}, ambos são {}iguais{}.'
          .format(cores['azul'], cores['limpa'], cores['amarelo'], cores['limpa']))
else:
    print('Erro!')