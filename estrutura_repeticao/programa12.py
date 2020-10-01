# Um programa que lê 5 números e informa a soma e a média dos números.

quantidade = 5
soma = 0

# Um laço de 5 passos
for i in range(1, quantidade+1):
  
  # Pede o número ao usuário
  numero = input("Digite o " + str(i) + "º número: ")

  # Converte a entrada do usuário de texto para número
  numero = float(numero)

  # Acumula cada número em soma
  soma = soma + numero

# Calcula a média
media = soma / quantidade

# Mostra os resultados
print("A soma é", soma)
print("A média é", media)