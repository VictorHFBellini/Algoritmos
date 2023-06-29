# Tendo como dados de entrada a altura e o sexo de uma pessoa (M masculino e F feminino), construa um
# algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#   para homens: (72.7*h)-58
#   para mulheres: (62.1*h)-44.7
#   altura = float(input('Insira sua altura: '))
#   sexo = str(input('Qual o seu sexo (M ou F): '))

if sexo == "M":
  peso_ideal = (72.7 * altura) - 58
  print('O peso ideal para a sua altura é: ', peso_ideal)
elif sexo == "F" :
  peso_ideal = (62.1 * altura) - 44.7
  print('O peso ideal para a sua altura é: ', peso_ideal)