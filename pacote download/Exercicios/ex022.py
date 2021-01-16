''' --Corrigido--
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas;x
- O nome com todas minúsculas;x
- Quantas letras ao total (sem considerar espaços);?
- Quantas letras tem o primeiro nome.x
'''
nome = input('Digite o seu nome completo: ').strip()
print('\nAnalisando nome: {}...\n'.format(nome))
print('Nome em letras maiúsculas: {}'.format(nome.upper()))
print('Nome em letras minúsculas: {}'.format(nome.lower()))
print('Quantidade de letras no nome: {}'.format((len(nome) - nome.count(' '))))
dividido = (nome.split())
print('Quantidade de letras no primeiro nome: {}'.format(len(dividido[0])))
