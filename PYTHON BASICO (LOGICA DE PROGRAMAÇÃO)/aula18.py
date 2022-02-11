'''
UTILIZAR "while" PARA REALIZAR AÇÕES ENQUANTO UMA CONDIÇÃO FOR VERDADEIRA

REQUISITOS: ENTENDER CONDIÇÕES E OPERADORES
'''

# num = input('Insira um numero entre 0-5: ')

# while num <= 5:
#     print(num)
#     num = num + 1
...  

# x = 0
# while x < 10:
#     y = 0

#     while y < 5:
#         print(f'({x},{y})')
#         y = y + 1

#     x = x + 1

...

#CALCULADORA BASICA

while True:
    print()
    num1 = input('Digite um numero: ')
    operador = input('Digite um operador: ')
    num2 = input('Digite outro número: ')
    
    if not num1.isnumeric() or not num2.isnumeric():
        print('Por favor, insira um numero válido.')
        continue
    num1 = int(num1)
    num2 = int(num2)
    

    if operador == '+':  # (+ - / * **)
        print(num1 + num2)
        break
    elif operador == '-':
        print(num1 - num2)
        break
    elif operador == '/':
        print(num1 / num2)
        break
    elif operador == '*':
        print(num1 * num2)
        break
    elif operador == '**':
        print(num1 ** num2)
        break



