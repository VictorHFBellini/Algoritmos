# A sequência de Fibonacci tem papel importante na explicação
# de fenômenos naturais. Ela é também bastante utilizada para fins estéticos, pela
# sua reconhecida harmonia. Exemplo disso foi sua utilização na construção do
# Partenon, em Atenas. A sequência dá-se inicialmente por dois números 1. A
# partir do terceiro elemento usa-se a expressão: elemento n = elementon1
# + elementon2. Exemplo de sequência: 1, 1, 2, 3, 5, 8. Construa um
# algoritmo que imprima na tela os 10 primeiros elementos da sequência de Fibonacci.

# __________________________________________________________________________ #

n1 = 1
n2 = 1
n3 = n1 + n2
n4 = n2 + n3
n5 = n3 + n4
n6 = n4 + n5
n7 = n5 + n6
n8 = n6 + n7
n9 = n7 + n8
n10 = n8 + n9

print(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10)

# __________________________________________________________________________ #

n1 = 1
n2 = 1
n3 = n1 + n2
n4 = n2 + n3
n5 = n3 + n4
n6 = n4 + n5
n7 = n5 + n6
n8 = n6 + n7
n9 = n7 + n8
n10 = n8 + n9

print('', n1)
print('','', n2)
print('','','', n3)
print('','','','', n4)
print('','','','','', n5)
print('','','','','','', n6)
print('','','','','','','', n7)
print('','','','','','','','', n8)
print('','','','','','','','','', n9)
print('','','','','','','','','','', n10)

# __________________________________________________________________________ #

trem1 = 0
trem2 = 1
trem3 = 0

for i in range(10):
  if trem1 < 1:
    print(trem2)
    trem3 = trem1 + trem2
    trem1 = trem2
    trem2 = trem3
  else:
    print(trem3)
    trem3 = trem1 + trem2
    trem1 = trem2
    trem2 = trem3

# __________________________________________________________________________ #