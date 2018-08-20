# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * (F - 32) / 9.

fahrenheit = input('Qual a temperatura em F°? \n')
celsius = 5 * ((int(fahrenheit) - 32) / 9)

print('Sua temparatura em C° é de ' + str(celsius));
