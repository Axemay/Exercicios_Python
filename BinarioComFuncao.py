numeroDecimal = int(input('Insira um número decimal: '))
listaBinario = []
numeroBinario = ''


def converteBinario(numeroDecimal, numeroBinario):
    numeroIndicado = numeroDecimal
    while numeroDecimal > 0:
        restoDivisao = numeroDecimal % 2
        listaBinario.append(restoDivisao)
        numeroDecimal = numeroDecimal // 2


    for i in range(len(listaBinario)):

        numeroBinario += str(listaBinario.pop())


    print('O número binário equivalente ao decimal {} é {}.'.format(numeroIndicado, numeroBinario))

if numeroDecimal > 0:
    converteBinario(numeroDecimal, numeroBinario)

else:
    while numeroDecimal <= 0:
        numeroDecimal = int(input('Você precisa indicar um número positivo maior que zero: '))


    converteBinario(numeroDecimal, numeroBinario)


