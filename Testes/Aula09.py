frase = "Curso em Video Python"
frase2 = "   Aprenda Python  "


#Fatiamento

print(frase[9::4])
print(len(frase))
print(frase.count('o'))
print(frase.find('Android'))
print('Curso' in frase)

#Transformação
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase2)
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())


#Divisão
print(frase.split()) # Gera uma lista com todas as palavras de uma cadeia de caractere

#Junção
print('-'.join(frase)) # Após o split, faz a junção dos elementos inserindo o separador indicado (-)

