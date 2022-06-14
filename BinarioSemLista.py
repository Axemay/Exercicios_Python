numeroDecimal = int(input('Insira um número decimal: '))
numeroBinario = ''


def converteBinario(numeroDecimal, numeroBinario):
    numeroIndicado = numeroDecimal
    while numeroDecimal > 0:
        restoDivisao = numeroDecimal % 2
        numeroBinario += str(restoDivisao)
        numeroDecimal = numeroDecimal // 2

    print('O número binário equivalente ao decimal {} é {}.'.format(numeroIndicado, numeroBinario[::-1]))

if numeroDecimal > 0:
    converteBinario(numeroDecimal, numeroBinario)

else:
    while numeroDecimal <= 0:
        numeroDecimal = int(input('Você precisa indicar um número positivo maior que zero: '))

    converteBinario(numeroDecimal, numeroBinario)


