#  CONTINUAÇÃO DO WHILE / ELSE
# CONTADORES E ACUMULADORES


contador = 1 
acumulador = 1


while contador <= 10:
    print (contador , acumulador)
    
    if contador > 5:
        break

    acumulador = acumulador + contador
    contador = contador + 1

else:
    print('ACABOU !')