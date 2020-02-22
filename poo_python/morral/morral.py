#!/usr/bin/env python3
"""
Function to solve the problem of bag
"""
def morral(tamano_moral, pesos, valores, n):
    if n == 0 or tamano_moral == 0:
        return 0
    if pesos[n - 1] > tamano_moral:
        return morral(tamano_moral, pesos,valores, n - 1)

    return max(valores[n -1] + morral(tamano_moral - pesos[n - 1], pesos, valores, n - 1), morral(tamano_moral, pesos, valores, n - 1))

if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_moral = 5
    n = len(valores)

    resultado = morral(tamano_moral, pesos, valores, n)
    print(resultado)
