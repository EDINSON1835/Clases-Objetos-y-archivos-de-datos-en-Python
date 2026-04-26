from carrito import CarritoCompras
from archivo_csv import escribir_frutas, leer_frutas
from api_json import procesar_api

def main():
    print("PROYECTO PYTHON COMPLETO")

    carrito = CarritoCompras("Edinson")
    carrito.agregar("Laptop", 2500)
    carrito.agregar("Mouse", 50)
    carrito.agregar("Teclado", 100)

    print(carrito)
    print(f"Total productos: {len(carrito)}")

    escribir_frutas()
    leer_frutas()

    procesar_api()

if __name__ == "__main__":
    main()
