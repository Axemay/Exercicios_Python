# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere Us$ 1.00 = 3.27

dinheiro = float(input('Quanto você tem na carteira? R$ '))

print('Com {} você pode comprar U$ {:.2f} dólares.'.format(dinheiro, (dinheiro / 3.27)))
