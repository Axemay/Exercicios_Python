# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
# calcule e mostre o comprimento da hipotenusa

from math import hypot

catetoOposto = float(input('Insira o cateto Oposto: '))
catetoAdjacente = float(input('Insira o cateto adjacente: '))

hipotenusa = hypot(catetoOposto, catetoAdjacente)

print('O valor da hipotenusa é: {:.2f}'.format(hipotenusa))
