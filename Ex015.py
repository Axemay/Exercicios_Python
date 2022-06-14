# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e  a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado

dias = int(input('Insira a quantidade de dias de aluguel: '))
kmRodado = float(input('Insira a quantidade de km rodados: '))

valorDias = dias * 60
valorKm = 0.15 * kmRodado
valorTotal = valorDias + valorKm

print('Valor do aluguel: {}\nValor por km rodado: {:.2f}\nTotal a pagar: {:.2f}'.format(valorDias, valorKm, valorTotal))
