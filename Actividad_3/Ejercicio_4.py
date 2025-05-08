import datetime as dt
import os

fecha = dt.date.today()
os.system("cls || clear")
print(f"Fecha actual: {fecha}")

cant = int(input(f"Introduzca la cantidad de notas a calificar \n-> "))

suma = 0

for i in range(cant):
    notas = int(input(f"Introduzca la nota {i+1}: "))
    suma += notas

promedio = suma / cant

os.system("cls || clear")
print(f"----------------------- \nEl promedio es: {promedio:.1f}\n----------------------- ")

