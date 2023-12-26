#!/usr/bin/python
monstruos = [
    'orco',
    'trasgo',
    'troll',
    'goblin',
    False
]

print(type(monstruos))
print(len(monstruos))

heroes = list(
    ('elfo','enano','mago')
)

monstruos.append('Nazgul')
heroes.append('Clérigo')

print(type(heroes))
print(len(heroes))

print('Todos juntos:')
print(monstruos + heroes)

