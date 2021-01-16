'''CORRIGIDO
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A";                        (x)
- Em que posição ela aparece pela primeira vez;             (x)
- Em que posição ela aparece pela última vez.               (x)
'''

a = input('Digite uma frase: ').strip().lower()
print('Há {} "A"(s) na frase'.format(a.count('a')))
print('1º "A" na posição {}'.format(a.find('a')+1))
print('Último "A" na posição {}'.format(a.rfind('a')+1))
