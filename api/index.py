from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def Inicio():
    return "API Funcionando"


@app.route("/funcionarios", methods=["GET", "POST", "PUT", "DELETE"])
def metodo():

    # Tipo de requisição é mostrada
    print("Tipo do Método: ", request.method)

    tipoMetodo = request.method

    if request.method == "GET":
        return chamaFuncionarios()

    if request.method == "POST":
        return addFuncionario()

    if request.method == "PUT":
        return metodoPUT()

    if request.method == "DELETE":
        return delFuncionario()


###############################################################################


def chamaFuncionarios():
    # MOKANDO OS DADOS
    listaFuncionarios = [
        {"id": 1, "nomeCompleto": "Teste A", "nomeMae": "Mae Teste A"},
        {"id": 2, "nomeCompleto": "Teste B", "nomeMae": "Mae Teste B"},
        {"id": 3, "nomeCompleto": "Teste C", "nomeMae": "Mae Teste C"},
        {"id": 4, "nomeCompleto": "Teste D", "nomeMae": "Mae Teste D"},
    ]

    return listaFuncionarios


def addFuncionario():
    obj = {"message": "Funcionario Adicionado"}
    return obj


def metodoPUT():
    obj = {"message": "Método PUT"}
    return obj


def delFuncionario():
    obj = {"message": "Funcionario Deletado"}
    return obj


if __name__ == "__main__":
    # debug=True permite que erros do Python apareçam na página da web.
    app.run(debug=True)
