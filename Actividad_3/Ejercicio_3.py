# 3. Contar vocales en una cadena
# Enunciado: Pide al usuario una cadena y cuenta cuántas vocales (a, e, i, o, u) tiene.
# Especificación: Usa un bucle for para recorrer la cadena y contadores para cada
# vocal.

import os

os.system("cls || clear")
cadena = input(f"Introduzca una cadena cualquiera \n-> ")
cadena = cadena.lower()
vocales = ["a","e","i","o","u"]

total_vocales = 0
vocal_a = 0
vocal_e = 0
vocal_i = 0
vocal_o = 0
vocal_u = 0

for i in cadena:
    if i in vocales:
        total_vocales += 1

for j in cadena:
    if j == "a":
        vocal_a += 1
    elif j == "e":
        vocal_e += 1
    elif j == "i":
        vocal_i += 1
    elif j == "o":
        vocal_o += 1
    elif j == "u":
        vocal_u += 1

cadena = cadena.capitalize()

os.system("cls || clear")
print(f"----------------------- \nOración introducida: {cadena}\nTotal de vocales: {total_vocales:,}")
print(f"Cantidad de la vocal a: {vocal_a:,} \nCantidad de la vocal e: {vocal_e:,} \nCantidad de la vocal i: {vocal_i:,}")
print(f"Cantidad de la vocal o: {vocal_o:,} \nCantidad de la vocal u: {vocal_u:,}\n----------------------- ")
