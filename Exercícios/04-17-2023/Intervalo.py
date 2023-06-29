# Utilizando a estrutura de repetição for, faça um programa em python que receba 10 números 
# e conte quantos deles estão no intervalo [10,20] e quantos deles estão fora do intervalo, 
# escrevendo estas informações.

EstaoDentro = 0
EstaoFora = 0

for i in range(10):
  Inserir = float(input('Digite um número a sua escolha: '))

  if (Inserir <= 10) or (Inserir >= 20):
    EstaoFora = EstaoFora + 1
  else:
    EstaoDentro = EstaoDentro + 1
print('Na execusão foi encontrado', EstaoDentro, 'em um intervalo de 10 a 20, e', EstaoFora, 'fora desse intervalo!')