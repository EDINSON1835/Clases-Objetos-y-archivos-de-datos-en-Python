#  Evidencia Final — Python: POO, CSV y APIs

Este proyecto demuestra el uso de **Programación Orientada a Objetos (POO)**, manejo de **archivos CSV** y consumo de **APIs REST** en Python, integrando todo en un flujo práctico de análisis de datos.

---

##  Tecnologías utilizadas

*  Python 3
*  Módulos estándar: `csv`, `json`, `urllib`
*  Consumo de API pública (JSONPlaceholder)

---

##  Estructura del proyecto

```
proyecto_api_python/
│
├── carrito.py        # Clase POO CarritoCompras
├── archivo_csv.py    # Escritura y lectura de CSV
├── api_json.py       # Consumo de API + manejo JSON
└── main.py           # Ejecución principal del proyecto
```

---

##  Funcionalidades

###  1. Programación Orientada a Objetos (POO)

* Clase `CarritoCompras`
* Métodos:

  * `agregar()`
  * `total()`
  * `promedio()`
  * `producto_mas_caro()`
* Métodos mágicos:

  * `__str__` → impresión del carrito
  * `__len__` → cantidad de productos

---

###  2. Manejo de archivos CSV

* Escritura de datos en `frutas.csv`
* Lectura de datos desde CSV
* Uso de:

  * `csv.writer`
  * `csv.reader`

---

###  3. Consumo de API (JSONPlaceholder)

* Obtención de usuarios
* Obtención de álbumes
* Procesamiento de datos
* Análisis:

  * Conteo de álbumes por usuario
  * Identificación del usuario con más actividad

---

###  4. Manejo de JSON

* Serialización y deserialización:

  * `json.dumps()`
  * `json.loads()`
  * `json.dump()`
  * `json.load()`

---

##  Cómo ejecutar el proyecto

1. Clonar el repositorio:

```
git clone https://github.com/EDINSON1835/Clases-Objetos-y-archivos-de-datos-en-Python.git
```

2. Entrar a la carpeta:

```
cd Clases-Objetos-y-archivos-de-datos-en-Python
```

3. Ejecutar el programa:

```
python main.py
```

---

##  Resultados esperados

* ✔ Visualización de un carrito de compras
* ✔ Creación y lectura de archivos CSV
* ✔ Consumo de datos desde una API
* ✔ Análisis de información en consola

---

##  Objetivo académico

Este proyecto tiene como finalidad aplicar conceptos fundamentales de:

* Programación Orientada a Objetos
* Manipulación de archivos
* Consumo de servicios web
* Procesamiento de datos

---

##  Autor

**Edinson Mena**
Proyecto académico — Analítica de Datos
IUDIGITAL de Antioquia

---

##  Recomendación

Si este proyecto te parece útil, puedes darle una ⭐ en el repositorio.

---
