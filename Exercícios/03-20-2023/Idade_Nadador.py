# Elabore um algoritmo que dada a idade de um nadador classifica-o em uma das seguintes categorias:
#  infantil I - 5 a 7 anos
#  infantil II - 8 a 10 anos
#  juvenil I - 11 a 13 anos
#  juvenil II - 14 a 17 anos
#  adulto - maiores de 18 anos

# ________Código para organizar Categorias de Nadadores________ #
Idade = int(input("Insira a sua idade para melhor organização: "))
# _____________________________________________________________ #

# __________Implementando o If, Elif e Else__________ #
if Idade <= 7:
  print('Você está na classificação Infantil I: ')
elif Idade <= 10:
  print('Você está na classificação Infantil II: ')
elif Idade <= 13:
  print('Você está na classificação Juvenil I: ')
elif Idade <= 17:
  print('Você está na classificação Juvenil II: ')
else:
  print('Você está na classificação Adulto: ')
# ___________________________________________________ #