'''
    Faça um programa que leia um ângulo qualquer e mostre na tela o valor do sena, cosseno e tangente desse ângulo.
'''

from math import sin, cos, tan, radians
ang = float(input('Digite um ângulo qualquer: '))
print('\nÂngulo: {}º\n\nSeno: {:.2f}º\nCosseno: {:.2f}º\nTangente: {:.2f}º'
      .format(ang, sin(radians(ang)),cos(radians(ang)), tan(radians(ang))))
