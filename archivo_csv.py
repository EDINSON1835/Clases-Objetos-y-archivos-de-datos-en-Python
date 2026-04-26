import csv

def escribir_frutas():
    frutas = [
        ["Manzana", "Roja", "Dulce"],
        ["Plátano", "Amarillo", "Dulce"],
        ["Lima", "Verde", "Ácida"],
    ]

    with open("frutas.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(frutas)

    print("Archivo frutas.csv creado")

def leer_frutas():
    datos = []

    with open("frutas.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            datos.append(fila)

    print("Datos leídos:", datos)
