'''

OPERADORES LOGICOS
and, not, or
in e not in
'''
#   True e False = False
# comparacao1 and comparacao2
#  True OU True = True

# a = 2
# b = 3

# if not b > a:
#     print('B é maior que A')

# else:
#     print('A é maior que B')

# letra = input('Insira a letra que pretende achar: ')
# nome = input('Digite seu nome: ')


# if letra in nome:
#     print(f'Existe a letra "{letra}" na palavra "{nome}". ')

# else:
#     print(f'Não existe a letra "{letra}" na palavra "{nome}".')

user = input('Insira Usuário: ')
senha = input('Insira Senha: ')

user_log = 'SamuelVBF'
senha_log = '1234567890'

if user == user_log and senha == senha_log:
    print('Você está Logado!')
else:
    print('Usuário ou senha não identificados, Tente novamente.')
