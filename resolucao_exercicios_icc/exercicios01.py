while (True):
  email = input('Digite o seu email: ')

  senha = input('Digite a sua senha: ')

  if senha == email or len(senha) < 6:
    print('Senha inválida.')
  else:
    print('Bem-vindo.')
    break

