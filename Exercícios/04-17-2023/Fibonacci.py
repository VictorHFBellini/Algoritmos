# Escreva um programa que gere a sequência de Fibonacci até um determinado limite fornecido pelo usuário. 
# A sequência de Fibonacci começa com 0 e 1,
# e cada número subsequente é a soma dos dois números anteriores.

trem1 = 0
trem2 = 1
trem3 = 0

for F in range(10):
  if trem1 < 1:
    print(trem3)
    trem3 = trem1 + trem2
    trem1 = trem2
    trem2 = trem3
  else:
    print(trem1)
    trem3 = trem1 + trem2
    trem1 = trem2
    trem2 = trem3

# ______________________________________________ #