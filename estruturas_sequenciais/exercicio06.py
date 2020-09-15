# Faça um programa que peça o raio de um círculo, calcule e mostre sua área.

# 1 - Solicitar o raio do círculo em cm e armazenar na variável raio 
raio = input("Digite o raio do círculo em cm: ")

# 2 - Converter o valor digitado pelo usuário em número real e armazenar na variavel raio 
raio = float(raio)

# 3 - Calcular a área do círculo e armaazenar na variável area 
area = 3.14159265 * raio ** 2

# 4 - Mostrar a área do círculo 
print("A área do círculo de raio", raio, "é", area)