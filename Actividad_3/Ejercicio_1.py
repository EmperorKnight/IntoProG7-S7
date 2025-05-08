# 1. Suma de los primeros N números
# Enunciado: Pide al usuario un número entero positivo N y calcula la suma de los
# números desde 1 hasta N.
# Especificación: Usa un bucle for y un acumulador.

import os

os.system("cls || clear")
N = int(input(f"Introduzca un numero \n-> "))

acumulador = 0

for i in range(1,N+1):
    acumulador += i

os.system("cls || clear")
print(f"----------------------- \nLa sumatoria desde el 1 hasta el {N:,}")
print(f"Da un total de: {acumulador:,}\n----------------------- ")