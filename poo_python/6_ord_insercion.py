#!/usr/bin/env python3
"""
Ordenamiento inserción
"""
import random

def ordenamiento_de_insercion(lista):
    
    
            


if __name__ == '__main__':
    tamaño_de_lista = int(input('De que tamaño sera la lista? '))
    lista = [random.randint(0, 100) for i in range(tamaño_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_de_insercion(lista)
    print(lista_ordenada)
