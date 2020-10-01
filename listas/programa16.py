# Um programa que lê dois vetores com 5 elementos cada. Gera um terceiro vetor de 5 elementos, cujos valores são compostos pelos elementos intercalados dos dois outros vetores.

# Inicializa vetores
vetor1 = []
vetor2 = []
vetor3 = []

# Pede os números do primeiro vetor
print("Números do primeiro vetor")
for i in range(5):
  val = input("Digite um número: ")
  vetor1.append(float(val))


# Pede os números do segundo vetor
print("Números do segundo vetor")
for i in range(5):
  val = input("Digite um número: ")
  vetor2.append(float(val))


# Intercala os números dos dois vetores no terceiro vetor
for i in range(5):
  vetor3.append(vetor1[i])
  vetor3.append(vetor2[i])


# Mostra os vetores
print("Vetor 1: ", vetor1)
print("Vetor 2: ", vetor2)
print("Vetor 3: ", vetor3)

