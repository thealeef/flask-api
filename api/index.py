from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/")
def Inicio():
    return "API Funcionando"


@app.route("/funcionarios")
def funcionarios():
    # MOKANDO OS DADOS
    listaFuncionarios = [
        {"id": 1, "nomeCompleto": "Teste A", "nomeMae": "Mae Teste A"},
        {"id": 2, "nomeCompleto": "Teste B", "nomeMae": "Mae Teste B"},
        {"id": 3, "nomeCompleto": "Teste C", "nomeMae": "Mae Teste C"},
        {"id": 4, "nomeCompleto": "Teste D", "nomeMae": "Mae Teste D"},
    ]

    return listaFuncionarios
