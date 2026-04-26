import requests
import csv
import json

def procesar_api():
    url = "https://jsonplaceholder.typicode.com/users"
    respuesta = requests.get(url)
    usuarios = respuesta.json()

    print(f"Usuarios obtenidos: {len(usuarios)}")

    nombres_esp = [
        "Carlos Ramírez", "María López", "Andrés García",
        "Lucía Martínez", "Jorge Hernández", "Valentina Torres",
        "Sebastián Flores", "Daniela Rojas", "Felipe Morales",
        "Camila Jiménez"
    ]

    usuarios_esp = [
        "carlos_r", "maria_l", "andres_g",
        "lucia_m", "jorge_h", "valentina_t",
        "sebastian_f", "daniela_r", "felipe_m",
        "camila_j"
    ]

    correos_esp = [
        "carlos.ramirez@gmail.com", "maria.lopez@hotmail.com",
        "andres.garcia@yahoo.com", "lucia.martinez@gmail.com",
        "jorge.hernandez@outlook.com", "valentina.torres@gmail.com",
        "sebastian.flores@hotmail.com", "daniela.rojas@yahoo.com",
        "felipe.morales@gmail.com", "camila.jimenez@outlook.com"
    ]

    ciudades_esp = [
        "Bogotá", "Medellín", "Cali", "Barranquilla",
        "Cartagena", "Bucaramanga", "Manizales", "Pereira",
        "Santa Marta", "Cúcuta"
    ]

    lista_usuarios = []

    for i, usuario in enumerate(usuarios):
        lista_usuarios.append([
            usuario["id"],
            nombres_esp[i],
            usuarios_esp[i],
            correos_esp[i],
            ciudades_esp[i]
        ])

    with open("usuarios.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["ID", "Nombre", "Usuario", "Correo", "Ciudad"])
        escritor.writerows(lista_usuarios)

    print("usuarios.csv creado")

    json_str = json.dumps(lista_usuarios, ensure_ascii=False)

    with open("usuarios.json", "w", encoding="utf-8") as archivo:
        json.dump(lista_usuarios, archivo, ensure_ascii=False, indent=4)

    print("usuarios.json creado")
