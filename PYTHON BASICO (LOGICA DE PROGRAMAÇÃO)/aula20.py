#    Indices
#    0123456789......................33

frase = 'o rato roeu a roupa do rei de roma'  #iteravel / ATO DE PERCORRER TODOS OS COMPONETES DA FRASE
tamanho_frase = len(frase)
contador = 0
nova_string = ''

nova_letra = input(" Qual letra voce gostaria de modificar? ")

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == nova_letra:
        
        nova_string += nova_letra.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)


