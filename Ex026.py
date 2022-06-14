# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez


frase = str(input('Escreva uma frase: ')).lower().strip()

vezes = frase.count('a')
p_posicao = frase.find('a') + 1
u_posicao = frase.rfind('a') + 1

print(f'A letra A aparece {vezes} vezes')
print(f'O primeiro A aparece na posição: {p_posicao}')
print(f'A letra A aparece pela última vez na posição: {u_posicao}')

#A letra A é A mais bonita
