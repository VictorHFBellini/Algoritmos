# Escreva um programa que simule o jogo da "adivinhação" em que o computador escolhe um número aleatório 
# e o usuário tem que tentar adivinhar o número. O programa deve continuar pedindo ao usuário para adivinhar 
# até que ele acerte o número.

import random

adivinhar = random.randint(0, 5)

while True:
  TentarAdivinhar = int(input('Tente adivinhar o número escolhido: '))
  if TentarAdivinhar == adivinhar:
    print('Você acertou a adivinhação !')
    break
  else:
    print('Você errou a adivinhação, tente novamente !')