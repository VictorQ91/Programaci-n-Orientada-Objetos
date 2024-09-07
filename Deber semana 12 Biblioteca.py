class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"'{self.titulo}' por {self.autor}, Categoría: {self.categoria}, ISBN: {self.isbn}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def listar_libros_prestados(self):
        return [str(libro) for libro in self.libros_prestados]


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario para libros disponibles: ISBN -> Libro
        self.usuarios = set()  # Conjunto para IDs de usuarios únicos
        self.usuario_dict = {}  # Diccionario para usuarios: ID de usuario -> Usuario

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]

    def registrar_usuario(self, nombre, id_usuario):
        if id_usuario not in self.usuario_dict:
            usuario = Usuario(nombre, id_usuario)
            self.usuarios.add(id_usuario)
            self.usuario_dict[id_usuario] = usuario

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuario_dict:
            usuario = self.usuario_dict.pop(id_usuario)
            self.usuarios.remove(id_usuario)
            # Devolver libros prestados al quitar un usuario (opcional)
            for libro in usuario.libros_prestados:
                self.libros[libro.isbn] = libro

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuario_dict and isbn in self.libros:
            usuario = self.usuario_dict[id_usuario]
            libro = self.libros.pop(isbn)
            usuario.prestar_libro(libro)

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuario_dict:
            usuario = self.usuario_dict[id_usuario]
            if isbn in self.libros:
                libro = self.libros[isbn]
                usuario.devolver_libro(libro)
                self.libros[isbn] = libro

    def buscar_libro(self, **kwargs):
        resultados = []
        for libro in self.libros.values():
            coincide = all(getattr(libro, k) == v for k, v in kwargs.items())
            if coincide:
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuario_dict:
            return self.usuario_dict[id_usuario].listar_libros_prestados()
        return []

# Ejemplo de uso

biblioteca = Biblioteca()

# Añadir libros
biblioteca.añadir_libro(Libro("El Quijote", "Miguel de Cervantes", "Novela", "001"))
biblioteca.añadir_libro(Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "002"))

# Registrar usuarios
biblioteca.registrar_usuario("Victor Quiroz", "Usuario1")
biblioteca.registrar_usuario("Karina Veliz", "Usuario2")

# Prestar libro
biblioteca.prestar_libro("Usuario1", "001")

# Listar libros prestados por un usuario
print("Libros prestados por Victor Quiroz:")
print(biblioteca.listar_libros_prestados("Usuario1"))

# Buscar libro por autor
print("Buscar libros por Gabriel García Márquez:")
for libro in biblioteca.buscar_libro(autor="Gabriel García Márquez"):
    print(libro)