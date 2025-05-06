from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/Elegir")

# def Ejercicio_1():
#     return render_template("Ejercicio_1.html")

# @app.route("/Sumar", methods = ["Post"])

# def suma():
#     numero = 0
#     N = request.form.get("N")
#     N = int(N)
#     for i in range(0+1,N+1):
#         numero += i
#     resultado = f"{numero:,}"
#     return render_template("Ejercicio_1.html", resultado = resultado)

# def Ejercicio_2():
#     return render_template("Ejercicio_2.html")

# @app.route("/Producto", methods = ["Post"])

# def multiplicar():
#     acumulador = 0
#     contador = 0
#     acumulador1 = 1
#     M = request.form.get("M")
#     M = int(M)
#     while M > 0:
#         pares = M % 2
#         if pares == 0:
#             acumulador = M
#             acumulador1 = acumulador1 * acumulador
#             contador += 1
#         M -= 1
#     cantidad_pares = f"{contador:,}"
#     resultado = f"{acumulador1:,}"
#     return render_template("Ejercicio_2.html", resultado = resultado,cantidad_pares=cantidad_pares)

# def Ejercicio_3():
#     return render_template("Ejercicio_3.html")

# @app.route("/Vocales", methods = ["Post"])

# def contar_vocales():
#     vocales = ["a","e","i","o","u"]
#     contador = 0
#     cadena = request.form.get("cadena")

#     cadena = cadena.lower()
#     for i in cadena:
#         if i in vocales:
#             contador += 1

#     vocal_a = cadena.count("a")
#     vocal_e = cadena.count("e")
#     vocal_i = cadena.count("i")
#     vocal_o = cadena.count("o")
#     vocal_u = cadena.count("u")

#     total_vocales = f"{contador:,}"
#     vocal_a1 = f"a = {vocal_a:,}"
#     vocal_e1 = f"e = {vocal_e:,}"
#     vocal_i1 = f"i = {vocal_i:,}"
#     vocal_o1 = f"o = {vocal_o:,}"
#     vocal_u1 = f"u = {vocal_u:,}" 
#     return render_template("Ejercicio_3.html",total_vocales = total_vocales, vocal_a1 = vocal_a1, vocal_e1 = vocal_e1 , vocal_i1 = vocal_i1 , vocal_o1 = vocal_o1 , vocal_u1 = vocal_u1 )

def Ejercicio_4():
    return render_template("Ejercicio_4.html")

@app.route("/Calificando",methods = ["post"])

def promedio():
    return render_template("E_4.1.html")

app.route("/Promedio", methods = ["post"])

def promedio():
    
    cantidad_calificar = request.form.get("cantidad_a_calificar")
    nota = request.form.get("notas")
    notas = 0
    i = 0
    while i != cantidad_calificar:
        notas = int(nota) + notas
        i += 1	
        nota = request.form.get("notas")
        return render_template("E_4.1.html")     
    promedio = notas / i
    return render_template("E_4.2.html", promedio = promedio, notas = notas)

if __name__ == "__main__":
    app.run(debug = True)
