#Faça um programa que receba uma valor em Celsius e converta para Fahenheit

celsius = float(input("Insira o valor da temperatura em Celsius: "))
fahenheit = celsius * 9 / 5 + 32

print('O valor {} em Celsius equivale a {} na escala fahenheit'.format(celsius, fahenheit))
