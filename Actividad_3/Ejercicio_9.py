# 9. Calcular la frecuencia de cada dígito en un número
# Enunciado: Pide al usuario un número entero y calcula cuántas veces aparece cada
# dígito (0 al 9) en el número.
# Especificación: Usa un bucle while y un array/list de contadores (uno para cada
# dígito).

import os

os.system("cls || clear")
numero = input(f"Introduzca un numero \n-> ")

n0 = 0
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0
n7 = 0
n8 = 0
n9 = 0

for i in numero:
    if i == "0":
        n0 += 1
    elif i == "1":
        n1 += 1
    elif i == "2":
        n2 += 1
    elif i == "3":
        n3 += 1
    elif i == "4":
        n4 += 1
    elif i == "5":
        n5 += 1
    elif i == "6":
        n6 += 1
    elif i == "7":
        n7 += 1
    elif i == "8":
        n8 += 1
    elif i == "9":
        n9 += 1

print(f"----------------------- \nEl numero 0 aparece {n0:,} \nEl numero 1 aparece {n1:,} \nEl numero 2 aparece {n2:,}")
print(f"El numero 3 aparece {n3:,} \nEl numero 4 aparece {n4:,} \nEl numero 5 aparece {n5:,} \nEl numero 6 aparece {n6:,}")
print(f"El numero 7 aparece {n7:,} \nEl numero 8 aparece {n8:,} \nEl numero 9 aparece {n9:,} \n-----------------------")

