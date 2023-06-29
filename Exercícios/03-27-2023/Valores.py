
# Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é
# menor que C.

# __________________________________________________________________________ #

A = float(input("Insira o primeiro valor: "))
B = float(input("Insira o segundo valor: "))
C = float(input("Insira o terceiro valor: "))

Soma = A + B
print("Sua soma é: ", Soma)
print('')

if Soma < C:
  print("Então a sua soma é menor que o 3º valor !")
else:
  print("Então a sua soma foi maior que o 3º valor !")
# ____________________________________________________#