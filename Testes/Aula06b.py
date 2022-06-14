'''
n = float(input('Digite o preço: '))
b = bool(input('Digite o preço: '))
print('O valor {} é do tipo {}, mas o valor {} é do tipo {}'.format(n, type(n), b, type(b)))
'''

p = input('Digite algo: ')

def verificaNumero():
    if p.isnumeric():
        print('{} é um número.'.format(p))

    elif p.isalpha():
        print('{} não é um número. É uma letra.'.format(p))

    elif p.isalnum():
        print('{} é alfanumerico.'.format(p))
    else:
        print('{} é bizarro.'.format(p))

verificaNumero()
