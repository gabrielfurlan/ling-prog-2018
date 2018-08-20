# Leet é uma forma de se escrever o alfabeto latino usando outros
# símbolos em lugar das letras, como números por exemplo. A própria
# palavra leet admite muitas variações, como l33t ou 1337. O uso do
# leet reflete uma subcultura relacionada ao mundo dos jogos de
# computador e internet, sendo muito usada para confundir os
# iniciantes e afrmar-se como parte de um grupo. Pesquise sobre as
# principais formas de traduzir as letras. Depois, faça um programa
# que peça uma texto e transforme-o para a grafa leet speak.
# Desafo: não use loops nem desvios condicionais.

import string
texto = input('Seu texto: ')
print(texto.translate(bytes.maketrans(b'AacCeEhHiIoOsStT', b'44((33##110O5577')))
