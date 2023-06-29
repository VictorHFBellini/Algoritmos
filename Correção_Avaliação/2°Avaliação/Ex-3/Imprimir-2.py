# Acrescentar uma mensagem de 'VALOR INVÁLIDO' no exercício anterior caso o segundo valor informado seja ZERO.

# __________________________________________________________ #
numero1 = float(input('Insira o primeiro valor: '))
numero2 = float(input('Insira o segundo valor: '))

while numero2 == 0:
    print('O valor "0" é INVÁLIDO, insira um novo valor !')
    numero2 = float(input("Inisira outro valor, para realizar a divisão: "))
    
divisão = numero1 / numero2

print("O resultado da divisão é:", divisão)
# __________________________________________________________ #