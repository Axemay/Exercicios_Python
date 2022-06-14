# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
# Ex.: Digite um número: 6.127
# O número 6.127 tema parte inteira 6


import math

numero = float(input('Digite um número Real: '))
parteInteira = math.floor(numero)

print('O número {} tem a parte inteira {}.'.format(numero, parteInteira))
