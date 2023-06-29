aluguel = 0
valorkm = 0

tipoCarro = input('Qual é o tipo do carro? (popular ou luxo): ')
diasAluguel = int(input('Quantos dias ?: '))
kmPercorrido = float(input('Quantos km percorrido ?: '))

if tipoCarro == 'popular':
  aluguel = diasAluguel * 90
  if kmPercorrido < 100:
    valorkm = kmPercorrido * 0.20
  else:
    valorkm = kmPercorrido * 0.10

elif tipoCarro == 'luxo':
  aluguel = diasAluguel * 150
  if kmPercorrido < 100:
    valorkm = kmPercorrido * 0.30
  else:
    valorkm = kmPercorrido * 0.25
else:
  print('Valor inválido !')

print('O valor do aluguel é: ', aluguel)
print('O valor total de km é: ', valorkm)
print('O valor total é: ', aluguel + valorkm)