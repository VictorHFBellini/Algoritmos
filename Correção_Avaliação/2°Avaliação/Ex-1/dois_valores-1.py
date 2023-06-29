# Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior
# deles.

# ________________________________________________ #
num1 = float(input('Insira o primeiro número: '))
num2 = float(input('Insira o segundo númmero: '))

while (num1 == num2):
  print('Valor inválido, insira outro valor !')
  num2 = float(input('Insira o segundo númmero: '))
if num2 > num1:
  print(num2)
else:
  print(num1)
# ________________________________________________ #