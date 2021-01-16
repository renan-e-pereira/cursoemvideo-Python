''' --Corrigido--
Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
'''
nome = input('Digite um nome: ').strip()
print('Tem "Silva" no nome? {}'.format('Silva' in nome.lower()))
