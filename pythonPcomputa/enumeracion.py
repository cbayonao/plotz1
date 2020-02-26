#!/usr/bin/env python3
"""
Funcion para obtener la raiz cuadrada de un numero
"""

objetivo = int(input('Escoge un numero entero: '))
respuesta = 0

while respuesta**2 < objetivo:
    print(respuesta)
    respuesta += 1

if respuesta**2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'{objetivo} no tiene una raiz cuadrada exacta')
