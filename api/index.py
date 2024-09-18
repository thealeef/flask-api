from flask import Flask, jsonify, request

app = Flask(__name__)

## OBS: Não colocar o CORs ele buga o vercel

contador_id = 1


# Gerador de IDs
def gerador_id():
    global contador_id
    novo_id = contador_id
    contador_id += 1
    return novo_id


# Funcionarios Cód:
# 0 = Desligado
# 1 = Ativo
# 2 = Afastado
# 3 = Férias

# MOKANDO OS DADOS
funcionarios = [
    {
        "id": gerador_id(),
        "nomeCompleto": "Rivelino Oliveira",
        "nomeMae": "Maria Oliveira",
        "status": 1,
        "cargo": "gerente",
    },
    {
        "id": gerador_id(),
        "nomeCompleto": "Henrique Bastos",
        "nomeMae": "Marcia Bastos",
        "status": 1,
        "cargo": "coordernador",
    },
    {
        "id": gerador_id(),
        "nomeCompleto": "Felipe Henrique de Sousa",
        "nomeMae": "Cristina de Sousa",
        "status": 1,
        "cargo": "auxiliar",
    },
    {
        "id": gerador_id(),
        "nomeCompleto": "Adalberto Queiroz",
        "nomeMae": "Leticia Queiroz",
        "status": 2,
        "cargo": "auxiliar",
    },
    {
        "id": gerador_id(),
        "nomeCompleto": "Cris Figueira",
        "nomeMae": "Laura Figueira",
        "status": 3,
        "cargo": "analista",
    },
    {
        "id": gerador_id(),
        "nomeCompleto": "Alef Rib",
        "nomeMae": "Eli de Sousa",
        "status": 3,
        "cargo": "analista",
    },
    {
        "id": gerador_id(),
        "nomeCompleto": "Alonso Riquelme",
        "nomeMae": "Maria Riquelme",
        "status": 0,
        "cargo": "analista",
    },
]


# Rota GET para obter todos os usuários
@app.route("/funcionarios", methods=["GET"])
def chama_funcionarios():
    return jsonify(funcionarios)


# Adiciona um funcionario com metodo POST
@app.route("/funcionarios", methods=["POST"])
def add_funcionario():
    global funcionarios

    novo_funcionario = request.json

    if novo_funcionario in funcionarios:
        print("tem repitido")
        jsonify({"erro": "Funcionario já cadastrado"})
    else:
        novo_funcionario["id"] = gerador_id()
        funcionarios.append(novo_funcionario)

    return jsonify(funcionarios), 201


# Rota GET para obter um único usuário pelo ID
@app.route("/funcionarios/<int:id>", methods=["GET"])
def chama_funcionario(id):
    funcionario = next((f for f in funcionarios if f["id"] == id), None)

    if funcionario:
        return jsonify(funcionario)
    else:
        return jsonify({"erro": "Funcionario nao encontrado"}), 404


# Rota DELETE para excluir um usuário pelo ID
@app.route("/funcionarios/<int:id>", methods=["DELETE"])
def deletar_funcionario(id):
    global funcionarios

    # Filtra os itens, removendo aquele com o ID correspondente
    funcionarios = [f for f in funcionarios if f["id"] != id]
    return jsonify({"message": "Item deletado com sucesso"}), 200


@app.route("/funcionarios/<int:id>", methods=["PUT"])
def edit_funcionario(id):

    print(id)

    # Localizar o funcionário pelo ID
    funcionario = next((f for f in funcionarios if f["id"] == id), None)

    if not funcionario:
        return jsonify({"error": "Funcionário não encontrado"}), 404

    # Obter os dados JSON da requisição
    data = request.get_json()

    # Atualizar os campos do funcionário
    funcionario["nomeCompleto"] = data.get("nomeCompleto", funcionario["nomeCompleto"])
    funcionario["nomeMae"] = data.get("nomeMae", funcionario["nomeMae"])

    return jsonify(funcionario), 200


if __name__ == "__main__":
    # debug=True permite que erros do Python apareçam na página da web.
    app.run(debug=True)
