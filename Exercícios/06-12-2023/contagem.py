vInicial = int(input('Qual o valor inicial: '))
vFinal = int(input('Qual o valor final: '))
vInc = int(input('Valor do Incremento: '))
qtd = vFinal - vInicial

for i in range(vInicial, vFinal+1, vInc):
  print(i)