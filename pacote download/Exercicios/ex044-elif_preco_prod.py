'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''
preco = float(input('Preço do produto: R$ '))
escolha = int(input('[1] - À vista em dinheiro / cheque\n'
                    '[2] - À vista no cartão\n'
                    '[3] - Até 2x no cartão\n'
                    '[4] - 3x ou mais no cartão\n'
                    'Escolha: '))
if escolha == 1:
    print('Parabéns! você ganhou um desconto de 10%.\nPreço final: R$ {:.2f}'.format(preco * .9))
elif escolha == 2:
    print('Parabés! Você ganhou um desconto de 5%.\nPreço final: R$ {:.2f}'.format(preco * .95))
elif escolha == 3:
    print('Obrigado por comprar conosco!\nPreço final: R$ {:.2f}'.format(preco))
elif escolha == 4:
    print('3x ou mais no cartão cobramos uma taxa de 20%\nPreço final: R$ {:.2f}'.format(preco * 1.2))
