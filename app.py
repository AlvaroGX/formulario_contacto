from flask import Flask, render_template, request
import modelo

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predecir', methods=["POST"])
def predecir():
    habitaciones = int(request.form["habitaciones"])
    superficie = float(request.form["superficie"])
    ubicacion = request.form["ubicacion"]

    precio = modelo.predecir(habitaciones, superficie, ubicacion)
    return render_template("predecir.html", precio=precio)

if __name__ == "__main__":
    app.run(debug=True)