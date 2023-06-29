#A prefeitura de Bebedouro abriu uma linha de crédito para os
#funcionários estatutários. O valor máximo da prestação não poderá ultrapassar
#30% do salário bruto. Fazer um algoritmo que permita entrar com o salário bruto
#e o valor da prestação, e informar se o empréstimo pode ou não ser concedido.

# ___________________________________________________________________________ #

SalarioBruto = float(input('Digite o valor do seu salário: '))
print('Primeiramente o seu salário é de: ', SalarioBruto)

print('')

Emprestimo = float(input('Qual seria o valor do empréstimo?: '))
print('O valor do empréstimo desejado é: ', Emprestimo)

print('')

if SalarioBruto * 0.3 >= Emprestimo:
  print('O valor do empréstimo desejado pode ser efetuada!')
else:
  print('O valor do empréstimo desejado não pode ser efetuada!')

# ___________________________________________________________________________ #