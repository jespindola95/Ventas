class Venta:
    def __init__(self, fecha, cliente, productos):
        self.fecha = fecha
        self.cliente = cliente
        self.productos = productos

    def __str__(self):
        return f"Venta(fecha={self.fecha}, cliente={self.cliente}, productos={self.productos})"

class VentaOnline(Venta):
    def __init__(self, fecha, cliente, productos, direccion_envio):
        super().__init__(fecha, cliente, productos)
        self.direccion_envio = direccion_envio

    def __str__(self):
        return f"VentaOnline(fecha={self.fecha}, cliente={self.cliente}, productos={self.productos}, direccion_envio={self.direccion_envio})"

class VentaLocal(Venta):
    def __init__(self, fecha, cliente, productos, tienda):
        super().__init__(fecha, cliente, productos)
        self.tienda = tienda

    def __str__(self):
        return f"VentaLocal(fecha={self.fecha}, cliente={self.cliente}, productos={self.productos}, tienda={self.tienda})"