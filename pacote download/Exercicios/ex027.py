''' CORRIGIDO
Faça um programa que leia o nome completo de uma pessoa e mostre o primeiro e último nome separadamente
Ex: Ana Maria de Souza
Primeiro: Ana
Último: Souza
'''
nome = input('Digite um nome: ').strip()
print('Nome: {}'.format(nome).title())
nome = nome.split()
print('Primeiro nome: {}'.format(nome[0].title()))
print('Último nome: {}'.format(nome[len(nome)-1].title()))
