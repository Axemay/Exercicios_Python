# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo

from math import cos, sin, tan, radians

angulo = float(input('Insira um ângulo: '))

cosseno = cos(radians(angulo))
seno = sin(radians(angulo))
tangente = tan(radians(angulo))

print('Cosseno: {:.2f}\nSeno: {:.2f}\nTangente: {:.2f}'.format(cosseno, seno, tangente))
