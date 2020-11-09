numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
operacao = input('Digite a operação (+, -, * ou /): ')

if operacao == '+':
  resultado = numero1 + numero2 
elif operacao == '-':
  resultado = numero1 - numero2
elif operacao == '*':
  resultado = numero1 * numero2 
elif operacao == '/':
  resultado = numero1 / numero2 
else:
  resultado = None

if (resultado == None):
  print('Operação Inválida')
else:
  print('O resultado é', resultado)

