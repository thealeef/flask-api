from flask import Flask, json, request


app = Flask(__name__)

## OBS: Não colocar o CORs ele buga o vercel

# MOKANDO OS DADOS
listaFuncionarios = [
    {"id": "1", "nomeCompleto": "Teste A", "nomeMae": "Mae Teste A"},
    {"id": "2", "nomeCompleto": "Teste B", "nomeMae": "Mae Teste B"},
    {"id": "3", "nomeCompleto": "Teste C", "nomeMae": "Mae Teste C"},
    {"id": "4", "nomeCompleto": "Teste D", "nomeMae": "Mae Teste D"},
]


@app.route("/")
def Inicio():
    return "API Funcionando"


@app.route("/funcionarios", methods=["GET", "POST", "PUT", "DELETE"])
def metodo():

    # Tipo de requisição é mostrada
    print("Tipo do Método: ", request.method)

    if request.method == "GET":
        return chamaFuncionarios()

    if request.method == "POST":
        # Coleta os dados que vem da request, que no caso é mais um funcionário
        return addFuncionario(request.get_data())

    if request.method == "PUT":
        return metodoPUT()

    if request.method == "DELETE":
        return delFuncionario(request.get_json())


###############################################################################


def chamaFuncionarios():
    return listaFuncionarios


def addFuncionario(funcionario):

    # Carrega em Json
    funcionario = json.loads(funcionario)

    # Adicionamos ao dicionario da API
    listaFuncionarios.append(funcionario)

    return listaFuncionarios


def metodoPUT():
    obj = {"message": "Método PUT"}
    return obj


def delFuncionario(funcionario):

    # Carrega em Json

    listaFuncionarios.remove(funcionario)

    return listaFuncionarios


if __name__ == "__main__":
    # debug=True permite que erros do Python apareçam na página da web.
    app.run(debug=True)
