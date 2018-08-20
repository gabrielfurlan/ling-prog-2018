# Faça um Programa que pergunte quanto você ganha por hora e o
# número de horas trabalhadas no mês. 

hourly_wage = input('Quanto você ganha por hora? \n')
hours_amount = input('Quantas horas você trabalhou no mês? \n')

# Calcule e mostre o total do seu salário no referido mês, 
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% 
# para o INSS e 5% para o sindicato, faça um programa que nos dê:
gross_wage = (float(hours_amount) * float(hours_amount)) 
net_wage = gross_wage * 0.77

income_tax = gross_wage * 0.11
inss = gross_wage * 0.8
syndicate = gross_wage * 0.5; 

# salário bruto.
print('O seu salário bruto no mês é de ' + str(gross_wage) + ' reais');

# quanto pagou ao INSS.
print('Foram descontados de INSS ' + str(inss) + ' reais');

# quanto pagou ao sindicato.
print('Foram descontados de sindicato ' + str(syndicate) + ' reais');

# ######## OBS: não tinha no exercicio o imposto de renda mais estou fazendo e deixando comentado a baixo.
# print('Foram descontados de imposto de renda ' + str(income_tax) + ' reais');

# o salário líquido.
print('O seu salário liquído no mês é de ' + str(net_wage) + ' reais');
