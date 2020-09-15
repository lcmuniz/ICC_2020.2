# Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo .
# b) a soma do triplo do primeiro com o terceiro.
# c) o terceiro elevado ao cubo.

# 1 - Solicitar o primeiro número (inteiro) e armazenar em n1

n1 = input("Digite o primeiro número (inteiro): ")
n1 = int(n1)

# 2 - Solicitar o segundo número (inteiro) e armazenar em n2
n2 = input("Digite o segundo número (inteiro): ")
n2 = int(n2)

# 3 - Solicitar o terceiro número (real) e armazenar em n3
n3 = input("Digite o terceiro número (real): ")
n3 = float(n3)

# 4 - Calcular o produto do dobro do primeiro com metade do segundo e armazenar em resultado1

resultado1 = (n1 * 2) * (n2 / 2) 

# 5 - Calcular a soma do triplo do primeiro com o terceiro e armazenar em resultado2
resultado2 = (n1 * 3) + n3

# 6 - Elevar o terceiro número ao cubo e armazenar em resultado3
resultado3 = n3 ** 3

# 7 - Mostrar resultado1, resultado2 e resultado3
print("Resultado 1:", resultado1)
print("Resultado 2:", resultado2)
print("Resultado 3:", resultado3)

