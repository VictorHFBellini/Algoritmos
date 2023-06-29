# Fazer um algoritmo que calcule a área de um trapézio. (base maior + base menor*altura /2)

# ______________Calculando a área do Trapézio______________ #
BaseMaior = float(input("Insira a Base Maior do Trapézio: "))
BaseMenor = float(input("Insira a Base Menor do Trapézio: "))
Altura = float(input("Insira a Altura do Trapézio: "))
# _________________________________________________________ #


# __________Área do Trapézio__________ #
Area = ((BaseMaior + BaseMenor) * Altura) / 2
print("A área do Trapézio é: " + str(Area))
# ____________________________________ #