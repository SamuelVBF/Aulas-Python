# QUANTIDADE DE CARACTERES USANDO FUNÇÃO "len" e só funciona com 'String'

usuario = input('Digite seu usario: ')
caracteres = len(usuario)

if caracteres < 8:
    print('Por favor, insira um usuario maior!')
else:
    print(f'Cadastro Realizado. \n Olá {usuario} ! ')
