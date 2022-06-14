# Crie um programa que leia um nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
#O nome com todas minúsculas.
# Quantas letras sem considerar espaços
#Quantas letras tem o primeiro nome


nome = str(input('Digite seu nome completo: '))
espaco = nome.count(' ')
qtd_letras = len(nome) - espaco
fim = nome.find(' ')


print('Maiúsculo: ',nome.upper())
print('Minúsculo: ',nome.lower())
print('Quantidade letras sem espaço: ',qtd_letras)
print('Quantidade letras primeiro nome: ',fim)

# Gabarito do curso

# nome = str(input('Digite seu nome completo: ')).strip()
# print('Analisando seu nome...')
# print('Seu nome em maiúsculas é {}.'.format(nome.upper()))
# print('Quantidade letras sem espaço: '.format(len(nome) - nome.count(' ')))
# print('Quantidade letras primeiro nome: '.format(nome.find(' ')))




