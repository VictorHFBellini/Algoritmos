# ________Inserindo as Variáveis________ #
Nota1 = float(input('Digite a 1º Nota: '))
Nota2 = float(input('Digite a 2º Nota: '))
# ______________________________________ #


# ________Soma e Media________ #
Soma = Nota1 + Nota2
print(Soma)
Media = Soma / 2
print(Media)
# ____________________________ #

# ___Utilizando if e o else___ #
if Media >= 7:
  print('Foi Aprovado')
elif Media <= 3:
  print('Foi Reprovado')
else:
  print('Recuperação')
# ____________________________ #