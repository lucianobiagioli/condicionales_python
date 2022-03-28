# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda


if texto_1 < texto_2:
    print('texto_1 es menor a texto_2')
elif texto_1 == texto_2:
    print('las 2 palabras son iguales')
else:
    print('texto_1 es mayor a texto_2')


# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda


l_1 = len(texto_1)
l_2 = len(texto_2)

if l_1 > l_2:
    print('texto_1 tiene mas letras que texto_2')
elif l_1 == l_2:
    print('las 2 palabras tienen la misma cantidad de letras')
else:
    print('texto_2 tiene mas letras que texto_1')


# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

if texto_1[0] > texto_2[0]:
    print('la primer letra de {} es mayor que la primer letra de {}'.format(texto_1 , texto_2))
elif texto_1[0] < texto_2[0]:
    print('la primer letra de {} es mayor que la primer letra de {}'.format(texto_2 , texto_1))
else:
    print('las 2 letras son iguales')


copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

if texto_1 == copia_texto_1:
    print('la copia se realizo con exito')
   

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

if texto_2 != copia_texto_1:
    print('texto_2 y copia_texto_1 son distintas')

