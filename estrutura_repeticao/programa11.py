# Um programa que pede uma nota, entre zero e dez. Mostra uma mensagem caso o valor seja inválido e continua a pedir até que o usuário informe um valor válido.

# Pede a nota ao usuário
nota = input("Digite uma nota entre 0 e 10: ")

# Converte em número
nota = float(nota)

# Enquanto a nota não estiver entre 0 e 10...
while nota < 0 or nota > 10:

  # Mostra mensagem de nota inválida
  print("Nota inválida")

  # Pede a nota novamente
  nota = input("Digite uma nota entre 0 e 10: ")

  # Converte em número
  nota = float(nota)

# Mostra a nota válida na tela
print("A nota válida foi", nota)