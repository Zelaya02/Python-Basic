from flask import Flask, request, jsonify
from cliente import buscar_cliente

app = Flask(__name__)

@app.route('/cliente', methods=['POST'])
def cliente():
    data = request.get_json()
    ci = data.get("ci", None)
    
    if not ci:
        return jsonify({
            "accion": "Falta el campo ci",
            "codRes": "ERROR",
            "menRes": "Datos incompletos"
        }), 400
    
    resultado = buscar_cliente(ci)
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5003, debug=True)
