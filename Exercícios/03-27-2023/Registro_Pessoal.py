
# faça um algoritmo que leia o nome, o sexo, eo estado civil.
# (M ou F) de uma pessoa.
# caso o estado civil seja "CASADA(o)", solicitar o
# tempo de casado(a), em (anos) e o nome do companheiro(a)
# e exibir o nome da pessoa, o tempo de casado e o nome do companheiro

Nome = input("Insira seu Nome Completo: ")
Estado_Civil = input('Qual é o seu Estado Civil ? ')
Sexo = input('Qual o seu Sexo (M ou F): ')

print('_________________________________')
print(Nome)

print('É: ', Estado_Civil)

print('Do sexo: ', Sexo)
print('')

if (Estado_Civil == 'Casada' or Estado_Civil == 'Casado'):
  print('Complete a documentação a seguir: ')
  print('_________________________________')

  Tempo_Casado = input('Quandos anos juntos?: ')
  Nome_Conjuge = input('Qual o nome do seu Companheiro(a): ')
  
  print('O Senhor(a)', Nome)
  print('')

  print('É', Estado_Civil)
  print('')

  print('Com a(o): ', Nome_Conjuge)
  print('')

  print('A', Tempo_Casamento)

  print('Obrigado pela Atenção !')

  print('_________________________________')
else:
  print('Obrigado pela Atenção !!')