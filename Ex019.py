# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

import random

AlunoUm = input('Primeiro aluno: ')
AlunoDois = input('Segundo aluno: ')
AlunoTres = input('Terceiro aluno: ')
AlunoQuatro = input('Quarto aluno: ')

alunos = [AlunoUm, AlunoDois, AlunoTres, AlunoQuatro]

sorteado = random.choice(alunos)

print('O aluno escolhido foi {}.'.format(sorteado))
