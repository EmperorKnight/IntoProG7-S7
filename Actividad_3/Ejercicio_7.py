# 7. Suma de números pares e impares
# Enunciado: Pide al usuario una lista de números (pueden ser ingresados uno a la
# vez hasta que el usuario ingrese un valor de fin, como 0 o -1). Calcula la suma de
# los números pares y la suma de los números impares.
# Especificación: Usa un bucle while, acumuladores para la suma de pares e impares,
# y un contador (opcional, dependiendo de la implementación).

import os

os.system("cls || clear")
numeros = int(input(f"Introduzca una lista de numeros (terminara si introduce 0 o -1) \n-> "))

introducidos = []
pares = []
impar = []
suma_impares = 0
suma_pares = 0

if numeros == 0 or numeros == -1:
    print(f"Fin de la lista")
elif numeros > 0 and numeros > -1:
    while numeros > 0 and numeros > -1:
        introducidos.append(numeros)
        par = numeros % 2
        if par == 0:
            pares.append(numeros)
            suma_pares += numeros
        elif par != 0:
            impar.append(numeros) 
            suma_impares += numeros
        numeros = int(input("-> "))

    os.system("cls || clear")
    print(f"----------------------- \nLos numeros introducidos son {introducidos} ")
    print(F"----------------------- \nLos numeros pares introducidos fueron {pares} \nLos numeros impares introducidos fueron {impar}")
    print(f"----------------------- \nLa suma de los numeros pares en la lista es: {suma_pares:,}")
    print(f"La suma de los numeros impares en la lista es: {suma_impares:,} \n------------------------")

    