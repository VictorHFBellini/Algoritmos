
soma = 0
for i in range(501):
  if (i % 3) == 0:
    if (i % 2) == 0:
      print(i, 'Par')
    else:
      soma = soma + i
      print(i, 'Impar')
      print('Soma = ',soma)