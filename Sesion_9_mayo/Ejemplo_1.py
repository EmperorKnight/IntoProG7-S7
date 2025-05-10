# Sumar los primeros 10 numeros naturales usando la sentencia for

import os

suma = 0
expresion = ""

os.system("cls || clear")

for i in range(1,11):
    suma += i
    expresion += str(i)
    if i < 10:
        expresion += "+"
    print(f"Suma parcial despues de agregar {i}: {suma}")

print(f"\nExpresion: {expresion} = {suma}")
# os.system("cls || clear")
# print("El resultado de sumar los primeros dies numeros naturales son: ",suma)