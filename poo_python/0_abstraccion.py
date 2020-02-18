#!/bin/env python3
"""Abstraccion"""
class Lavadora:
    def __init__(self):
        pass

    def lavar(self, temp='caliente'):
        self._llenar_tanque_de_agua(temp)
        self._añadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self, temp):
        print(f'Llenando el tanque con agua {temp}')
    def _añadir_jabon(self):
        print('Añadiendo jabon')

    def _lavar(self):
        print('Lavando la ropa')

    def _centrifugar(self):
        print('Centrifugando')


if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()
