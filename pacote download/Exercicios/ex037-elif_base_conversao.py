'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 - binário
2 - octal
3 - hexadecimal
'''
'''
n = int(input('Número inteiro: '))
escolha = (int(input('Conversor:\n'
                        '1 - Binário\n'
                        '2 - Octal\n'
                        '3 - Hexadecimal\n'
                        'Escolha: ')))
if escolha == 1:
    list.count(n)

    for x in range (len(n)):
        n1 = n / 2
        if n1 % 2 == 0:
            n2 = 0
        elif n % 2 != 0:
            n2 = 1
        print('{}'.format(n2))
if escolha == 2:
    n1 = n // 64
    n2 = n - n1 * 64
    n3 = n2 // 8
    n4 = n2 - n3 * 8
    print('Hexadecimal de {} = {}{}{}'.format(n, n1, n3, n4))
if escolha == 3:
    n1 = n // 16
    n2 = n - n1 * 16
    if n1 == 10:
        n1 = 'A'
    elif n1 == 11:
        n1 = 'B'
    elif n1 == 12:
        n1 = 'C'
    elif n1 == 13:
        n1 = 'D'
    elif n1 == 14:
        n1 = 'E'
    elif n1 == 15:
        n1 = 'F'
    print('{}{}'.format(n1, n2))'''
a = int(input('N: '))
print('Octal: {}\n'
      'Binary: {}\n'
      'Hexadecimal: {}'.format(oct(a), bin(a), hex(a)))
