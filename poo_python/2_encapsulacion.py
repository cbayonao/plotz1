#!/usr/bin/env python3
"""Encapsulación, getters and setters"""
"""
Permite agrupar datos y su comportamiento.
Controla el acceso a dichos datos.
Previene modificaciones no deseadas.
"""
class CasillaDeVotacion:
    def __init__(self, identificador, pais):
        self._identificador = identifficador
        self._pais = pais
        self._region = None

    """Decorador para poder acceder al metodo con dot notation"""
    @property
    def region(self):
        return self._region

    """Funcion que nos permite modificar, el valor anterior, es decir seteandolo si se encuentra en la listabde regiones para el pais, de lo contrario ValueError"""
    @region.setter
    def set_region(self, region):
        if region in self._pais:
            self._region = region
        raise ValueError(f'La region {region} no es validad en {self._pais}')

# >>> casilla = CasillaDeVotacion(123, ['Ciudad de Mexico', 'Morelos'])
# >>> casilla.region
# None
# >>> casilla.region = 'Ciudad de Mexico'
# 'Ciudad de Mexico'
