
idade = int(input('Qual a sua idade? '))

eh_estudante = input('É estudante? (S/N) ')

if idade > 65 or eh_estudante == 'S' or eh_estudante == 's':
  print('Você paga meia: R$ 15,00')
else:
  print('Você paga inteira: R$ 30,00')


