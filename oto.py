cantidad = 1
notas = 0
calificacion = int(input(f"Introduzca la cantidad de calificaciones a sumar \n-> "))
nota = int(input(f"Introduzca las notas \n-> "))
for i in range(1,calificacion):
    nota1 = int(input(f"-> "))
    nota = nota + nota1
    cantidad += 1
promedio = nota / cantidad
print(promedio)