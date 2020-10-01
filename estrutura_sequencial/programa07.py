# Um programa que pede a temperatura em graus Fahrenheit, transforma e mostra a temperatura em graus Celsius.


# Pede a temperatura ao usuário
fahrenheit = input("Digite a temperatura em Fahrenheit: ")

# Converte a entrada do usuário de texto para número
fahrenheit = float(fahrenheit)

# Converte a temperatura para Celsius
celsius = 5 * ( (fahrenheit - 32) / 9)

# Mostra a temperatura em Celsius na tela
print(fahrenheit, "ºF =", celsius, "ºC")