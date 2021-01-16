'''
A Confederação Nacional de Natação precisa de um programa que leia o ano
de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: Mirim;
- Até 14 anos: Infantil;
- Até 19 anos: Junior;
- Até 20 anos: Sênior;
- Acima: Master.
'''
from datetime import date
ano = int(input('Em que ano você nasceu: '))
idade = date.today().year - ano
if idade <= 9:
    categoria = 'Mirim'
elif idade <= 14:
    categoria = 'Infantil'
elif idade <= 19:
    categoria = 'Junior'
elif idade <= 20:
    categoria = 'Sênior'
elif idade > 20:
    categoria = 'Master'
print('Você tem {} anos e sua categoria é a {}.'.format(idade, categoria))
