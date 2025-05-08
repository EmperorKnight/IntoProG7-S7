# 5. Factorial de un número
# Enunciado: Pide al usuario un número entero positivo y calcula su factorial.
# Especificación: Usa un bucle while y un acumulador (para el producto).

import os, sys

sys.set_int_max_str_digits(1000000)
os.system("cls || clear")
numero = int(input(f"Introduzca un numero para obtener su factorial \n-> "))

i = 1
numero1 = numero
factorial = numero

while i != numero:
    numero1 -= 1
    factorial *= numero1
    i += 1

os.system("cls || clear")
print(f"----------------------- \nEl resultado de {numero:,}! = {factorial:,}\n----------------------- ")