from gestion_ventas import GestionVentas
from venta import VentaOnline, VentaLocal

def main():
    gestion_ventas = GestionVentas()

    while True:
        print("\n1. Agregar venta")
        print("2. Listar ventas")
        print("3. Actualizar venta")
        print("4. Eliminar venta")
        print("5. Guardar datos")
        print("6. Cargar datos")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == '1':
                tipo = input("Tipo de venta (online/local): ")
                fecha = input("Fecha: ")
                cliente = input("Cliente: ")
                productos = input("Productos (separados por coma): ").split(',')

                if tipo == 'online':
                    direccion_envio = input("Dirección de envío: ")
                    venta = VentaOnline(fecha, cliente, productos, direccion_envio)
                elif tipo == 'local':
                    tienda = input("Tienda: ")
                    venta = VentaLocal(fecha, cliente, productos, tienda)
                else:
                    print("Tipo de venta no válido.")
                    continue

                gestion_ventas.agregar_venta(venta)

            elif opcion == '2':
                gestion_ventas.listar_ventas()

            elif opcion == '3':
                cliente = input("Cliente de la venta a actualizar: ")
                fecha = input("Nueva fecha (presione enter para dejar igual): ")
                productos = input("Nuevos productos (presione enter para dejar igual, separados por coma): ")
                productos = productos.split(',') if productos else None

                gestion_ventas.actualizar_venta(
                    cliente,
                    fecha=fecha if fecha else None,
                    productos=productos
                )

            elif opcion == '4':
                cliente = input("Cliente de la venta a eliminar: ")
                gestion_ventas.eliminar_venta(cliente)

            elif opcion == '5':
                filename = input("Nombre del archivo para guardar: ")
                gestion_ventas.guardar_datos(filename)

            elif opcion == '6':
                filename = input("Nombre del archivo para cargar: ")
                gestion_ventas.cargar_datos(filename)

            elif opcion == '7':
                break

            else:
                print("Opción no válida. Por favor, intente de nuevo.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()