# Prueba técnica para scraper

# Overview

Este proyecto considera 2 tareas especificadas en un documento privado de prueba técnica, cuyas tareas abarcan
descargar y formatear un archivo json a csv y realizar un scraping de un sitio, exponiendo con un API, el resultado de los datos obtenidos a través de un JSON.

# Requerimientos
Este proyecto utiliza la versión 3.12 de Python, usando BeatifulSoup como librería de scrapping y playwright como webdriver. se proporciona un archivo requirements.txt para instalar las dependencias necesarias.

# Instalación
Para instalar las dependencias necesarias, se puede ejecutar el siguiente comando en la terminal:

```bash
pip install -r requirements.txt
```

Es recomendable utilizar un entorno virtual para evitar conflictos.

## Construcción de la imagen Docker
Para construir la imagen de Docker, se puede ejecutar el siguiente comando en la terminal:

```bash
docker build -t scrape-api .
```

Posteriormente, se puede ejecutar el contenedor con el siguiente comando:

```bash
docker run -p 5000:5000 scrape-api
```

# Ejecución

El proyecto cuenta con 2 scripts principales, uno para la tarea de formatear un archivo JSON a CSV y otro para la tarea de scraping, ambos casos de uso se exponen desde un archivo main.py, que actúa como un punto de entrada para ejecutar los scripts.

# 1. Formatear JSON a CSV

Para ejecutar el script de formatear un archivo JSON a CSV, se puede ejecutar el siguiente comando en la terminal:

```bash
  python main.py format-json --json <path_to_json_file> --csv <path_to_new_csv_file>
```

Donde:
- `path_to_json_file` es la ruta del archivo JSON a formatear. En caso de no especificar la ruta del archivo JSON, se utilizará cómo fuente el json de la url: https://storage.googleapis.com/resources-prod-shelftia/scrapers-prueba/product.json que fue especificada en el documento de la prueba técnica.
- `path_to_new_csv_file` es la ruta del archivo CSV a generar. En caso de no especificar la ruta del archivo CSV, se generará un archivo con el nombre products.csv por defecto

Ejemplo:

Este ejemplo descargará el archivo https://storage.googleapis.com/resources-prod-shelftia/scrapers-prueba/product.json para convertirlo en csv y guardarlo en la raiz del proyecto con el nombre products.csv.

```bash
  python main.py format-json
```

# 2. Scrapping
El proyecto de scrapping está diseñado para ejecutarse en un contenedor de Docker, sin embargo, se puede ejecutar en local, pero se debe tener en cuenta que se necesita tener instaladas las dependencias de playwright (Estas dependencias dependen del sistema operativo) y pueden ejecutarse con `playwright install` y `playwrigth install-deps`.

Para ejecutar el script de scrapping, se puede ejecutar el siguiente comando en la terminal:

```bash
  python main.py start-api
```

ó con el contenedor de Docker:

```bash
docker run -p 5000:5000 scrape-api
```
cómo se mencionó anteriormente.


# API

El proyecto expone un API en la ruta `/scrape` que devuelve un JSON con los productos obtenidos del scrapping.

## /scrape

### POST

localhost:5000/scrape

### Body

```json
{
    "url": "https://www.tiendasjumbo.co/supermercado/despensa/aceite"
}
```

### Response

```json
{
    "products": [
        {
            "name": "Aceite Puroil vegetal x3000ml",
            "price": "$ 20.890",
            "promo_price": "$ 20.890"
        },
        {
            "name": "Aceite Riquisimo garrafa x3000ml",
            "price": "$ 29.450",
            "promo_price": "$ 29.450"
        },
        {
            "name": "Aceite Cuisine&Co girasol x3L",
            "price": "$ 39.490",
            "promo_price": "$ 39.490"
        },
        {
            "name": "Aceite Ybarra oliva extra virgen x1L",
            "price": "$ 59.090",
            "promo_price": "$ 59.090"
        },
        {
            "name": "Aceite Premier girasol x2700ml",
            "price": "$ 52.290",
            "promo_price": "$ 38.990"
        },
        {
            "name": "Aceite Ybarra oliva extra virgen x3L",
            "price": "$ 146.290",
            "promo_price": "$ 142.590"
        },
        {
            "name": "Aceite Canola Life puro x3L",
            "price": "$ 72.590",
            "promo_price": "$ 50.813"
        },
        {
            "name": "Aceite Premier girasol x900ml",
            "price": "$ 18.450",
            "promo_price": "$ 18.450"
        },
        {
            "name": "Aceite Olivetto oliva para freír x2000ml",
            "price": "$ 61.590",
            "promo_price": "$ 49.272"
        },
        {
            "name": "Aceite Premier oliva extra virgen x250ml",
            "price": "$ 25.950",
            "promo_price": "$ 25.950"
        },
        {
            "name": "Aceite Olivetto oliva para freír x1000ml",
            "price": "$ 33.990",
            "promo_price": "$ 27.192"
        },
        {
            "name": "Aceite Cuisine&Co oliva extra virgen x1L",
            "price": "$ 69.990",
            "promo_price": "$ 69.990"
        },
        {
            "name": "Aceite Premier oliva extra virgen x500ml",
            "price": "$ 48.660",
            "promo_price": "$ 48.660"
        },
        {
            "name": "Aceite Premier girasol x4500ml",
            "price": "$ 90.390",
            "promo_price": "$ 90.390"
        },
        {
            "name": "Aceite Premier girasol x1800ml",
            "price": "$ 36.020",
            "promo_price": "$ 36.020"
        }
    ],
    "url": "https://www.tiendasjumbo.co/supermercado/despensa/aceite"
}
```

# Comentarios de la solución

## Formatear JSON a CSV
Lo interesante de esta tarea es extraer de un nivel profundo el contenido de un JSON, el mismo tiene diferentes lenguajes disponibles para extraer información, se optó por extraer la información del lenguaje es-CR que está disponible, pero esto podría ser parametrizable para extraer información de cualquier lenguaje disponible en el JSON.

## Scrapping
El sitio a scrapear, maneja una carga de contenido basada en scroll, se utilizó playwright para garantizar que se cargue todo el contenido antes de extraer la información, para este tipo de utilidad, se podría utilizar Selenium, pero se optó por playwright por ser más ligero y rápido.
También pensé en una estrategia basada en esperar la carga de un API del sitio web, y extraer la información directamente del API, manipular directamente ese tipo de respuestas permite reconocer casos especiales como la paginación o el número total de elementos de una categoría de productos, que no se consideró en este caso.
Algo que no se especifica en el ejercicio, es que sucede para los articulos que no tienen un precio de promoción, por lo que opté a asignar para estos casos el precio regular.