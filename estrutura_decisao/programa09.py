# Um programa que lê duas notas parciais de um aluno. O programa deve calcular a média alcançada pelo aluno e apresentar a mensagem "Aprovado", se a média alcançada for maior ou igual a sete; a mensagem "Reprovado", se a média for menor do que sete; a mensagem "Aprovado com distinção", se a média for igual a dez

# Pede a primeira nota
nota1 = input("Digite a primeira nota: ")

# Pede a segunda nota
nota2 = input("Digite a segunda nota: ")

# Converte as entradas do usuário de textos para números
nota1 = float(nota1)
nota2 = float(nota2)

# Calcula a média das notas
media = (nota1 + nota2) / 2

# Testa a média e mostra a mensagem apropriada
if media == 10:
  print("Aprovado com distinção")
elif media >= 7:
  print("Aprovado")
else:
  print("Reprovado")
