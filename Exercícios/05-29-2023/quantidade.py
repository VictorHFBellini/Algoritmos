# Faça um algoritmo para ler uma quantidade e a
# seguir ler esta quantidade de números. Depois de ler todos os números o
# algoritmo deve apresentar na tela o maior dos números lidos e a média dos
# números lidos.

maior = 0
soma = 0

qtd = int(input('Insira a quantidade: '))

for i in range(qtd):
  valor = int(input('Qual é o valor: '))
  if i == 0:
    maior = valor
  if valor > maior:
    maior = valor
  soma += valor

média = soma/qtd

print('O maior valor é: ', maior)
print('A média é: ', média)
 