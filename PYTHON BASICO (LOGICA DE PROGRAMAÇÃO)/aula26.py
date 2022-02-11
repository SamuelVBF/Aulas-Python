"""
Operador ternario
"""
idade = input('Qual a sua idade: ')


if not idade.isnumeric():
    print('Digite apenas numeros')
    
else:
    idade = int(idade)
    maior = (idade >= 18)
    msg = 'pode entrar' if maior else 'nao pode entrar'

    print(msg)