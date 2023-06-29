# Crie um algoritmo que leia dois números inteiros e que depois mostre:
#   O primeiro valor vezes o segundo valor
#   A soma do segundo número com a metade do primeiro número
#   A diferença do primeiro número com o segundo
#   O valor negativo do segundo número

# ________________Gambiarra________________ #
Numero1 = int(input("Insira o 1º Número: "))
Numero2 = int(input("Insira o 2º Número: "))
# _________________________________________ #

# ____O primeiro valor vezes o segundo valor____ #
Valor = Numero1 * Numero2
print(Valor)
# ______________________________________________ #

# A soma do 2ºNum com a metade do 1ºNum #
Soma = Numero2 + (Numero1 / 2)
print(Soma)
# ______________________________________________ #

# A diferença do 1ºNum com o 2ºNum #
Diferença = Numero1 - Numero2
print(Diferença)
# ________________________________ #

# O valor negativo do 2ºNum #
Neg_Num2 = -1 * Numero2
print(Neg_Num2)
# ________________________________ #