# A prefeitura de uma cidade deseja fazer uma pesquisa entre seus habitantes. Faça
# um algoritmos para coletar dados sobre o salário e número de filhos de cada
# habitante e após as leituras, escrever: a)
# Média de salário da população
# Média do número de filhos
# Maior salário dos habitantes
# Percentual de pessoas com salário menor que R$ 150,00

# Obs.: O final da leituras dos dados se dará
# com a entrada de um “salário negativo”.

salário = 0
i = 0
totalSalario = 0
totalFilho = 0
maiorSalario = 0
totalMenor150 = 0

while salário >= 0:
  salário = float(input('Insira o salário: '))
  if salário >= 0:
    if salário < 150:
        totalMenor150 += 1
    if salário > maiorSalario:
      maiorSalario = salário
    filhos = int(input('Insira a quantidade de filhos: '))
    i += 1
    totalFilho += filhos
    totalSalario += salário

medFilhos = totalFilho / i
medSalario = totalSalario / i

print('A média dos salários é: ', medSalario)
print('A média de filhos é: ', medFilhos)
print('O maior salário é: ', maiorSalario)
print('O percentual é: ', ((totalMenor150 / i)* 100), '%')