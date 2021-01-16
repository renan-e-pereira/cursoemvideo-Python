'''
Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
Equilátero: todos os lados iguais
Isóceles: dois lados iguai
Escaleno: todos os lados diferentes
'''
n1 = float(input('Reta 1: '))
n2 = float(input('Reta 2: '))
n3 = float(input('Reta 3: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 +n2:
    if n1 == n2 == n3:
        tipo = 'Equilátero'
    elif n1 != n2 != n3:
        tipo = 'Escaleno'
    else:
        tipo = 'Isóceles'
    print('É possível formar um triângulo {} com esses valores!'.format(tipo))
else:
    print('Valores inválidos para triângulo.')