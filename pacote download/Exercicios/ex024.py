''' --Corrigido--
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".
'''
cidade = input('Digite o nome de uma cidade: ').strip()
print('Cidade tem a palavra "Santo"? {}'.format(cidade[:5].lower() == 'santo'))