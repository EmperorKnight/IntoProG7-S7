# 1. Suma de los primeros N números
# Enunciado: Pide al usuario un número entero positivo N y calcula la suma de los
# números desde 1 hasta N.
# o Especificación: Usa un bucle for y un acumulador.
numero = 0

N = int(input(f"Introduzca el limite de la suma \n-> "))

for i in range(0+1,N+1):
    numero += i

print(f"La suma es: {numero:,}")