# Escreva um algoritmo que leia 3 números inteiros e mostre o maior deles.

# _____________________________________ #
Num1 = int(input('Digite o valor 1: '))
Num2 = int(input('Digite o valor 2: '))
Num3 = int(input('Digite o valor 3: '))
# _____________________________________ #

# _____________________________________ #
if Num1 > Num2 > Num3:
    print('A order é', Num1, Num2, Num3)
if Num1 > Num3 > Num2:
    print('A order é', Num1, Num3, Num2)
if Num2 > Num1 > Num3:
    print('A order é', Num2, Num1, Num3)
if Num2 > Num3 > Num1:
    print('A order é', Num2, Num3, Num1)
if Num3 > Num1 > Num2:
    print('A order é', Num3, Num1, Num2)
if Num3 > Num2> Num1:
    print('A order é', Num3, Num2, Num1)
# _____________________________________ #