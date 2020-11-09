def eh_primo(numero):
  i = 2
  while i < numero:
    if numero % i == 0:
      return False
    i = i + 1
  return True


n = int(input('Digite um número: '))

i = 1

while i <= n:
  if (eh_primo(i)):
    print(i)
  i = i + 1

  