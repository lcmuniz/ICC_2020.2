# Um programa que lê três números e mostra o maior deles.

# Pede o primeiro número
numero1 = input("Digite o primeiro número: ")

# Pede o segundo número
numero2 = input("Digite o segundo número: ")

# Pede o terceiro número
numero3 = input("Digite o terceito número: ")

# Converte as entradas do usuário de textos para números
numero1 = float(numero1)
numero2 = float(numero2)
numero3 = float(numero3)

# Assume que o maior é numero1
maior = numero1

# Testa se o maior é numero2 
if numero2 > maior:
  maior = numero2

# Testa se o maior é numero3 
if numero3 > maior:
  maior = numero3

# Mostra que é o maior na tela
print("O maior número é", maior)
