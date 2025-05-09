# 10. Simulación de un cajero automático (simplificado)
# Enunciado: Simula un cajero automático con un saldo inicial. Permite al usuario
# realizar depósitos (sumar al saldo) y retiros (restar del saldo) hasta que decida salir.
# Muestra el saldo actual en cada operación.
# Especificación: Usa un bucle while, un acumulador (para el saldo), y contadores
# (opcionales, para el número de depósitos/retiros). 

import os, time

os.system("cls || clear")
monto = float(input(f"Introduzca el deposito inicial \n-> "))
os.system("cls || clear")
print("¿Desea depositar, retirar o salir?")
operacion = input(f"-> ")
operacion = operacion.lower()

while operacion != "salir":
    if operacion == "depositar":
        os.system("cls || clear")
        deposito = float(input(f"Introduzca la cantidad que desea depositar \n-> "))
        monto1 = deposito + monto
        os.system("cls || clear")
        print(f"Monto actual = C${monto1:,.2f}")
        monto = monto1
    monto = monto
    if operacion == "retirar":
        os.system("cls || clear")
        retiro = float(input(f"Introduzca la cantidad que desea retirar \n-> "))
        monto2 = monto - retiro
        os.system("cls || clear")
        print(f"Monto actual = C${monto2:,.2f}")
        monto = monto2
    monto = monto
    time.sleep(5)
    os.system("cls || clear")
    print("¿Desea depositar, retirar o salir?")
    operacion = input(f"-> ")
    operacion = operacion.lower()

print(f" \nSalida del cajero automatico con exito \n")
