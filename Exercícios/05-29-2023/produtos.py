# Faça um algoritmo para ler o código e o preço
# de 15 produtos, calcular e escrever:
# o maior preço lido
# a média aritmética dos preços dos produtos

maior = 0
soma = 0

for i in range(15):
  cod = input('Qual é o código: ')
  valor = int(input('Insira o valor: '))
  if i == 0:
    maior = valor
  if valor > maior:
    maior = valor
  soma += valor

média = soma/15

print('O maior valor é: ', maior)
print('A média é: ', média)