# Mostrar la tabla de multiplicar de un numero

import os

os.system("cls || clear")

numero = int(input(f"Introduzca el numero de la tabla que desea conocer \n-> "))

print(f"\nTabla de {numero:,}")
for i in range(1,13):
    print(f"{numero:,} * {i} = {numero*i:,}")