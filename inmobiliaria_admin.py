import mysql.connector

class InmobiliariaAdmin:
    def __init__(self, host, user, password,  database ):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
           
             )
        
        self.conector = self.conn.cursor()

        # Intentamos seleccionar la base de datos
        try:
            self.conector.execute(f"USE {database}")
        except mysql.connector.Error as err:
            # Si la base de datos no existe, la creamos
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.conector.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err
                    
        self.__crear_tablas()



    def __crear_tablas(self):
        tablas = {
                 'inmuebles': (
                ''' CREATE TABLE IF NOT EXISTS inmuebles (
                    id_inmueble INT AUTO_INCREMENT PRIMARY KEY,
                    direccion VARCHAR(255) NOT NULL,
                    localidad VARCHAR(50) NOT NULL,
                    provincia VARCHAR(50) NOT NULL,
                    moneda VARCHAR(10) ,
                    precio INT(20) NOT NULL,
                    tipo_inmueble VARCHAR(255),
                    estado VARCHAR(255),
                    descripcion VARCHAR(255)
                    
                )'''
            )
           
        }

        for nombre_tabla in tablas:
            tabla_sql = tablas[nombre_tabla]
            print(f"Creando tabla {nombre_tabla}: {tabla_sql}")
            self.conector.execute(tabla_sql)
        
        self.conn.commit()
        # Cerrar el cursor inicial y abrir uno nuevo con el parámetro dictionary=True
        self.conector.close()
        self.conector = self.conn.cursor(dictionary=True)


    
    # CRUD DE INMUEBLES
    def agregar_inmueble(self, direccion, localidad, provincia, moneda, precio, tipo_inmueble, estado, descripcion):
        sql = "INSERT INTO inmuebles (direccion, localidad, provincia, moneda, precio, tipo_inmueble, estado, descripcion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (direccion, localidad, provincia, moneda, precio, tipo_inmueble, estado, descripcion)
        self.conector.execute(sql, valores)
        self.conn.commit()
        return self.conector.lastrowid
    
    def consultar_inmueble(self, id_inmueble):
        self.conector.execute(f"SELECT * FROM inmuebles WHERE id_inmueble = {id_inmueble}")
        return self.conector.fetchone()
    
    def modificar_inmueble(self, id_inmueble, mod_direccion, mod_localidad, mod_provincia, mod_moneda, mod_precio, mod_tipo_inmueble, mod_estado, mod_descripcion):
        sql = "UPDATE inmuebles SET direccion=%s, localidad=%s, provincia=%s, moneda=%s, precio=%s, tipo_inmueble=%s, estado=%s, descripcion=%s WHERE id_inmueble=%s"
        valores = (mod_direccion, mod_localidad, mod_provincia, mod_moneda, mod_precio, mod_tipo_inmueble, mod_estado, mod_descripcion, id_inmueble)
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
    
    
    
# Inicialización de la clase y ejecución de métodos CRUD
inmobiliaria = InmobiliariaAdmin(host='localhost', user='root', password='', database='inmobiliaria_admin')
# inmueble = inmobiliaria.consultar_inmueble(1)
# print (inmueble)


# Agregar datos
# inmobiliaria.agregar_precio('Pesos', 50)
# inmobiliaria.agregar_tipo_inmueble('Departamento')
# inmobiliaria.agregar_estado('Baja')
# inmobiliaria.agregar_operacion('Alquiler')
# inmobiliaria.agregar_usuario('Anto', 'Torres', 30658425, '1234', 'anto@gmail.com')

# inmobiliaria.agregar_estado_inmueble(1)
# inmobiliaria.agregar_inmueble('Verdadera 456', 'Shelbyville', 'Provincia Real', 'Pesos', 10000, 'Casa', 'Venta', 'Hermosa casa en venta ')
# inmobiliaria.agregar_inmueble('Solano 34', 'Capital', 'Cordoba', 'Pesos', 1000, 'Casa', 'Alquiler', 'Hermosa casa en alquiler ')
# inmobiliaria.agregar_inmueble('Colon 560', 'Capital', 'Mendoza', 'Dolares', 5000, 'Casa', 'Venta', 'Hermosa casa en venta ')
# inmobiliaria.agregar_inmueble('Laprida 636', 'Capital', 'Tucuman', 'Dolares', 3000, 'Departamento', 'Alquiler', 'Hermoso departamento en alquiler ')

