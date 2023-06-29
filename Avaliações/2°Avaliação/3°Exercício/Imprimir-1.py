# Escreva um algoritmo para ler 2 valores e se o segundo valor informado for ZERO, deve
# ser lido um novo valor, ou seja, para o segundo valor não pode ser aceito o
# valor zero e imprimir o resultado da divisão do primeiro valor lido pelo
# segundo valor lido.

# __________________________________________________________ #
numero1 = float(input('Insira o primeiro valor: '))
numero2 = float(input('Insira o segundo valor: '))

while numero2 == 0:
    numero2 = float(input("Inisira outro valor: "))
    
divisão = numero1 / numero2

print("O resultado da divisão é:", divisão)
# __________________________________________________________ #