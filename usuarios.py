### Usuario usando como diccionario
# no se usa ahora
class Usuario:
    usuarios=[]

    def agregar_usuario(self,id_usuario, nombre, apellido, dni, email, contrasenia):
        if self.consultar_usuario(id_usuario):
            return False
        nuevo_usuario = {
            "id_usuario": id_usuario,
            "nombre": nombre,
            "apellido": apellido,
            "dni": dni,
            "email": email,
            "contrasenia": contrasenia,
           
        }
        self.usuarios.append(nuevo_usuario)
        return True
    
    def consultar_usuario(self,id_usuario):
        for usuario in self.usuarios:
            if usuario['id_usuario'] == id_usuario:
                return usuario
        return False
    
    def modificar_usuario(self,id_usuario, nombre, apellido, dni, email, contrasenia):
        for usuario in self.usuarios:
            if usuario['id_usuario'] == id_usuario:
                usuario['nombre'] = nombre
                usuario['apellido'] = apellido
                usuario['dni'] = dni
                usuario['email'] = email
                usuario['contrasenia'] = contrasenia
                
                return True
        return False