class Producto():
    def _init_(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Vajilla(Producto):
    def _init_(self, nombre, precio, material):
        super()._init_(nombre, precio)
        self.material = material
        
class Juguete(Producto):
    def _init_(self, nombre, precio, edadRecomendad):
        super()._init_(nombre, precio)
        self.edadRecomendad = edadRecomendad

class ArtJardin(Producto):
    def _init_(self, nombre, precio, usoProfesional):
        super()._init_(nombre, precio)
        self.usoProfesional = usoProfesional

class Empleado():
    def _init_(self, nombre, apellido, dni, sueldo, comision):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.sueldo = sueldo
        self.comision = comision
        
    def venderProducto(self, objectProducto):
        self.comision = self.comision + objectProducto.precio * 0.1
        
        
class Cordinador(Empleado):
    def _init_(self, nombre, apellido, dni, sueldo, comision):
        super()._init_(nombre, apellido, dni, sueldo, comision)
        
    def Coordinar(self):
        print("Estoy cordinando")
    
class Mostrador(Empleado):
    def _init_(self, nombre, apellido, dni, sueldo, comision, caja):
        super()._init_(nombre, apellido, dni, sueldo, comision)
        self.caja = caja
        
    def cobrar(self, objectProducto):
        self.caja = self.caja + objectProducto.precio
    
class Repositor(Empleado):
    def _init_(self, nombre, apellido, dni, sueldo, comision):
        super()._init_(nombre, apellido, dni, sueldo, comision)
        
    def irDeposito(self):
        print("Estoy yendo al deposito")