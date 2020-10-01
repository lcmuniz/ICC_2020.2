# Um programa que pede dois números e imprime a soma.

# Pede o primeiro número ao usuário
numero1 = input("Digite o primeiro número: ")

# Pede o segundo número ao usuário 
numero2 = input("Digite o segundo número: ")

# Converte as entradas do usuário (que são strings) em números
numero1 = float(numero1)
numero2 = float(numero2)

# Soma os dois números
soma = numero1 + numero2

# Mostra a soma na tela
print("A soma de", numero1, "e", numero2, "é", soma)