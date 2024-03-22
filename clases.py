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

class Empleado:
    def __init__(self, nombre, apellido, dni, sueldo):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.sueldo = sueldo
        self.comision = 0

    def vender_articulo(self):
        self.comision = self.calcular_comision(self.precio)
       
    
    def calcular_comision(self):
        self.comision = self.sueldo * 0.10
        return self.comision
    
class Coordinador(Empleado):
    def __init__(self, nombre, apellido, dni, sueldo):
        super().__init__(nombre, apellido, dni, sueldo)
        self.comision = 0

    def coordinar_trabajo(self):
        print("Estoy coordinando el trabajo")

class Empleado_mostrador(Empleado):
    def __init__(self, nombre, apellido, dni, sueldo):
        super().__init__(nombre, apellido, dni, sueldo)
        self.comision = 0
        self.caja = 0
    
    def cobrar(self):
        self.caja += self.sueldo 
        
    
class Empleado_repositor(Empleado):
    def __init__(self, nombre, apellido, dni, sueldo):
        super().__init__(nombre, apellido, dni, sueldo)
        self.comision = 0

    def ir_deposito_mercaderia(self):
        print("Estoy yendo al deposito de mercaderias")