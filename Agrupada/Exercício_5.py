qtd = 2
peso = 0
altura = 0
mediaAlt = 0
maiorQNoventa = 0
menorPeso = 0
maiorPeso = 0


for i in range(qtd):
  peso = float(input('Insira o seu peso: '))
  altura = float(input('Insira a sua altura: '))

  mediaAlt += altura

  if peso > 90:
    maiorQNoventa += 1
  if (peso < 50) and (altura < 1.60):
    menorPeso += 1
  if (altura > 1.90) and (peso > 100):
    maiorPeso += 1

print('Média de altura do grupo é de: ', mediaAlt/qtd)
print('No grupo possui, ', maiorQNoventa, 'pessoas com mais de 90Kg' )
print('No grupo possui, ', menorPeso, 'pessoas com menos de 50Kg e menos de 1.60m' )
print('No grupo possui, ', maiorPeso, 'pessoas com mais de 1.90m e mais de 100Kg' )
