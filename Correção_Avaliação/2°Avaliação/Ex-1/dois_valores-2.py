# Utilizando o código do exercício anterior, ler
# dois valores (considere que não serão
# lidos valores iguais) e escrevê-los em ordem crescente.

# ________________________________________________ #
num1 = float(input('Insira o primeiro número: '))
num2 = float(input('Insira o segundo númmero: '))

while (num1 == num2):
  print('Valor inválido, insira outro valor !')
  num2 = float(input('Insira o segundo númmero: '))
if num2 < num1:
  print(num2, num1)
else:
  print(num1, num2)
# ________________________________________________ #