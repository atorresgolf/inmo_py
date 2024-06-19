class Inmobiliaria:
    inmuebles=[]

    def agregar_inmueble(self,id_inmueble, direccion, localidad, provincia, codigo_precio, codigo_operacion, codigo_tipo_inmueble, codigo_estado_inmueble,descripcion):
        if self.consultar_inmueble(id_inmueble):
            return False
        nuevo_inmueble = {
            "id_inmueble": id_inmueble,
            "direccion": direccion,
            "localidad": localidad,
            "provincia": provincia,
            "codigo_precio": codigo_precio,
            "codigo_operacion": codigo_operacion,
            "codigo_tipo_inmueble": codigo_tipo_inmueble,
            'codigo_estado_inmueble': codigo_estado_inmueble,
            "descripcion" : descripcion
        }
        self.inmuebles.append(nuevo_inmueble)
        return True
    
    def consultar_inmueble(self,id_inmueble):
        for inmueble in self.inmuebles:
            if inmueble['id_inmueble'] == id_inmueble:
                return inmueble
        return False
    
    def modificar_inmueble(self, id_inmueble, direccion, localidad, provincia, codigo_precio, codigo_operacion, codigo_tipo_inmueble, codigo_estado_inmueble, descripcion ):
        for inmueble in self.inmuebles:
            if inmueble['id_inmueble'] == id_inmueble:
                inmueble['direccion'] = direccion
                inmueble['localidad'] = localidad
                inmueble['provincia'] = provincia
                inmueble['codigo_precio'] = codigo_precio
                inmueble['codigo_operacion'] = codigo_operacion
                inmueble['codigo_tipo_inmueble'] = codigo_tipo_inmueble
                inmueble['codigo_estado_inmueble'] = codigo_estado_inmueble
                inmueble['descripcion'] = descripcion
                return True
        return False
    
    def listar_inmuebles(self):
        print('-'*50)
        for inmueble in self.inmuebles:
            print(f'Id_inmueble.........: {inmueble['id_inmueble']}')
            print(f'Direccion...........: {inmueble['direccion']}')
            print(f'Localidad...........: {inmueble['localidad']}')
            print(f'Provincia...........: {inmueble['provincia']}')
            print(f'Codigo Precio.......: {inmueble['codigo_precio']}')
            print(f'Codigo Operacion....: {inmueble['codigo_operacion']}')
            print(f'Codigo Tipo Inmueble.: {inmueble['codigo_tipo_inmueble']}')
            print(f'Codigo Estado Inmueble: {inmueble['codigo_estado_inmueble']}')
            print(f'Descripcion...........: {inmueble['descripcion']}')
            print('-'*50)

    def eliminar_inmueble(self, id_inmueble):
        for inmueble in self.inmuebles:
            if inmueble['id_inmueble'] == id_inmueble:
                self.inmuebles.remove(inmueble)
                return True
        return False
    
    def mostrar_inmueble(self, id_inmueble):
        inmueble = self.consultar_inmueble(id_inmueble)
        if inmueble:
            print('-'*50)
            print(f'Id_inmueble.........: {inmueble["id_inmueble"]}')
            print(f'Direccion...........: {inmueble["direccion"]}')
            print(f'Localidad...........: {inmueble['localidad']}')
            print(f'Provincia...........: {inmueble['provincia']}')
            print(f'Codigo Precio.......: {inmueble['codigo_precio']}')
            print(f'Codigo Operacion....: {inmueble['codigo_operacion']}')
            print(f'Codigo Tipo Inmueble.: {inmueble['codigo_tipo_inmueble']}')
            print(f'Codigo Estado Inmueble: {inmueble['codigo_estado_inmueble']}')
            print(f'Descripcion...........: {inmueble['descripcion']}')
            print('-'*50)
        else:
            print('Inmueble no encontrado')

    # def __str__(self):
    #     return self.inmueble
                                                     
#Ejemplo del uso de las funciones implementadas

inmueble = Inmobiliaria()
inmueble.agregar_inmueble(1, 'Av.Solano Vera 1300', 'Yerba Buena', 'Tucuman', 'cod_pre_3', 'cod_ope_2', 'cod_tipo_1', 'cod_estado_5', 'casa en alquiler barrio cerrado')
inmueble.agregar_inmueble(2, 'Vera 1300', 'Yerba Buena', 'Tucuman', 'cod_pre_3', 'cod_ope_2', 'cod_tipo_1', 'cod_estado_5', 'casa en alquiler barrio cerrado')
inmueble.agregar_inmueble(3, 'Salta 1050', 'Yerba Buena', 'Tucuman', 'cod_pre_3', 'cod_ope_2', 'cod_tipo_1', 'cod_estado_5', 'casa en alquiler barrio cerrado')
print()
print('Listado de inmubles:')
inmueble.listar_inmuebles()
print()
print('Datos de un inmueble:')
inmueble.mostrar_inmueble(1)
#inmueble.eliminar_inmueble(2)
print()
print('Listado de inmubles:')
inmueble.listar_inmuebles()