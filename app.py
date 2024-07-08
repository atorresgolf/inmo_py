
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

inmobiliaria = InmobiliariaAdmin(host='localhost', user='root', password='', port=3307,  database='inmobiliaria_admin')


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

@app.route('/inmuebles', methods=['GET'])
def listar_inmuebles():
    # Obtener los inmuebles de la base de datos
    inmuebles = inmobiliaria.listar_inmuebles()
    # Obtener las imagenes de la base de datos
    # imagenes = inmobiliaria.listar_imagenes()
    # Obtener las imagenes asociadas a cada inmueble
    # inmuebles_con_imagenes = []
    # for inmueble in inmuebles:
    #     inmueble_con_imagenes = inmueble.copy()
    #     inmueble_con_imagenes['imagenes'] = inmobiliaria.consultar_imagenes_inmueble()
    #     inmuebles_con_imagenes.append(inmueble_con_imagenes)
    #     return render_template('propiedades.html', inmuebles=inmuebles_con_imagenes)
    return jsonify(inmuebles)

#muestra un solo inmueble por su id_inmeuble 
#este metodo busca en la base de datos el inmueble con el id especificado y devuelve un json con los detalles del inmueble si lo encuentra o None si no o encuentra
@app.route('/inmuebles/<int:id_inmueble>', methods=['GET'])
def mostrar_inmueble(id_inmueble):
    # inmobiliaria.mostrar_inmueble(id_inmueble)
    inmueble = inmobiliaria.consultar_inmueble(id_inmueble)
    if inmueble:
        # print(inmueble)
        return jsonify(inmueble), 201
    else:
        return "Inmueble no encontrado", 404
    # imagenes = inmobiliaria.consultar_imagenes_inmueble(id_inmueble)
    # return jsonify(inmueble, imagenes)


@app.route('/inmuebles', methods=['POST'])
def agregar_inmueble():
    # id_inmueble = request.form['id_inmueble']
    direccion = request.form['direccion']
    localidad = request.form['localidad']
    provincia = request.form['provincia']
    moneda = request.form['moneda']
    precio = request.form['precio']
    tipo_inmueble = request.form['tipo_inmueble']
    estado = request.form['estado']
    descripcion = request.form['descripcion']
    
    nuevo_id_inmueble = inmobiliaria.agregar_inmueble( direccion, localidad, provincia, moneda, precio, tipo_inmueble, estado, descripcion)

    if nuevo_id_inmueble:
        return jsonify({"mensaje": "Inmueble agregado", "Id:": nuevo_id_inmueble }), 201
    else:
        return jsonify({"mensaje": "Error al agregar inmueble"}), 500
    
@app.route('/inmuebles/<int:id_inmueble>', methods=['PUT'])
def modificar_inmueble(id_inmueble):
    nueva_direccion = request.form.get('direccion')
    nueva_localidad = request.form.get('localidad')
    nueva_provincia = request.form.get('provincia')
    nueva_moneda = request.form.get('moneda')
    nuevo_precio = request.form.get('precio')
    nuevo_tipo_inmueble = request.form.get('tipo_inmueble')
    nuevo_estado = request.form.get('estado')
    nueva_descripcion = request.form.get('descripcion')
    #busco el inmueble guardado
    # inmueble = inmobiliaria.consultar_inmueble(id_inmueble)
    # if inmueble:
    #     inmueble.direccion = nueva_direccion
    if inmobiliaria.modificar_inmueble(id_inmueble, nueva_direccion, nueva_localidad, nueva_provincia, nueva_moneda, nuevo_precio, nuevo_tipo_inmueble, nuevo_estado , nueva_descripcion):
        return jsonify({"mensaje": "Inmueble modificado"}), 200
    else:
        return jsonify({"mensaje": "Inmueble no encontrado"}), 404
    
@app.route('/inmuebles/<int:id_inmueble>', methods = ['DELETE'])
def eliminar_inmueble(id_inmueble)  :
    inmueble = inmobiliaria.consultar_inmueble(id_inmueble)
    if inmueble:
        if inmobiliaria.eliminar_inmueble(id_inmueble):
            return jsonify({"mensaje": "Inmueble eliminado"}), 200
        else:
            return jsonify({"mensaje": "Error al eliminar el Inmueble"}), 500
    else:
        return jsonify({"mensaje": "Inmueble no encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True)