#!/usr/bin/python

mi_coche = {
    "marca": "Ford Mondeo",
    "matrícula":"4567FFT",
    "color":"negro, como Batman"
}

#print(mi_coche["matrícula"])

# for clave in mi_coche.keys():
#     print(clave)
# 
# for valor in mi_coche.values() :
#     print(valor)

print('El método definitivo y perfecto, usando TUPLAS')

for clave,valor in mi_coche.items():
    frase = "Clave: {}, Valor: {}"
    print(frase.format(clave,valor))
    print('')