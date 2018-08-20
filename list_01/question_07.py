# João Papo-de-Pescador, homem de bem, comprou um
# microcomputador para controlar o rendimento diário de seu
# trabalho. Toda vez que ele traz um peso de peixes maior que o
# estabelecido pelo regulamento de pesca do estado de São Paulo (50
# quilos8 deve pagar uma multa de R$ 4,00 por quilo excedente. João
# precisa que você faça um programa que leia a variável peso (peso
# de peixes8 e verifque se há excesso. Se houver, gravar na variável
# excesso e na variável multa o valor da multa que João deverá pagar.
# Caso contrário mostrar tais variáveis com o conteúdo ZERO.

import math 

kilos = int(input('Quantos quilos de peixes: \n'))

print('--------------------------------------------')
print('--------------------------------------------')

excess = int(math.fabs(50 - kilos)) if kilos > 50 else 0
print('Excedeu: ' + str(excess)) 

fine_amount = math.fabs(50 - kilos) * 4.0 if kilos > 50 else 0.0
print('Sua multa é de: ' + str(fine_amount))

print('--------------------------------------------')
print('--------------------------------------------')
