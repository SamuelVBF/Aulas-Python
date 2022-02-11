'''
 OPERADORES RELACIONAIS

==  IGUALDADE
>   MAIOR QUE
>=  MAIOR OU IGUAL
<   MENOR QUE 
<=  MENOR OU IGUAL
!=  DIFERENTE 

 '''

# print( 2 == 2 )
# print( 2 > 2 )
# print( 2 >= 2 )
# print( 2 < 2 )
# print( 2 <= 2 )
# print( 2 != 2 )

nome = input('Digite o seu nome: ')
idade = int(input('Digite sua idade: '))
muito_jovem = 20
muito_velho = 65

if idade < muito_jovem:  # pode ser usado o 'and' e excluir o 'elif'
    print(f'{nome}, o emprestimo nao foi aprovado pois o nao atende à idade minima.')
elif idade > muito_velho:
        print(f'{nome}, o emprestimo nao foi aprovado pois o nao atende à idade máxima.')

else:
    print(f'{nome}, o emprestimo foi autorizado.')

