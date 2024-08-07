import json
from venta import Venta, VentaOnline, VentaLocal

class GestionVentas:
    def __init__(self):
        self.ventas = []

    def agregar_venta(self, venta):
        self.ventas.append(venta)

    def obtener_venta(self, cliente):
        for venta in self.ventas:
            if venta.cliente == cliente:
                return venta
        return None

    def actualizar_venta(self, cliente, fecha=None, productos=None):
        venta = self.obtener_venta(cliente)
        if venta:
            if fecha is not None:
                venta.fecha = fecha
            if productos is not None:
                venta.productos = productos

    def eliminar_venta(self, cliente):
        venta = self.obtener_venta(cliente)
        if venta:
            self.ventas.remove(venta)

    def listar_ventas(self):
        for venta in self.ventas:
            print(venta)

    def guardar_datos(self, filename):
        with open(filename, 'w') as file:
            json.dump([venta.__dict__ for venta in self.ventas], file)

    def cargar_datos(self, filename):
        try:
            with open(filename, 'r') as file:
                ventas_data = json.load(file)
                for venta_data in ventas_data:
                    if 'direccion_envio' in venta_data:
                        venta = VentaOnline(**venta_data)
                    elif 'tienda' in venta_data:
                        venta = VentaLocal(**venta_data)
                    else:
                        venta = Venta(**venta_data)
                    self.ventas.append(venta)
        except FileNotFoundError:
            print("Archivo no encontrado.")