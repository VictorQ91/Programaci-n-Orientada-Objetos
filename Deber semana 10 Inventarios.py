import os

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "cantidad": self.cantidad, "precio": self.precio}

    @staticmethod
    def from_dict(data):
        return Producto(data["id"], data["nombre"], data["cantidad"], data["precio"])


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_productos()

    def cargar_productos(self):
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, "r") as file:
                    for linea in file:
                        datos = linea.strip().split(',')
                        if len(datos) == 4:
                            id, nombre, cantidad, precio = datos
                            producto = Producto(id, nombre, int(cantidad), float(precio))
                            self.productos.append(producto)
            else:
                print(f"Archivo {self.archivo} no encontrado. Se creará un nuevo archivo al guardar productos.")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {self.archivo}.")
        except PermissionError:
            print(f"Error: Permiso denegado para leer el archivo {self.archivo}.")

    def guardar_productos(self):
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos:
                    file.write(f"{producto.get_id()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print(f"Error: Permiso denegado para escribir en el archivo {self.archivo}.")

    def añadir_producto(self, producto):
        if not any(p.get_id() == producto.get_id() for p in self.productos):
            self.productos.append(producto)
            self.guardar_productos()
            print("PRODUCTO AGREGADO EXITOSAMENTE")
        else:
            print(f"Error: Un producto con ID {producto.get_id()} ya existe.")

    def eliminar_producto(self, id):
        self.productos = [p for p in self.productos if p.get_id() != id]
        self.guardar_productos()

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                self.guardar_productos()
                return
        print(f"Error: Producto con ID {id} no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return resultados

    def mostrar_productos(self):
        for p in self.productos:
            print(p)


def menu():
    inventario = Inventario()

    while True:
        print("\nMenú de Gestión de Inventarios")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco si no se desea actualizar): ")
            precio = input("Nuevo precio (dejar en blanco si no se desea actualizar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, por favor intenta de nuevo.")


if __name__ == "__main__":
    menu()