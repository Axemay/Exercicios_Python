# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
precoBase = float(input('Insira o preço do produto: R$ '))

novoPreco = precoBase - (precoBase * 0.05)

print('O novo preço é R$ {:.2f}'.format(novoPreco))
