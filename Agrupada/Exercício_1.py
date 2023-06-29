HorasTrabalhadas = int(input('Quantas horas você trabalhou nesse mês? (Em 4 Semanas): '))
SalarioHora = float(input('Quando que você recebe por Hora?: '))

if HorasTrabalhadas <= 160:
  SalarioTotal = HorasTrabalhadas * SalarioHora
  print('O seu salário foi de: ', SalarioTotal)

if HorasTrabalhadas > 160:
  HorasExtras = (HorasTrabalhadas - 160)
  acrescimoHora = ((HorasExtras * SalarioHora) * 0.5)
  SalarioTotal = ((HorasTrabalhadas * SalarioHora) + acrescimoHora)
  print('O seu salário foi de: ', SalarioTotal)