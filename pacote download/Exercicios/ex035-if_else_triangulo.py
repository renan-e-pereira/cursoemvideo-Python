''' CORRIGIDO
Desenvolva um program que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos
outros dois e maior que o valor absoluto da diferença entre essas medidas.
'''
from time import sleep
n1 = float(input('Reta 1: '))
n2 = float(input('Reta 2: '))
n3 = float(input('Reta 3: '))
print('Verificando medidas para triângulo...')
sleep(1)
'''
if n1 == n2 == n3:
    menor = n1
    maior = n2
else:
    if n2 >= n3 >= n1:
        maior = n2
        menor = n1
    else:
        if n3 >= n2 >= n1:
            menor = n1
            maior = n3
        else:
            if n1 >= n3 >= n2:
                menor = n2
                maior = n1
            else:
                if n3 >= n1 >= n2:
                    menor = n2
                    maior = n3
                else:
                    if n1 >= n2 >= n3:
                        menor = n3
                        maior = n1
                    else:
                        if n2 >= n1 >= n3:
                            menor = n3
                            maior = n2

if (n1 < (n2+n3)) and (n1 > (maior - menor)):
    print('É possível formar um triângulo com esses valores!')
else:
    if (n2 < (n1 + n3)) and (n2 > (maior - menor)):
        print('É possível formar um triângulo com esses valores!')
    else:
        if (n3 < (n2 + n1)) and (n3 > (maior - menor)):
            print('É possível formar um triângulo com esses valores!')
        else:
            print('Valores inválidos para triângulo.')
'''
#Modo Guanabara:
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
     print('É possível formar um triângulo com esses valores!')
else:
    print('Valores inválidos para triângulo.')