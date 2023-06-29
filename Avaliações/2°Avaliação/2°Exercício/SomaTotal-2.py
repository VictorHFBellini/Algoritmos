# Utilizando o código anterior escreva
# um algoritmo para ler 10 números. Todos os números lidos com valor inferior a
# 40 devem ser somados. Escreva o valor final da soma efetuada.

# ________________________________________________________ #
soma = 0

for i in range(10):
    numero = float(input('Insira um valor: '))
    if numero < 40:
      soma = soma + numero

print('A soma dos números inferiores a 40 é:', soma)
# ________________________________________________________ #