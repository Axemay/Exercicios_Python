# Crie um algoritmo que leia um número e moste seu dobro, seu triplo e raiz quadrada.

numero = int(input('Insira um valor: '))
print('Você digitou {} \n O dobro é {} \n O triplo é {} \n A raiz quadrada é {:.2f}'.format(numero, (numero *2), (numero *3), numero**(1/2)))
