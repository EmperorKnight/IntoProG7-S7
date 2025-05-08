# 2. Producto de los primeros M números pares
# Enunciado: Pide al usuario un número entero positivo M y calcula el producto de los
# primeros M números pares.
# Especificación: Usa un bucle while, un acumulador (para el producto), y un contador
# (para los números pares).

import os 

os.system("cls || clear")
M = int(input(f"Introduzca un numero \n-> "))

contador = 1
contador_pares = 0
acumulador = 1

while contador < M:
    pares = contador % 2
    if pares == 0:
        contador_pares +=1
        acumulador *= contador
    contador += 1

os.system("cls || clear")
print(f" \n----------------------- \nEl total del producto de los numeros pares: {acumulador:,}\n----------------------- ")