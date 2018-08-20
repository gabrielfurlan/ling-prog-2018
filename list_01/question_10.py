
# Faça um programa que permita ao usuário digitar o seu nome e
# em seguida mostre o nome do usuário de trás para frente utilizandosomente letras maiúsculas. Dica: lembre−se que ao informar o
# nome o usuário pode digitar letras maiúsculas ou minúsculas.
# Observação: não use loops.


name = input('Informe seu nome: \n')

def invert(name, current = 0, inverted_name = ''): 
	if current == len(name):
		return inverted_name;

	index = len(name) - current - 1
	inverted_name = inverted_name + name[index]
	return invert(name, current + 1, inverted_name) 

print('----------------------------------------------')
print('----------------------------------------------')

print('Seu nome invertido é:')
print(invert(name))
