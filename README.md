# Proyecto de Recomendación y Análisis de Películas

## Índice

1. [Introducción](#introducción)
2. [Contextualización](#contextualización)
3. [Metodología](#metodología)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Conclusiones](#conclusiones)
6. [Ejemplo de Uso](#ejemplo-de-uso)
7. [Colaboración](#colaboración)

---

## Introducción

### Un Viaje por el Análisis de Datos y la Recomendación Personalizada en Cine

El trabajo incluye:

- Análisis de grandes conjuntos de datos de películas.
- Identificación de patrones en géneros, directores y actores.
- Desarrollo de algoritmos para predecir preferencias de usuarios.
- Creación de un sistema de recomendación basado en estos análisis.

Se utilizaron herramientas para procesar y interpretar los datos. El resultado final es un sistema capaz de sugerir películas a usuarios basándose en sus gustos previos y en las características de las películas. Este proyecto busca mejorar la experiencia de los espectadores al ayudarles a descubrir películas que probablemente disfruten, basándose en un análisis objetivo de datos y tendencias cinematográficas. 

**Tecnologías utilizadas:** Python, GitHub, FastAPI, Render. Además librerías como Pandas, Unvicorn, Matplotlib, Scikit-learn, entre otras.

---

## Contextualización

Este proyecto aborda la necesidad de recomendar películas de manera efectiva. El sistema considera factores como el género, el director y el actor principal para generar recomendaciones personalizadas y precisas.

---

## Metodología

El sistema utiliza **Vectorización TF-IDF** para representar las características relevantes (género, director, actor) y **Cosine Similarity** para calcular la similitud entre películas.

---

## Estructura del Proyecto

- **datos_procesados/**: Contiene los datos preprocesados utilizados para el sistema de recomendación.
- **modulos/**: Directorio con los módulos Python que implementan las funciones del sistema.
- **main.py**: Archivo principal que inicializa la aplicación FastAPI y define los endpoints para interactuar con el sistema.
- **requirements.txt**: Archivo que lista las dependencias del proyecto.

---

## Conclusiones

El sistema muestra una recomendación de películas similares, mejorando la experiencia del usuario al proporcionar sugerencias relevantes y personalizadas. Además provee datos como votos, años de estreno, etc. para posterior análisis.

### Ejemplos de lo que se podrá ver en el EDA:

#### Directores

- Hay una notable consistencia entre los directores del top 20, con la mayoría produciendo entre 35 y 50 películas.
- Incluso el director en el puesto 20 tiene cerca de 40 películas, lo que indica una alta productividad entre los directores más destacados.
- Todos los directores en el top 20 son hombres, lo que podría reflejar un sesgo histórico en la industria cinematográfica.

#### Ingresos y presupuesto

- La mayoría de las películas de la base de datos tienen ingresos bajos, con una distribución muy sesgada hacia la izquierda.
- Las películas con mayores ingresos tienden a tener un mayor número de votos.
- Las películas con mayor presupuesto tienden a tener mayores ingresos, un mayor número de votos y una calificación promedio más alta.
- Los mayores presupuestos suelen generar más ingresos, aunque no siempre es garantía de éxito.
- La mayoría de las películas se concentran en presupuestos e ingresos bajos, con algunos outliers entre la relación de presupuesto y retornos.

#### Preferencias por género

- Hay una preferencia por ciertos géneros, con el drama y la comedia dominando significativamente.
- Los mayores presupuestos suelen generar más ingresos, aunque la relación no es siempre garantía de éxito.
- La mayoría de las películas se concentran en presupuestos e ingresos bajos, con algunos outliers entre la relación de presupuesto y retornos.

---

## Ejemplo de Uso

### Instrucciones de Acceso a la API

#### Acceso a la Documentación

Visita el siguiente enlace: [Documentación API](https://proyecto-individual-n-1-labs-henry.onrender.com/docs)

#### Documentación Interactiva de la API

Esta documentación está generada por FastAPI y te permite explorar y probar los diferentes endpoints.

#### Navegación en la Documentación

- **Interfaz Interactiva**: Una vez que accedas al enlace, verás una interfaz interactiva que lista todos los endpoints disponibles en tu API.
- **Explorar Endpoints**: Puedes hacer clic en cada endpoint para ver detalles adicionales, como los parámetros que aceptan y los posibles valores de retorno.
- **Probar Endpoints**: La interfaz permite probar los endpoints directamente. Puedes ingresar valores en los campos de entrada y hacer clic en el botón "Try it out" para ver la respuesta de la API.

#### Uso de los Endpoints

Aquí tienes un ejemplo de cómo usar uno de los endpoints disponibles en tu API:

- **Método**: GET
- **Endpoint**: `/peliculas_dia/{dia}`
- **Descripción**: Este endpoint devuelve la cantidad de filmaciones en un día específico.
- **URL**: `/cantidad_filmaciones_mes/{mes}`
- **Parámetro**: 
  - `dia`: El nombre del día (por ejemplo, "lunes", "jueves", etc.)
- **Respuesta Esperada**

```json
{
  "cantidad": 5303
}


Colaboración
¡Tu contribución es bienvenida! Si deseas mejorar este proyecto, por favor sigue estos pasos:

Instrucciones de Ejecución Local
Clonación
Clona este repositorio a tu máquina local:

sh
Copiar código
git clone https://github.com/tu_usuario/tu_proyecto.git
Crear un entorno virtual:
sh
Copiar código
python -m venv venv
Activar el entorno virtual:
Windows:

sh
Copiar código
venv\Scripts\activate
macOS/Linux:

sh
Copiar código
source venv/bin/activate
Instalar las dependencias:
sh
Copiar código
pip install -r requirements.txt
Dependencias
Instala las dependencias necesarias:

sh
Copiar código
pip install -r requirements.txt
Las que se incluyen son:

fastapi==0.73.0
uvicorn==0.30.1
pandas==2.2.2
openpyxl==3.0.9
numpy==1.26.4
scikit-learn==1.5.1
seaborn==0.12.2
pydantic==1.10.17
python-multipart==0.0.9
python-dotenv==1.0.1
requests==2.32.3
pyarrow==15.0.2
matplotlib==3.9.1
Ubicación
Navega al directorio del proyecto:

sh
Copiar código
cd <dirección del proyecto>
Base de Datos
Por si se quiere consultar desde la base de origen, los datasets originales (convertidos a Parquet para optimizar rendimiento y espacio) se encuentran en la carpeta datos_procesados. Se utilizan conjuntos de datos de películas que incluyen información detallada sobre géneros, directores, actores y métricas de éxito.

Contribuciones
Abre un issue para discutir los cambios propuestos.
Haz un fork del repositorio y realiza tus modificaciones.
Envía un pull request para revisar tus cambios.
