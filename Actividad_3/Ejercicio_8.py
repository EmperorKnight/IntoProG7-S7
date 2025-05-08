# 8. Encontrar el mayor y el menor de N números
# Enunciado: Pide al usuario la cantidad N de números y luego solicita cada número.
# Encuentra el número mayor y el número menor.
# Especificación: Usa un bucle for, y acumuladores.

import os

os.system("cls || clear")

cantidad_numeros = int(input("Introduzca la cantidad de numeros a introducir \n-> "))
print(f"Introduzca los numeros")
Ingresados = []
mayor = 0
menor = 0

for i in range(cantidad_numeros):
    numero = int(input("-> "))
    Ingresados.append(numero)
    if i == 0:
        mayor = numero
        menor = numero
    else:
        if numero > mayor:
            mayor = numero
        elif numero < menor:
            menor = numero

os.system("cls || clear")
print(f"Los numeros introducidos fueron {Ingresados} \n----------------------- ")
print(f"El mayor es: {mayor:,} \nEl menor es: {menor:,} \n----------------------- ")
