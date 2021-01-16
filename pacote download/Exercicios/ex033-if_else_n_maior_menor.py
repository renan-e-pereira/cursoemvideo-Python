''' CORRIGIDO
Faça um programa que leia três números e mostre qual é o maior e qual é o menor
'''
from time import sleep
n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
n3 = float(input('Digite o 3º número: '))
print('Verificando números...')
sleep(1)
if n1 == n2 == n3:
    print('Todos os números são iguais a {}.'.format(n1))
if n2 >= n3 >= n1:
    print('Menor: {}\nMaior: {}'.format(n1, n2))
else:
    if n3 >= n2 >= n1:
        print('Menor: {}\nMaior: {}'.format(n1, n3))
    else:
        if n1 >= n3 >= n2:
            print('Menor: {}\nMaior: {}'.format(n2, n1))
        else:
            if n3 >= n1 >= n2:
                print('Menor: {}\nMaior: {}'.format(n2, n3))
            else:
                if n1 >= n2 >= n3:
                    print('Menor: {}\nMaior: {}'.format(n3, n1))
                else:
                    if n2 >= n1 >= n3:
                        print('Menor: {}\nMaior: {}'.format(n3, n2))