# Faça um programa que leia 15 valores e no
# final, escreva o maior e o menor valor lido.

maior = 0
menor = 0

for i in range(15): # Códificando com o For
  valor = int(input('Insira o valor: '))
  if i == 0:
    menor = valor
    maior = valor
  if valor < menor:
    menor = valor
  if valor > maior:
    maior = valor

print('________Resultado________')

print('Maior: ', maior)
print('Menor: ', menor)