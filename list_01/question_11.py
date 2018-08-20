## Faça um programa que solicite a data de nascimento
## (dd/mm/aaaa8 do usuário e imprima a data com o nome do mês por
## extenso.

## Data de Nascimento: 29/10/1973
birthday = input('Data de Nasciment0: ')

## Você nasceu em 29 de Outubro de 1973.
months = [
	'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 
	'Agosto', 'Setembro', 'Outrubro', 'Novembro', 'Dezembro'
]

day = birthday[:2]
month = months[int(birthday[3:5]) - 1]
year = birthday[6:]

print('Você nasceu em ' + day + ' de ' + month + ' de ' + year)

## Obs.: Não use desvio condicional nem loops.

