
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

from inmobiliaria_admin import InmobiliariaAdmin

app = Flask(__name__)
CORS(app)

inmobiliaria = InmobiliariaAdmin(host='localhost', user='root', password='',  database='inmobiliaria_admin')


@app.route("/", methods=["GET"])
def index():
    inmuebles = inmobiliaria.listar_inmuebles()
    # return jsonify(inmuebles)
    return render_template('index.html', inmuebles=inmuebles)

@app.route('/propiedades')
def propiedades():
    return render_template('propiedades.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')


@app.route("/inmuebles", methods=["GET"])
def index_admin():
    inmuebles = inmobiliaria.listar_inmuebles()
    return jsonify(inmuebles)



if __name__ == "__main__":
    app.run(debug=True)