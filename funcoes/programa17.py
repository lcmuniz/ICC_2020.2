# Um programa, com uma função que necessita de três argumentos, 
# e que fornece a soma desses três argumentos.

# Declara a função
def soma3(x, y, z):
  return x + y + z

# Pede três números
num1 = int(input("Digite o primeiro número: "))

num2 = int(input("Digite o segundo número: "))

num3 = int(input("Digite o terceiro número: "))

# Soma os três números usando a função
soma = soma3(num1, num2, num3)

# Mostra a soma
print("A soma é", soma)