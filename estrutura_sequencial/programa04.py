# Um programa que pede 4 notas bimestrais ao usuário e mostra a média.

# Pede a primeira nota ao usuário
nota1 = input("Digite a primeira nota: ")

# Pede a segunda nota ao usuário
nota2 = input("Digite a segunda nota: ")

# Pede a terceira nota ao usuário
nota3 = input("Digite a terceira nota: ")

# Pede a quarta nota ao usuário
nota4 = input("Digite a quarta nota: ")

# Converte as entradas do usuário (que são textos) em números
nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
nota4 = float(nota4)

# Calcula a média
media = (nota1 + nota2 + nota3 + nota4) / 4

# Mostra a média na tela
print("A média das notas é", media)