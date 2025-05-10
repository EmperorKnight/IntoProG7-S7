# 5. Factorial de un número
# Enunciado: Pide al usuario un número entero positivo y calcula su factorial.
# Especificación: Usa un bucle while y un acumulador (para el producto).

import os, sys, time

sys.set_int_max_str_digits(1000000)
os.system("cls || clear")
numero = int(input(f"Introduzca un numero para obtener su factorial \n-> "))

i = 1
numero1 = numero
factorial = numero
salida = []

while i != numero:
    salida.append(str(numero1))
    p = " * ".join(salida)
    numero1 -= 1
    factorial *= numero1
    i += 1

os.system("cls || clear")
print(f"\n----------------------- \nEl resultado de {numero:,}! = {p} * 1 = {factorial:,}\n----------------------- ")