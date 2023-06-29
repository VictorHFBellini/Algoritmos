# Escreva um algoritmo que leia um número e informe se ele é
# divisível por 10, por 5 ou por 2 ou se não é divisível por nenhum deles

# ___________________________________________________________________________ #

Num = float(input('Digite um número de sua preferência: '))
print('O número escolhido foi: ', Num)

print('')

if Num % 10 == 0:
  print('Seu número é divisível por 10!')
elif Num % 5 == 0:
  print('Seu número é divisível por 5!')
elif Num % 2 == 0:
  print('Seu número é divisível por 2!')
else:
  print('Seu número não é divisível por nenhum dos seguintes números: (10, 5, 2)')

# ___________________________________________________________________________ #