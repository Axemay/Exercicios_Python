# Faça um programa que leia um número inteiro e moste na tela o seu sucessor e seu antecessor

numero = int(input('Insira um valor: '))
print('Você digitou {}. O antecessor é {}, e o sucessor é {}.'.format(numero, (numero - 1), (numero + 1)))
