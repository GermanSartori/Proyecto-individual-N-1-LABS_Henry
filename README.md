# DOCUMENTACIÓN PARA EL PROYECTO DE RECOMENDACIÓN Y ANÁLISIS DE PELÍCULAS 🚀


---


## Índice

- [Introducción](#introducción)
- [Contextualización](#contextualización)
- [Metodología](#metodología)
- [Conclusiones](#conclusiones)
- [Ejemplo de Uso](#ejemplo-de-uso)
- [Colaboración](#colaboración)



---


### 🟡 INTRODUCCIÓN
## "Un Viaje por el Análisis de Datos y la Recomendación Personalizada en Cine"

### El trabajo incluye:
Análisis de grandes conjuntos de datos de películas.
Identificación de patrones en géneros, directores y actores.
Desarrollo de algoritmos para predecir preferencias de usuarios.
Creación de un sistema de recomendación basado en estos análisis.

Se utilizaron herramientas para procesar y interpretar los datos. El resultado final es un sistema capaz de sugerir películas a usuarios basándose en sus gustos previos y en las características de las películas.
Este proyecto busca mejorar la experiencia de los espectadores al ayudarles a descubrir películas que probablemente disfruten, basándose en un análisis objetivo de datos y tendencias cinematográficas.
Tecnologías utilizadas: Python, Github, FastApi, Render. Además librerías commo Pandas, Unvicorn, Matplotlib, Scikit-learn, entre otras.


---


### 🟡 CONTEXTUALIZACIÓN:
Este proyecto aborda la necesidad de recomendar películas de manera efectiva. El sistema considera factores como el género, el director y el actor principal para generar recomendaciones personalizadas y precisas.


---


### 🟡METODOLOGÍA:
El sistema utiliza Vectorización TF-IDF para representar las características relevantes (género, director, actor) y Cosine Similarity para calcular la similitud entre películas.


---


### 🟡ESTRUCTURA DEL PROYECTO:
- datos_procesados/: Contiene los datos preprocesados utilizados para el sistema de recomendación.  
- modulos/: Directorio con los módulos Python que implementan las funciones del sistema.  
- main.py: Archivo principal que inicializa la aplicación FastAPI y define los endpoints para interactuar con el sistema.  
- requirements.txt: Archivo que lista las dependencias del proyecto.  


---


### 🟡CONCLUSIONES:
El sistema muestra una recomendación de películas similares, mejorando la experiencia del usuario al proporcionar sugerencias relevantes y personalizadas. 
Además provee datos como votos, años de estreno, etc. para posterior análisis.

Algunos ejemplos de lo que se podrá ver en el EDA:  

#### Directores:
- Hay una notable consistencia entre los directores del top 20, con la mayoría produciendo entre 35 y 50 películas.
  
- Incluso el director en el puesto 20 tiene cerca de 40 películas, lo que indica una alta productividad entre los directores más destacados.
  
- Todos los directores en el top 20 son hombres, lo que podría reflejar un sesgo histórico en la industria cinematográfica.

#### Ingresos y presupuesto:
- La base de datos muestra que la mayoría de las películas tienen ingresos bajos, con una distribución sesgada hacia la izquierda.
  
- Las películas con mayores ingresos generalmente reciben más votos. Además, aquellas con presupuestos más altos suelen generar mayores ingresos y obtener una calificación promedio más alta.

- Sin embargo, la relación entre presupuesto y éxito no siempre es garantía. Aunque la mayoría de las películas se concentran en presupuestos e ingresos bajos, existen algunos casos atípicos donde la relación entre presupuesto y retorno varía, reflejando diversos resultados. 

#### Preferencias por género:
- Preferencia por ciertos géneros, con el drama y la comedia dominando significativamente.


---


### 🟡EJEMPLO DE USO  
#### Instrucciones de Acceso a la API  
## Acceso a la Documentación  
[# Visita este enlace](https://proyecto-individual-n-1-labs-henry.onrender.com/docs)



##### Documentación Interactiva de la API
Esta documentación está generada por FastAPI y te permite explorar y probar los diferentes endpoints.

##### 1. Navegación en la Documentación
Interfaz Interactiva: Una vez que accedas al enlace, verás una interfaz interactiva que lista todos los endpoints disponibles en tu API.  
Explorar Endpoints: Puedes hacer clic en cada endpoint para ver detalles adicionales, como los parámetros que aceptan y los posibles valores de retorno.  
Probar Endpoints: La interfaz permite probar los endpoints directamente. Puedes ingresar valores en los campos de entrada y hacer clic en el botón "Try it out" para ver la respuesta de la API.  
##### 1. Uso de los Endpoints
Aquí tienes un ejemplo de cómo usar uno de los endpoints disponibles en tu API:  
Método: GET
Endpoint: peliculas_dia/{dia}  
Este endpoint devuelve la cantidad de filmaciones en un día específico.
URL: [Visita la documentación de la API](https://proyecto-individual-n-1-labs-henry.onrender.com/docs#/default/cantidad_filmaciones_dia_peliculas_dia__dia__get)
 
Parámetro:
día: El nombre del día (por ejemplo, "lunes", "jueves", etc.)  
  
Respuesta Esperada

- {  
-   "cantidad": 5303  
- }  


---


### 🟡FUENTES DE DATOS:
Se utilizan conjuntos de datos de películas que incluyen información detallada sobre géneros, directores, actores y métricas de éxito.

---

### 🟡COLABORACIÓN:
¡Tu contribución es bienvenida! Si deseas mejorar este proyecto, por favor sigue estos pasos:

#### INSTRUCCIONES DE EJECUCIÓN LOCAL
##### EJECUCIÓN:
Para ejecutar este proyecto localmente, sigue estos pasos:
##### CLONACIÓN:
Clona este repositorio a tu máquina local:  
[Repositorio GitHub](https://github.com/GermanSartori/Proyecto-individual-N-1---LABS---Henry.git)
 
Crear un entorno virtual: python -m venv venv  
Activar el entorno virtual:  
Windows: venv\Scripts\activate  
macOS/Linux: source venv/bin/activate  
Instalar las dependencias: pip install -r requirements.txt  
##### DEPENDENCIAS:
Instala las dependencias necesarias:    
###### pip install -r requirements.txt.  

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

##### Base de datos:
Por si se quiere consultar desde la base de origen, los datasets originales (convertidos a Parquet para optimizar rendimiento y espacio) se encuentran en la carpeta "datos_procesados".  
Se utilizan conjuntos de datos de películas que incluyen información detallada sobre géneros, directores, actores y métricas de éxito.  

-Abre un issue para discutir los cambios propuestos.  
-Haz un fork del repositorio y realiza tus modificaciones.  
-Envía un pull request para revisar tus cambios.
