# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

int_a = int(input('Insira um número inteiro: \n'))
int_b = int(input('Insira outro número inteiro: \n'))
real = float(input('Agora insira um número real: \n'))

print('----------------------------------------------------------------')
print('----------------------------------------------------------------')

# o produto do dobro do primeiro com metade do segundo .
a = (int_a * 2) * (int_b / 2)
print('- O produto do dobro do primeiro com metade do segundo é:')
print(a);

# a soma do triplo do primeiro com o terceiro.
b = (int_a * 3) + real
print('- A soma do triplo do primeiro com o terceiro é:')
print(b);

# o terceiro elevado ao cubo.
c = real ** 3
print('- O terceiro elevado ao cubo é:')
print(c)

