# Escreva um programa que peça ao usuário para digitar um número inteiro positivo e, 
# em seguida, exiba todos os números ímpares de 1 até esse número.

Num = int(input('Digite um número inteiro a sua escolha: '))
for n in range(1, Num+1):
  if (n%2 != 0):
    print(n)
