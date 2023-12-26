#!/usr/bin/python

nombres_de_usuarios = "Antón, Daniel, Borja, Reyes"
nombres = nombres_de_usuarios.split(',')
ultimo_nombre = nombres[-1].strip()
hacked_name = ultimo_nombre.replace('Reyes', 'Borja')

lenguaje = 'python'
frase = "El usuario \"{}\" es un 'crack' de {}"

print(frase.format(hacked_name, lenguaje))

# Contar repeticiones
frase2 = "Me gusta mucho mucho mucho repetirme"
palabra_repetida = 'mucho'
print(frase2.count(palabra_repetida))

