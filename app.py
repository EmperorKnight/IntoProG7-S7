from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def index():
    msn = ""
    for num in range(1,11):
        msn += str(num)
    return render_template("index.html", msn = msn)

if __name__ == "__main__":
    app.run(debug = True)

