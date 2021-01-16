''' O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos 4 alunos e mostrem a ordem sorteada.'''

from random import shuffle
print('Digite o nome dos alunos:')
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print (lista)
