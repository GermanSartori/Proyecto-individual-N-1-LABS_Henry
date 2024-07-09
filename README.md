Documentación para el "Proyecto de Recomendación de Películas"

Un Viaje por el Análisis de Datos y la Recomendación Personalizada


El trabajo incluye:

Análisis de conjuntos de datos de películas.
Identificación de patrones en géneros, directores y actores principalmente.
Creación de un sistema de recomendación basado en estos análisis.


El resultado final es un sistema capaz de sugerir películas a usuarios basándose en sus gustos previos y en las características de las películas.
Este proyecto busca mejorar la experiencia de los espectadores al ayudarles a descubrir películas que probablemente disfruten, basándose en un análisis objetivo de datos y tendencias cinematográficas.



Tecnologías utilizadas: Python, Github, FastApi, Render. Además librerías commo Pandas, Unvicorn, Matplotlib, Scikit-learn, entre otras.


Aplicaciones prácticas: 
Identificación de patrones: Detecta patrones en las preferencias de los usuarios, como las películas que han visto, calificado o buscado, para comprender sus gustos y tendencias cinematográficas.
Acceso a través de una API: Proporciona una interfaz de programación de aplicaciones (API) que permite a otras aplicaciones o servicios acceder a las funcionalidades de recomendación de películas. Esto permite integrar tu sistema en otras plataformas, como sitios web de streaming o aplicaciones móviles.


EJECUCIÓN:
Para ejecutar este proyecto localmente, sigue estos pasos:

CLONACIÓN:
Clona este repositorio a tu máquina local:
git clone https://github.com/tu_usuario/tu_proyecto.git

UBICACIÓN:
Navega al directorio del proyecto:
cd <dirección del proyecto>

DEPENDENCIAS:
Instala las dependencias necesarias:
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

BASE DE DATOS:
Por si se quiere consultar desde la base de origen, los datasets originales (convertidos a Parquet para optimizar rendimiento y espacio) se encuentran e4n la carpeta "datos_procesados".



CONTEXTUALIZACIÓN:
Este proyecto aborda la necesidad de recomendar películas de manera efectiva utilizando técnicas avanzadas de procesamiento de lenguaje natural y aprendizaje automático. El sistema considera factores como el género, el director y el actor principal para generar recomendaciones personalizadas y precisas.

METODOLOGÍA Y ANÁLISIS:
Técnicas Utilizadas
El sistema utiliza Vectorización TF-IDF para representar las características relevantes (género, director, actor) y Cosine Similarity para calcular la similitud entre películas.

ESTRUCTURA DEL PROYECTO:
datos_procesados/: Contiene los datos preprocesados utilizados para el sistema de recomendación.
modulos/: Directorio con los módulos Python que implementan las funciones del sistema.
main.py: Archivo principal que inicializa la aplicación FastAPI y define los endpoints para interactuar con el sistema.
requirements.txt: Archivo que lista las dependencias del proyecto.

INSTRUCCIONES DE ACCESO A LA API:
1. Acceso a la Documentación Interactiva
Para acceder a la documentación interactiva de la API, puedes visitar el siguiente enlace:
https://proyecto-individual-n-1-labs-henry.onrender.com/docs

Documentación Interactiva de la API
Esta documentación está generada por FastAPI y te permite explorar y probar los diferentes endpoints de la API directamente desde tu navegador.
Navegación en la Documentación
Interfaz Interactiva: Una vez que accedas al enlace, verás una interfaz interactiva que lista todos los endpoints disponibles en tu API.
Explorar Endpoints: Puedes hacer clic en cada endpoint para ver detalles adicionales, como los parámetros que aceptan y los posibles valores de retorno.
Probar Endpoints: La interfaz permite probar los endpoints directamente. Puedes ingresar valores en los campos de entrada y hacer clic en el botón "Try it out" para ver la respuesta de la API.

Ejemplo de uso:

Endpoint: peliculas_dia/{dia}
Este endpoint devuelve la cantidad de filmaciones en un día específico.

Método: GET
dia: El nombre del dia de la semana (por ejemplo, "lunes", "jueves", etc.)
Ejemplo de Uso
Para obtener la cantidad de filmaciones en el mes de enero, puedes hacer una solicitud GET a la siguiente URL:
[https://proyecto-individual-n-1-labs-henry.onrender.com/cantidad_filmaciones_mes/enero](https://proyecto-individual-n-1-labs-henry.onrender.com/docs#/default/cantidad_filmaciones_dia_peliculas_dia__dia__get)

Respuesta Esperada
{
  "cantidad": 3503
}



Navega a la documentación de la API en tu navegador web: URL_DE_TU_API/docs.
EJEMPLO DE USO:
Para obtener recomendaciones de películas similares a una película específica, realiza una solicitud GET al endpoint /recomendar/{titulo} con el título de la película de referencia en la URL.


Esto devolverá una lista de las películas más similares a la ingresada en caso de estar presente en la base de datos.


FUENTES DE DATOS:
Se utilizan conjuntos de datos de películas que incluyen información detallada sobre géneros, directores, actores y métricas de éxito.

CONCLUSIONES:
El sistema ha demostrado una alta precisión en la recomendación de películas similares, mejorando la experiencia del usuario al proporcionar sugerencias relevantes y personalizadas.

COLABORACIÓN:
¡Tu contribución es bienvenida! Si deseas mejorar este proyecto, por favor sigue estos pasos:

Abre un issue para discutir los cambios propuestos.
Haz un fork del repositorio y realiza tus modificaciones.
Envía un pull request para revisar tus cambios.







La Importancia de la Documentación en Proyectos de Ciencia de Datos:
Facilitad de Entendimiento: Una documentación clara y detallada permite que otros usuarios, colaboradores o futuros mantenedores del proyecto puedan comprender rápidamente el objetivo, la estructura, el funcionamiento y las características clave del proyecto.

Reutilización y Mantenimiento: La documentación facilita la reutilización del código, los datos y las metodologías empleadas. Esto es especialmente relevante en la ciencia de datos, donde los proyectos a menudo se basan en trabajo previo.

Transparencia y Reproducibilidad: Una buena documentación fomenta la transparencia del trabajo realizado y permite que otros puedan reproducir y validar los resultados del proyecto.

Colaboración y Contribución: Un README bien estructurado y completo incentiva la colaboración al facilitar que nuevos contribuidores puedan involucrarse y aportar al proyecto.

Cómo Documentar de Manera Efectiva:

Estructura y Organización: Divide el README en secciones claras y lógicas, como Introducción, Instalación, Uso, Metodología, Resultados, Contribución, etc. Esto ayuda a los usuarios a encontrar rápidamente la información que necesitan.

Lenguaje Claro y Conciso: Utiliza un lenguaje sencillo y evita jerga técnica innecesaria. Procura ser lo más conciso posible sin omitir detalles importantes.

Instrucciones Detalladas: Proporciona instrucciones paso a paso para instalar, configurar y ejecutar el proyecto. Incluye requisitos, comandos y ejemplos de uso.

Contextualización y Motivación: Explica el problema que aborda el proyecto, su objetivo y las principales características o funcionalidades. Esto ayuda a los usuarios a comprender el propósito del proyecto.

Metodología y Análisis: Describe las técnicas y algoritmos utilizados, las fuentes de datos y cualquier otra información relevante sobre la implementación del proyecto.

Resultados y Conclusiones: Presenta los hallazgos clave, las métricas de rendimiento y las principales conclusiones obtenidas a partir del proyecto.

Contribución y Colaboración: Establece pautas claras para que los usuarios puedan reportar problemas, solicitar nuevas funciones o enviar contribuciones al proyecto.

Licencia y Atribución: Especifica la licencia del proyecto y, si corresponde, proporciona la información de atribución para los recursos utilizados.

Ejemplo
Descripción
Este proyecto tiene como objetivo analizar los datos de ventas de una tienda de ropa para identificar patrones, tendencias y oportunidades de mejora. Utilizando técnicas de ciencia de datos, se busca generar información valiosa que ayude a la toma de decisiones estratégicas para mejorar el rendimiento de la tienda.

Tabla de contenido
Introducción
Instalación y Requisitos
Estructura del Proyecto
Uso y Ejecución
Datos y Fuentes
Metodología
Resultados y Conclusiones
Contribución y Colaboración
Licencia
Instalación y Requisitos
Requisitos:

Python 3.7 o superior
pandas
numpy
matplotlib
scikit-learn
Pasos de instalación:

Clonar el repositorio: git clone https://github.com/usuario/proyecto-ventas-ropa.git
Crear un entorno virtual: python -m venv venv
Activar el entorno virtual:
Windows: venv\Scripts\activate
macOS/Linux: source venv/bin/activate
Instalar las dependencias: pip install -r requirements.txt
Estructura del Proyecto
data/: Contiene los archivos de datos utilizados en el proyecto.
notebooks/: Incluye los notebooks de Jupyter con el análisis y modelos.
src/: Código fuente del proyecto, incluyendo scripts y módulos.
reports/: Guarda los informes y visualizaciones generados.
README.md: Archivo de documentación del proyecto.
Uso y Ejecución
Para ejecutar el análisis de ventas, abrir el notebook ventas_analisis.ipynb en la carpeta notebooks/.
El notebook guiará a través de las diferentes etapas del análisis, incluyendo carga de datos, visualizaciones y modelado.
Para generar un informe de ventas, ejecutar el script generate_report.py en la carpeta src/.
Datos y Fuentes
Los datos utilizados en este proyecto provienen de la base de datos interna de la tienda de ropa. Los datos incluyen información sobre ventas, clientes, inventario y promociones. Los archivos de datos se encuentran en la carpeta data/ en formato CSV.

Metodología
Se utilizaron técnicas de análisis exploratorio de datos para identificar patrones y tendencias en los datos de ventas. Se aplicaron modelos de aprendizaje automático, como regresión lineal y árboles de decisión, para predecir las ventas futuras. También se realizaron análisis de segmentación de clientes y optimización de estrategias de marketing.

Resultados y Conclusiones
El análisis de ventas reveló un aumento significativo en las ventas durante los meses de verano y temporada navideña.
Se identificaron los productos más y menos vendidos, lo que permitirá ajustar el inventario y las estrategias de merchandising.
El modelo de predicción de ventas alcanzó una precisión del 85%, lo que ayudará a la planificación y toma de decisiones.
Contribución y Colaboración
Los contribuidores son bienvenidos a reportar problemas, enviar solicitudes de funciones o enviar pull requests en el repositorio de GitHub. Antes de contribuir, por favor revisa las pautas de contribución en el archivo CONTRIBUTING.md.

Autores:
Este proyecto fue realizado por: Mariana Gigena . (Se puede incluir Linkedin o mail para que los contacten)
