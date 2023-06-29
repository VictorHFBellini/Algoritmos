# ________Inserindo as Variáveis________ #
Nota1 = float(input('Digite a 1º Nota: '))
Nota2 = float(input('Digite a 2º Nota: '))
Nota3 = float(input('Digite a 3º Nota: '))
# ______________________________________ #


# ________Soma e Media________ #
Soma = Nota1 + Nota2 + Nota3
print(Soma)
Media = Soma / 3
print(Media)
# ____________________________ #

# ___Utilizando if e o else___ #
if Media >= 7:
  print('Foi Aprovado')
else:
  print('Foi Reprovado')
# ____________________________ #