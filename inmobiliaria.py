### este es para ampliar el sistema con tablas y sus relaciones
import mysql.connector

class Inmobiliaria:
    def __init__(self, host, user, password,port, database):
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
            'operaciones': (
                ''' CREATE TABLE IF NOT EXISTS operaciones (
                    codigo_operacion INT AUTO_INCREMENT PRIMARY KEY,
                    descripcion VARCHAR(255)
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
            'imagenes': (
                ''' CREATE TABLE IF NOT EXISTS imagenes (
                    id_imagen INT AUTO_INCREMENT PRIMARY KEY,
                    imagen_url VARCHAR(255)
                )'''
            ),
            'inmuebles_imagenes': (
                ''' CREATE TABLE IF NOT EXISTS inmuebles_imagenes (
                    id_inmu_imag INT AUTO_INCREMENT PRIMARY KEY, 
                    id_imagen INT,
                    id_inmueble INT,
                    FOREIGN KEY (id_imagen) REFERENCES imagenes(id_imagen), 
                    FOREIGN KEY (id_inmueble) REFERENCES inmuebles(id_inmueble)
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
    
    # CRUD estado_inmuebles
    def agregar_estado_inmueble(self, codigo_estado):
    # Verificar si el estado existe
        self.conector.execute('SELECT COUNT(*) AS count FROM estados WHERE codigo_estado = %s', (codigo_estado,))
        if self.conector.fetchone()['count'] == 0:
            raise ValueError(f"El estado con codigo {codigo_estado} no existe.")
    
    # Insertar el registro en estado_inmuebles
        sql = 'INSERT INTO estado_inmuebles (codigo_estado) VALUES (%s)'
        valores = (codigo_estado,)
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
    
    def consultar_inmueble(self, id_inmueble):
        self.conector.execute(f"SELECT * FROM inmuebles WHERE id_inmueble = {id_inmueble}")
        return self.conector.fetchone()
    
    def modificar_inmueble(self, id_inmueble, mod_direccion, mod_localidad, mod_provincia, mod_codigo_precio, mod_codigo_operacion, mod_codigo_tipo_inmueble, mod_codigo_estado_inmueble, mod_descripcion):
        sql = "UPDATE inmuebles SET direccion=%s, localidad=%s, provincia=%s, codigo_precio=%s, codigo_operacion=%s, codigo_tipo_inmueble=%s, codigo_estado_inmueble=%s, descripcion=%s WHERE id_inmueble=%s"
        valores = (mod_direccion, mod_localidad, mod_provincia, mod_codigo_precio, mod_codigo_operacion, mod_codigo_tipo_inmueble, mod_codigo_estado_inmueble, mod_descripcion, id_inmueble)
        self.conector.execute(sql, valores)
        self.conn.commit()
        return self.conector.rowcount > 0
    
    def listar_inmuebles(self):
        self.conector.execute("SELECT * FROM inmuebles")
        inmuebles = self.conector.fetchall()
        return inmuebles

    def eliminar_inmueble(self, id_inmueble):
        self.conector.execute(f"DELETE FROM inmuebles WHERE id_inmueble = {id_inmueble}")
        self.conn.commit()
        return self.conector.rowcount > 0
    
    
    # CRUD DE IMAGENES
    def agregar_imagen(self, imagen_url):
        sql = 'INSERT INTO imagenes (imagen_url) VALUES (%s)'
        valores = (imagen_url,)  # Coma al final para definir una tupla de un solo elemento
        self.conector.execute(sql, valores)
        self.conn.commit()
        return self.conector.lastrowid

    # CRUD DE INMUEBLES_IMAGENES
    def agregar_inmueble_imagen(self, id_imagen, id_inmueble):
        # Verificar si la imagen existe
        self.conector.execute('SELECT COUNT(*) AS count FROM imagenes WHERE id_imagen = %s', (id_imagen,))
        if self.conector.fetchone()['count'] == 0:
            raise ValueError(f"La imagen con id {id_imagen} no existe.")
        
        # Verificar si el inmueble existe
        self.conector.execute('SELECT COUNT(*) AS count FROM inmuebles WHERE id_inmueble = %s', (id_inmueble,))
        if self.conector.fetchone()['count'] == 0:
            raise ValueError(f"El inmueble con id {id_inmueble} no existe.")
        
        # Insertar el registro en inmuebles_imagenes
        sql = 'INSERT INTO inmuebles_imagenes (id_imagen, id_inmueble) VALUES (%s, %s)'
        valores = (id_imagen, id_inmueble,)
        self.conector.execute(sql, valores)
        self.conn.commit()
        return self.conector.lastrowid

# Inicialización de la clase y ejecución de métodos CRUD
inmobiliaria = Inmobiliaria(host='localhost', user='root', password='', port=3307, database='inmobiliaria')
# inmueble = inmobiliaria.consultar_inmueble(1)
# print (inmueble)


# Agregar datos
# inmobiliaria.agregar_precio('Pesos', 50)
# inmobiliaria.agregar_tipo_inmueble('Departamento')
# inmobiliaria.agregar_estado('Baja')
# inmobiliaria.agregar_operacion('Alquiler')
# inmobiliaria.agregar_usuario('Anto', 'Torres', 30658425, '1234', 'anto@gmail.com')

# inmobiliaria.agregar_estado_inmueble(1)
# inmobiliaria.agregar_inmueble('Verdadera 456', 'otra Shelbyville', 'Provincia Real', 1, 1, 1, 1, 'Hermosa casa en venta ')
# inmobiliaria.agregar_imagen('casa2.jpg')
# inmobiliaria.agregar_inmueble_imagen(1, 1)  # Asegúrate de que estos IDs existan en las tablas correspondientes
