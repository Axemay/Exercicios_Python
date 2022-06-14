# Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua área
# calcule a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

altura = float(input('Insira a altura da parede: '))
largura = float(input('Insira a largura da parede: '))

area = altura * largura

tinta = area / 2

print('Você irá precisar de {:.1f} litros de tinta para pintar a área total de {:.1f}m² da parede'.format(tinta, area))
