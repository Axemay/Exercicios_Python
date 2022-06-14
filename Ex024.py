# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo"

cidade = str(input('Insira o nome da sua cidade: ')).strip() #strip tira os espaços

print(cidade[:5].upper() == 'SANTO')


