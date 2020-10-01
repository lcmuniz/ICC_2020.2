# Um programa que calcula as raízes de uma equação do 2o grau
# O programa pede os coeficientes A, B e C da equação
# e usa uma função para calcular as raízes

# Função para calcular o delta
def delta(a, b, c):
  return (b ** 2) - (4 * a * c)

# Função para calcular as raízes
def equacao2grau(a, b, c):

  d = delta(a,b,c)

  if d < 0:
    return None
  elif d == 0:
    return [(-b) / (2 * a)]
  else:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    return [x1, x2]

# Pede os coeficientes
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

# Calcula as raizes
resultado = equacao2grau(a, b, c)

if resultado == None:
  print("Não existem raízes reais")
elif len(resultado) == 1:
  print("A raíz é", resultado[0])
else:
  print("As raízes são: ", resultado)