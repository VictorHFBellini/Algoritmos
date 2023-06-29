# Utilizando o código anterior escreva
# um algoritmo para ler 10 números. Todos os números lidos com valor inferior a
# 40 devem ser somados. Escreva o valor final da soma efetuada.

soma = 0

# ______________________________________________ #
for i in range(1,11):
  ler = int(input('Insira o valor: '))
  if ler < 40:
    soma = soma + ler
print(soma)
# ______________________________________________ #
