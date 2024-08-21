from flask import Flask

app = Flask(__name__)


@app.route("/")
def Inicio():
    return "API Funcionando"


@app.route("/api")
def API():
    return "About"
