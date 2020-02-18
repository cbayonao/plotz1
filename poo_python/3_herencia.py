#!/usr/bin/env python3
"""
Herencia - Inheritance
"""
"""
-Modelar una jerarquia de clases
-Permite compartir compartamiento comun en la jerarquia
-Al padre se le conoce como superclase y al hijo como subclase
"""
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

if __name__ == '__main__':
    rectangulo = Rectangulo(base=3, altura=4)
    print(rectangulo.area())

    cuadrado = Cuadrado(lado=5)
    print(cuadrado.area())
