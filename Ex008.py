# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimímetros

metros = int(input('Insira o valor em metros: '))
km = metros * 0.001
hn = metros * 0.010
dam = metros * 0.100
dm = metros * 10
cm = metros * 100
mm = metros * 1000
print('O valor {} em metros equivale a:\n{} km\n{} hn\n{} dam\n{} dm\n{} cm\n{} mm'.format(metros, km, hn, dam, dm, cm, mm))

