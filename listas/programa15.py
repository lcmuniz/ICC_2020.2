# Um programa que lê 4 notas, armazena em uma lista, mostra as notas e a média na tela.

# Inicializa o array de notas
notas = []

# Laço para pedir as 4 notas
for i in range(1, 5):
  numero = input("Digite um número: ")
  numero = float(numero)
  notas = notas + [numero]

# Inicializa a soma das notas
soma = 0

# Laço para somar as notas
for i in range(len(notas)):
  soma = soma + notas[i]

# Calcular a média
media = soma / len(notas)

# Mostras as notas e a média na tela
print("Notas: ", notas)
print("Média: ", media)