''' Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo
o nome deles e escrevendo o nome escolhido '''

from random import choice
print('Digite o nome dos alunos:')
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
print ('\nEscolha: {}'.format(choice((a1, a2, a3, a4))))
'''
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print ('\nEscolha: {}'.format(escolhido))
'''
