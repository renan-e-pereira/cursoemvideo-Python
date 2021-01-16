''' CORRIGIDO
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite.
'''
v = int(input('Velcidade do veículo (km/h): '))
if v > 80:
    print('Velocidade acima!\nMulta: R${:.2f}'.format((v-80)*7))
else:
    print('Velocidade dentro do limite.')