#!/usr/bin/python

verdad = 0
falsedad = False

frase = 'Me encanta este método de python con esta palabra reserva: <in>'
palabra = 'encanta'

if palabra in frase:
    # Cosas que SÍ se imprimen:
    print('Esta frase se va a imprimir')
    print('Esto también se imprime')
else:
    print('Esto nunca se imprime, porque es falso')

