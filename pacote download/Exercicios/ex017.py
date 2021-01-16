'''
Questão: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa.
'''

from math import hypot
print('Hipotenusa:\n')
cat_adj = float(input('Cateto Adjacente: '))
cat_op = float(input('Cateto Oposto: '))
hip = hypot(cat_op, cat_adj)

print ('{:.2f} = {}² + {}²'.format(hip, cat_adj, cat_op))
print ('\nHipotenusa: {}'.format(hip))
