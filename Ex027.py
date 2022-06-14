# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome  separadamente
#Ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza


nome = str(input('Insira seu nome completo: ')).strip()
lista = nome.split()
fim = len(lista) - 1

print('Primeiro = ', lista[0])
print('Último = ', lista[fim])
