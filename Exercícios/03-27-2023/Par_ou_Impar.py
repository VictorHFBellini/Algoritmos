# Faça um algoritmo para receber um número qualquer e informar na tela se é par ou
# ímpar.

Num = int(input('Digite um Número: '))
restoDiv = Num % 2 # Usa-se para pegar a sobra da divisão #


if restoDiv == 0:
  print('Esse número é Par: ', Num)
else:
  print('Esse número é Impar; ', Num)