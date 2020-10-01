# Um programa que pede dois números e imprime o maior deles.

# Pede o primeiro número ao usuário
numero1 = input("Digite o primeiro número: ")

# Pede o segundo número ao usuário
numero2 = input("Digite o segundo número: ")

# Converte as entradas do usuário de textos para números
numero1 = float(numero1)
numero2 = float(numero2)

# Testa qual número é o maior e imprime a mensagem adequada
if numero1 > numero2: 
  print("O primeiro número é maior")
elif numero2 > numero1:
  print("O segundo número é maior")
else:
  print("Os dois números são iguais")

