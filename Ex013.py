# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salarioAntigo = float(input('Insira o valor do salário: R$ '))
novoSalario = salarioAntigo + (salarioAntigo * 0.15)

print('Seu novo salário é R$ {:.2f}'.format(novoSalario))
