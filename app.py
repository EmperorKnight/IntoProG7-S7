from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/Elegir")

def Ejercicio_1():
    return render_template("Ejercicio_1.html")

@app.route("/Sumar", methods = ["post"])

def sumar():
    numero = 0
    N = request.form.get("N")
    N = int(N)
    for i in range(0+1,N+1):
        numero += i
    resultado = f"{numero:,}"
    return render_template("Ejercicio_1.html", resultado = resultado)

if __name__ == "__main__":
    app.run(debug = True)
