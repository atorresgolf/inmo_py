import mysql.connector

class Inmobiliaria:
    def __init__(self, host, user, password, port, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=port,
            database=database
        )
        
        self.conector = self.conn.cursor(dictionary=True)
        self.__crear_tablas()

    def __crear_tablas(self):
        tablas = {
            'tipo_inmuebles': (
                ''' CREATE TABLE IF NOT EXISTS tipo_inmuebles (
                    codigo_tipo_inmueble INT AUTO_INCREMENT PRIMARY KEY,
                    descripcion VARCHAR(255) NOT NULL
                )'''
            ),
            'estados': (
                ''' CREATE TABLE IF NOT EXISTS estados (
                    codigo_estado INT AUTO_INCREMENT PRIMARY KEY,
                    descripcion VARCHAR(255)
                )'''
            ),
            'estado_inmuebles': (
                ''' CREATE TABLE IF NOT EXISTS estado_inmuebles (
                    codigo_estado_inmueble INT AUTO_INCREMENT PRIMARY KEY,
                    codigo_estado INT,
                    CONSTRAINT fk_estado FOREIGN KEY (codigo_estado) REFERENCES estados(codigo_estado)
                )'''
            ),
            'precios': (
                ''' CREATE TABLE IF NOT EXISTS precios (
                    codigo_precio INT AUTO_INCREMENT PRIMARY KEY,
                    moneda VARCHAR(10) NOT NULL,
                    valor DECIMAL(10,2)
                )'''
            ),
            'inmuebles': (
                ''' CREATE TABLE IF NOT EXISTS inmuebles (
                    id_inmueble INT AUTO_INCREMENT PRIMARY KEY,
                    direccion VARCHAR(255) NOT NULL,
                    localidad VARCHAR(50) NOT NULL,
                    provincia VARCHAR(50) NOT NULL,
                    codigo_precio INT,
                    codigo_operacion INT,
                    codigo_tipo_inmueble INT,
                    codigo_estado_inmueble INT,
                    descripcion VARCHAR(255),
                    FOREIGN KEY (codigo_precio) REFERENCES precios(codigo_precio),
                    FOREIGN KEY (codigo_operacion) REFERENCES operaciones(codigo_operacion),
                    FOREIGN KEY (codigo_tipo_inmueble) REFERENCES tipo_inmuebles(codigo_tipo_inmueble),
                    FOREIGN KEY (codigo_estado_inmueble) REFERENCES estado_inmuebles(codigo_estado_inmueble)
                )'''
            ),
            'usuarios': (
                ''' CREATE TABLE IF NOT EXISTS usuarios (
                    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    apellido VARCHAR(100) NOT NULL,
                    dni INT NOT NULL,
                    password VARCHAR(100) NOT NULL,
                    email VARCHAR(100) NOT NULL
                )'''
            ),
            'operaciones': (
                ''' CREATE TABLE IF NOT EXISTS operaciones (
                    codigo_operacion INT AUTO_INCREMENT PRIMARY KEY,
                    descripcion VARCHAR(255)
                )'''
            )
        }

        for nombre_tabla in tablas:
            tabla_sql = tablas[nombre_tabla]
            print(f"Creando tabla {nombre_tabla}: {tabla_sql}")
            self.conector.execute(tabla_sql)
        
        self.conn.commit()

    # CRUD TIPO_INMUEBLES
    def agregar_tipo_inmueble(self, descripcion):
        sql = "INSERT INTO tipo_inmuebles (descripcion) VALUES (%s)"
        valores = (descripcion,)
        self.conector.execute(sql, valores)
        self.conn.commit()
        return self.conector.lastrowid

    # CRUD ESTADOS
    def agregar_estado(self, descripcion):
        sql = "INSERT INTO estados (descripcion) VALUES (%s)"
        valores = (descripcion,)
        self.conector.execute(sql, valores)
        self.conn.commit()
        return self.conector.lastrowid

    # CRUD DE PRECIOS
    def agregar_precio(self, moneda, valor):
        sql = "INSERT INTO precios (moneda, valor) VALUES (%s, %s)"
        valores = (moneda, valor)
        self.conector.execute(sql, valores)
        self.conn.commit()
        return self.conector.lastrowid

    # CRUD OPERACIONES
    def agregar_operacion(self, descripcion):
        sql = "INSERT INTO operaciones (descripcion) VALUES (%s)"
        valores = (descripcion,)
        self.conector.execute(sql, valores)
        self.conn.commit()
        return self.conector.lastrowid

    # CRUD USUARIOS
    def agregar_usuario(self, nombre, apellido, dni, password, email):
        sql = "INSERT INTO usuarios (nombre, apellido, dni, password, email) VALUES (%s, %s, %s, %s, %s)"
        valores = (nombre, apellido, dni, password, email)
        self.conector.execute(sql, valores)
        self.conn.commit()
        return self.conector.lastrowid

    # CRUD DE INMUEBLES
    def agregar_inmueble(self, direccion, localidad, provincia, codigo_precio, codigo_operacion, codigo_tipo_inmueble, codigo_estado_inmueble, descripcion):
        sql = "INSERT INTO inmuebles (direccion, localidad, provincia, codigo_precio, codigo_operacion, codigo_tipo_inmueble, codigo_estado_inmueble, descripcion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (direccion, localidad, provincia, codigo_precio, codigo_operacion, codigo_tipo_inmueble, codigo_estado_inmueble, descripcion)
        self.conector.execute(sql, valores)
        self.conn.commit()
        return self.conector.lastrowid

# Inicialización de la clase y ejecución de métodos CRUD
inmobiliaria = Inmobiliaria(host='localhost', user='root', password='', port=3307, database='inmobiliaria')

# Agregar datos
inmobiliaria.agregar_precio('Dolares', 50)
inmobiliaria.agregar_tipo_inmueble('Casa')
inmobiliaria.agregar_estado('Activa')
inmobiliaria.agregar_operacion('Venta')
inmobiliaria.agregar_usuario('Anto', 'Torres', 30658425, 'anto@gmail.com', '1234')
