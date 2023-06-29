

altura = float(input('Insira sua altura: '))
sexo = input('Qual o seu sexo (M ou F): ')
peso = float(input('Qual o seu Peso: '))

# Calculando o Peso Ideal para Homens e Mulheres #
if sexo == "M":
  peso_ideal = (72.7 * altura) - 58
  print('O peso ideal para a sua altura é: ', peso_ideal)
elif sexo == "F" :
  peso_ideal = (62.1 * altura) - 44.7
  print('O peso ideal para a sua altura é: ', peso_ideal)
else:
  print('Gênero não encontrado!')
  print('')
# ______________________________________________ #

# Calculando A Indice de Massa Corporal #
imc = peso / (altura * 2)
print('Seu IMC é: ', imc)

if imc <= 18.5:
  print('Abaixo do peso')
elif (imc > 18.5) and (imc <= 25):
  print('Peso Normal')
elif (imc >= 25) and (imc <= 30):
  print('Acima do Peso')
else:
  print('Obesidade')
# _____________________________________ #