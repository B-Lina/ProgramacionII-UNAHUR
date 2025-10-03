"""
class BarUnahur:
    def __init__(self,cliente,compra,cantidad,total=0):
        self.cliente = cliente
        self.compra = compra
        self.cantidad = cantidad
        self.total = total

    def ingresarCompra(self):
        if self.cliente == "Estudiante":
            self.compra = 2000
            self.total = self.compra * self.cantidad
        elif self.cliente == "Docente":
            self.compra = 3000
            self.total = self.compra * self.cantidad
        elif self.cliente == "General":
            self.compra = 4000
            self.total = self.compra * self.cantidad
        
        return self.total
    def mostrarCompra(self):
        return f"Cliente: {self.cliente}\nValor del producto: {self.compra}\nCantidad: {self.cantidad}\nTotal a pagar: {self.total}"
    
    def contarCompras(self):
        return f"Cantidad de productos comprados: {self.cantidad} \nTotal a pagar: {self.total}"        
    
    def __str__(self):
        return f"Cliente: {self.cliente} - Valor del producto: {self.compra} - Cantidad: {self.cantidad} - Total a pagar: {self.total}"

compras1 = BarUnahur("Estudiante",0,3)
compras1.ingresarCompra()
print(compras1.mostrarCompra())


class Bar:
    def __init__(self, nombre:str):
        # Nombre del bar
        self.__nombre = nombre
        # Variables internas que siempre empiezan en cero
        self.__recaudacion = 0.0
        self.__ventasEstudiante = 0
        self.__ventasDocente = 0
        self.__ventasGeneral = 0

    # Registrar pedido de menú
    def pedirMenu(self, tipo:str, cantidad:int=1):
        if tipo == "Estudiante":
            precio = 2000
            self.__ventasEstudiante += cantidad
        elif tipo == "Docente":
            precio = 3000
            self.__ventasDocente += cantidad
        elif tipo == "General":
            precio = 4000
            self.__ventasGeneral += cantidad
        else:
            raise ValueError("Tipo de menú inválido")

        self.__recaudacion += precio * cantidad

    # Saber lo recaudado
    def obtenerRecaudacion(self):
        return self.__recaudacion

    # Resetear cuentas
    def resetear(self):
        self.__recaudacion = 0.0
        self.__ventasEstudiante = 0
        self.__ventasDocente = 0
        self.__ventasGeneral = 0

    # Contar ventas
    def contarVentas(self):
        return {
            "Estudiante": self.__ventasEstudiante,
            "Docente": self.__ventasDocente,
            "General": self.__ventasGeneral,
            "Total": self.__ventasEstudiante + self.__ventasDocente + self.__ventasGeneral
        }

    # Cambiar nombre del bar
    def cambiarNombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # Representación del objeto
    def __str__(self)->str:
        return f"{self.__nombre} recaudación ${self.__recaudacion}"

bar = Bar("UnaHur")
estudiante1 = bar.pedirMenu("Estudiante", 1) 
estudiante2 = bar.pedirMenu("Estudiante", 1) 
bar.pedirMenu("Docente", 1)     

print(bar)  # 👉 UnaHur recaudación $13000.0
print("Recaudación total:", bar.obtenerRecaudacion())  
print("Detalle ventas:", bar.contarVentas())  

bar.resetear()
print(bar)  # 👉 UnaHur recaudación $0.0

"""
class BarUnahur:
    total_ventas = 0  # Class attribute to track total sales

    def __init__(self, cliente, compra, cantidad, total=0):
        self.cliente = cliente
        self.compra = compra
        self.cantidad = cantidad
        self.total = total

    def ingresarCompra(self):
        if self.cliente.lower() == "estudiante":
            self.compra = 2000
        elif self.cliente.lower() == "docente":
            self.compra = 3000
        elif self.cliente.lower() == "general":
            self.compra = 4000
        
        self.total = self.compra * self.cantidad
        BarUnahur.total_ventas += self.total  # Add the current sale to the total
        return self.total

    def mostrarCompra(self):
        return f"Cliente: {self.cliente}\nValor del producto: {self.compra}\nCantidad: {self.cantidad}\nTotal a pagar: {self.total}"

    def __str__(self):
        return f"Cliente: {self.cliente} - Valor del producto: {self.compra} - Cantidad: {self.cantidad} - Total a pagar: {self.total}"

    # New methods
    def ventasTotales(self):
        return f"Ventas totales: {BarUnahur.total_ventas}"

    def limpiar_ventas(self):
        BarUnahur.total_ventas = 0
        return "Ventas totales reiniciadas."

# Example usage with the new methods
compras1 = BarUnahur("EstudiantE", 0, 2)
compras1.ingresarCompra()
print(compras1.mostrarCompra())
#print(compras1.ventasTotales())

print("---")

compras2 = BarUnahur("Docente", 0, 3)
compras2.ingresarCompra()
#print(compras2.mostrarCompra())
print(compras2.ventasTotales())

print("---")

print(BarUnahur.ventasTotales(None))  # Accessing the class method through the class itself
BarUnahur.limpiar_ventas(None)            # Resetting the total sales
print(BarUnahur.ventasTotales(None))