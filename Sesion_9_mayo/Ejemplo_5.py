# Pedir una contraseña hasta que sea correcta

import os,time

# contraseña_guardad = "1234567890"
# intento = 1

# os.system("cls || clear")
# print(f"Intento {intento:,}")
# contraseña = input(f"Introduzca la contraseña \n-> ")

# while contraseña != contraseña_guardad:
#     if contraseña != contraseña_guardad:
#         print("Error, vuelva a intentarlo")
#     time.sleep(2)
#     os.system("cls || clear")
#     intento += 1
#     print(f"Intento {intento:,}")
#     contraseña = input(f"Introduzca la contraseña \n-> ")    

# print("Bienvenido")

contraseña_correcta = "12345"
intento = 0

while True:
    intento += 1
    os.system("cls || clear")
    print(f"Intento #{intento:,}")
    entrada = input(f"Escriba la contraseña \n-> ")

    if entrada == contraseña_correcta:
        print("La contraseña es correcta")
        break
    else:
        print("Vuelva a intentarlo")
        time.sleep(2)