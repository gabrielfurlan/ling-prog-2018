# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
# F = C x 1.8 + 32.

celsius = input('Qual a temperatura em C°? \n')
fahrenheit = int(celsius) * 1.8 + 32

print('Sua temparatura em F° é de ' + str(fahrenheit));
