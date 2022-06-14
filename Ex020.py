#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos
# Faça um program aque leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

alunoUm = input('Primeiro Aluno: ')
alunoDois = input('Segundo Aluno: ')
alunoTres = input('Terceiro Aluno: ')
alunoQuatro = input('Quarto Aluno: ')
lista = ''
listaAlunos = [alunoUm, alunoDois, alunoTres, alunoQuatro]

shuffle(listaAlunos)

print(f'A ordem de apresentação será: {listaAlunos[0]}, {listaAlunos[1]}, {listaAlunos[2]} e {listaAlunos[3]}')

