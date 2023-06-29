qtd = 10
media = 0
maior = 0
menor = 0
idadeMaior = 0

for i in range(qtd):
  Idade = int(input('Quantos anos você tem?: '))

  media += Idade

  if Idade > 18:
    maior += 1
  if Idade < 5:
    menor += 1
  if idadeMaior < Idade:
    idadeMaior = Idade

print('Média da idade do grupo é de: ', media/qtd)
print('No grupo possui, ', maior, 'maiores de idade' )
print('No grupo possui, ', menor, 'menores de idade' )
print('A maior idade foi: ', idadeMaior)