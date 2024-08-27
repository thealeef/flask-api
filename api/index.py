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


# MOKANDO OS DADOS
funcionarios = [
    {"id": gerador_id(), "nomeCompleto": "Teste A", "nomeMae": "Mae Teste A"},
    {"id": gerador_id(), "nomeCompleto": "Teste B", "nomeMae": "Mae Teste B"},
    {"id": gerador_id(), "nomeCompleto": "Teste C", "nomeMae": "Mae Teste C"},
    {"id": gerador_id(), "nomeCompleto": "Teste D", "nomeMae": "Mae Teste D"},
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


if __name__ == "__main__":
    # debug=True permite que erros do Python apareçam na página da web.
    app.run(debug=True)
