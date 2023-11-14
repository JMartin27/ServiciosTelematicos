import requests

# URL base de la API
base_url = "http://192.168.60.3:5000/books"

# Función para realizar una solicitud GET y obtener todos los libros
def get_books():
    response = requests.get(base_url)
    print("GET Request: Obtiene todos los libros")
    print(response.json())

# Función para realizar una solicitud POST y agregar un nuevo libro
def add_book(title, description, author):
    data = {
        "title": title,
        "description": description,
        "author": author
    }
    response = requests.post(base_url, json=data)
    print("POST Request: Agrega un nuevo libro")
    print(response.json())

# Función para realizar una solicitud PUT y actualizar un libro existente
def update_book(book_id, title, description, author):
    data = {
        "title": title,
        "description": description,
        "author": author
    }
    url = f"{base_url}/{book_id}"
    response = requests.put(url, json=data)
    print("PUT Request: Actualiza un libro existente")
    print(response.json())

# Función para realizar una solicitud DELETE y eliminar un libro
def delete_book(book_id):
    url = f"{base_url}/{book_id}"
    response = requests.delete(url)
    print("DELETE Request: Elimina un libro")
    print(response.json())

# Ejemplos de uso
get_books()

add_book("Nuevo Libro", "Descripción del Nuevo Libro", "Autor del Nuevo Libro")

get_books()

update_book(1, "Libro Actualizado", "Descripción Actualizada", "Autor Actualizado")

get_books()

delete_book(1)

get_books()
