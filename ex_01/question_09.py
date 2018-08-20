# Faça um programa que leia 2 strings e informe o conteúdo delas
# seguido do seu comprimento. Informe também se as duas strings
# possuem o mesmo comprimento e são iguais ou diferentes no
# conteúdo.

phrase_a = input('Escreva uma frase:\n')
phrase_b = input('Escreva outra frase:\n')

length_a = len(phrase_a) 
length_b = len(phrase_b) 

print('-----------------------------------')
print('-----------------------------------')

#Exemplo:

#String 1: Brasil Hexa 2018
print('String 1: ' + phrase_a)

#String 2: Brasil! Hexa 2018!
print('String 2: ' + phrase_b)

#Tamanho de "Brasil Hexa 2018": 16 caracteres
print('Tamanho de ' + phrase_a + ': ' + str(length_a) + ' caracteres')

# Tamanho de "Brasil! Hexa 2018!": 18 caracteres
print('Tamanho de ' + phrase_b + ': ' + str(length_b) + ' caracteres')

# As duas strings são de tamanhos diferentes.
if length_a == length_b:
	print('As duas strings são de tamanhos iguais')
else:
	print('As duas strings são de tamanhos diferentes.')

# As duas strings possuem conteúdo diferente.
if(phrase_a == phrase_b):
	print('As duas strings possuem conteúdo iguais.')
else:
	print('As duas strings possuem conteúdo diferente.')

