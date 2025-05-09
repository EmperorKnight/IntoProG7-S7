# 6. Contar palabras en una frase
# Enunciado: Pide al usuario una frase y cuenta el número de palabras que contiene.
# Especificación: Usa un bucle for (o métodos de string) y un contador. 

import os

os.system("cls || clear")
frase = input(f"Introduzca una frase cualquiera \n-> ")

adornos =["!","@","#","$","%","%","^","&","*","(",")","_","-","=","{","}","[","]",":",";",",","'","<",".",">","?","¿","/","|","-","1","2","3","4","5","6","7","8","9","0","¡","~","`","≥","≤"," "]

contador = 0

for i in frase:
    contador += 1
    if i in adornos:
        contador -= 1

os.system("cls || clear")
print(f"-----------------------\nEl total de palabras en la frase '{frase}' es de {contador:,} palabras\n-----------------------")
