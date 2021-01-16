'''
Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é hora de alistar
- Se já passou do alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou desde de o alistamento
'''
from datetime import date
print('-=-'*8)
print('Verificador de milico')
print('-=-'*8)
ano = int(input('Em qual ano você nasceu? '))
idade = date.today().year - ano
if idade < 18:
    print('Faltam {} anos para se alistar'.format(18 - idade))
elif idade > 18:
    print('Faz {} anos que o alistamento se passou.'.format(idade - 18))
elif idade == 18:
    print('Este ano, deve-se fazer o alistamento.')
