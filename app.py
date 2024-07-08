
from flask import Flask, request, jsonify, render_template
# Instalar con pip install flask-cors
from flask_cors import CORS

# Instalar con pip install mysql-connector-python
import mysql.connector

# Si es necesario, pip install Werkzeug
from werkzeug.utils import secure_filename

# No es necesario instalar, es parte del sistema standard de Python
import os
import time

from inmobiliaria import Inmobiliaria

app = Flask(__name__)
CORS(app)

inmobiliaria = Inmobiliaria(host='localhost', user='root', password='', port=3307, database='inmobiliaria')


@app.route("/", methods=["GET"])
def index():
    inmuebles = inmobiliaria.listar_inmuebles()
    # return jsonify(inmuebles)
    return render_template('index.html', inmuebles=inmuebles)
@app.route("/inmuebles", methods=["GET"])
def adminPrincipal():
    inmuebles = inmobiliaria.listar_inmuebles()
    return jsonify(inmuebles)




if __name__ == "__main__":
    app.run(debug=True)