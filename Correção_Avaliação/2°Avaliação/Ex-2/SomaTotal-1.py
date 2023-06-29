# Escreva um algoritmo para ler 10 números e ao
# final da leitura escrever a soma total dos 10 números lidos.

soma = 0

# ______________________________________________ #
for i in range(1,11):
  ler = int(input('Insira o valor: '))
  soma = soma + ler
print(soma)
# ______________________________________________ #