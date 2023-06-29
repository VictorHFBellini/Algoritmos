codUser = 1234
senhaUser = 9999

Usuario = int(input('insira o seu código de usuário: '))

if Usuario == codUser:
  Senha = int(input('insira a sua senha: '))
  if Senha == senhaUser:
    print('Acesso Liberado')
  else:
    print('Senha incorreta')
else:
  print('Usuário Inválido')