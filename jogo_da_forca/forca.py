
import random 

# Ler arquivo 
arquivo = open('palavras.txt', 'r')

conteudo = arquivo.read()

linhas = conteudo.split('\n')

tamanho = len(linhas)

# Escolhe uma palavra aleatória do arquivo
indice = random.randint(0, tamanho - 1)

palavra = linhas[indice]

palpites = ""

tentativas = 10

while tentativas > 0:
  erros = 0
  for letra in palavra:
    if letra in palpites: 
      print(letra, end = " ")
    else:
      print("_", end = " ")
      erros = erros + 1

  print()

  if erros == 0:
    print("Você venceu!")
    break
  
  palpite = input("Digite uma letra: ")
  palpites = palpites + palpite

  if palpite not in palavra:
    tentativas = tentativas - 1
    print("Você errou")
    print("Você tem", tentativas, " tentativas")

    if tentativas == 0:
      print("Você perdeu!")