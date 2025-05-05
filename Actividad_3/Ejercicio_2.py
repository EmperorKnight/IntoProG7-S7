# 2. Producto de los primeros M números pares
# Enunciado: Pide al usuario un número entero positivo M y calcula el producto de los
# primeros M números pares.
# Especificación: Usa un bucle while, un acumulador (para el producto), y un contador
# (para los números pares).

acumulador = 0
numero = 0

M = int(input(f"Introduzca un numero \n-> "))

while M > 0:
    contador = M % 2
    if contador == 0:
        acumulador  
    else:
        M -= 1

acumulador = contador

print(acumulador)

