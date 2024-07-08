import locale
import pandas as pd
import ast
from fastapi import FastAPI, HTTPException
import os

app = FastAPI()

# Carga de datasets
current_dir = os.path.dirname(os.path.abspath(__file__))
movies_path = os.path.join(current_dir, "datos_procesados", "movies_df.csv")
director_actor_path = os.path.join(current_dir, "datos_procesados", "director_actor_df.csv")

df_movies_limpio = pd.read_csv(movies_path)
director_actor_df = pd.read_csv(director_actor_path, index_col=0)

# Convertir la columna 'release_date' a datetime
df_movies_limpio['release_date'] = pd.to_datetime(df_movies_limpio['release_date'], format='%Y-%m-%d', errors='coerce')

# Convertir la columna 'actor' de string a lista
director_actor_df['actor'] = director_actor_df['actor'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

# Convertir movie_id a string en ambos DataFrames
df_movies_limpio = df_movies_limpio.assign(movie_id=df_movies_limpio['movie_id'].astype(str))
director_actor_df = director_actor_df.assign(movie_id=director_actor_df['movie_id'].astype(str))

# Configurar la localización para el formato de números
try:
    locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
except locale.Error:
    print("Locale es_ES.UTF-8 no disponible. Usando el locale por defecto.")

# Normalizar cadenas de texto
def normalize_string(s):
    return ''.join(c.lower() for c in s if c.isalnum())


#================================================================================================
# Endpoint cantidad_filmaciones_mes
@app.get("/cantidad_filmaciones_mes/{mes}")
def cantidad_filmaciones_mes(mes: str):
    try:
        # Filtrar películas por el mes especificado
        filtered_movies = df_movies_limpio[df_movies_limpio['release_date'].dt.strftime('%B').str.lower() == mes.lower()]
        # Contar la cantidad de películas filtradas
        cantidad = filtered_movies.shape[0]
        return {"cantidad": cantidad}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


#================================================================================================
# Endpoint cantidad_filmaciones_dia

#====================================== # Diccionario para mapear números a nombres de días
# Diccionario para mapear nombres de días a números
dias_a_numeros = {
    'lunes': 0,
    'martes': 1,
    'miércoles': 2,
    'jueves': 3,
    'viernes': 4,
    'sábado': 5,
    'domingo': 6
}

@app.get("/cantidad_filmaciones_dia/{dia}")
def cantidad_filmaciones_dia(dia: str):
    try:
        # Convertir el nombre del día a minúsculas para evitar problemas de capitalización
        dia = dia.lower()

        # Verificar si el nombre del día es válido
        if dia not in dias_a_numeros:
            raise ValueError(f"Nombre de día inválido: {dia}")

        # Obtener el número correspondiente al día
        dia_semana = dias_a_numeros[dia]

        # Filtrar películas por el día de la semana especificado
        filtered_movies = df_movies_limpio[df_movies_limpio['release_date'].dt.dayofweek == dia_semana]
        # Contar la cantidad de películas filtradas
        cantidad = filtered_movies.shape[0]
        
        return {"día": dia, "cantidad": cantidad}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#================================================================================================
# Endpoint score_titulo
@app.get("/score_titulo/{titulo}")
def score_titulo(titulo: str):
    try:
        # Filtrar película por título
        filtered_movie = df_movies_limpio[df_movies_limpio['title'].str.lower() == titulo.lower()]
        # Obtener título, año de estreno y score
        if not filtered_movie.empty:
            titulo = filtered_movie.iloc[0]['title']
            año_estreno = filtered_movie.iloc[0]['release_date'].year
            score = filtered_movie.iloc[0]['vote_average']
            return {"titulo": titulo, "año_estreno": año_estreno, "score": score}
        else:
            raise HTTPException(status_code=404, detail=f"No se encontró la película con título {titulo} en el dataset")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


#================================================================================================
from fastapi import FastAPI, HTTPException
import pandas as pd

# Endpoint votos_titulo
@app.get("/votos_titulo/{titulo}")
def votos_titulo(titulo: str):
    try:
        # Filtrar película por título
        filtered_movie = df_movies_limpio[df_movies_limpio['title'].str.lower() == titulo.lower()]
        
        # Verificar si se encontró la película
        if filtered_movie.empty:
            raise HTTPException(status_code=404, detail=f"No se encontró la película con título {titulo} en el dataset")
        
        # Obtener el primer resultado (debería ser único, pero por si acaso)
        movie_data = filtered_movie.iloc[0]
        
        # Obtener cantidad de votos y promedio de votos
        cantidad_votos = movie_data['vote_count']
        promedio_votos = movie_data['vote_average']
        
        # Verificar si cantidad_votos es un número válido y es mayor o igual a 2000
        try:
            cantidad_votos = float(cantidad_votos)  # Convertir a float para manejar posibles decimales
            if cantidad_votos >= 2000:
                return {"titulo": titulo, "cantidad_votos": cantidad_votos, "promedio_votos": promedio_votos}
            else:
                raise HTTPException(status_code=404, detail=f"La película {titulo} no cumple con la condición de tener al menos 2000 valoraciones.")
        except ValueError:
            raise HTTPException(status_code=404, detail=f"No se puede convertir `vote_count` de la película {titulo} a un número válido.")
        
    except HTTPException as he:
        # Capturar las excepciones HTTPException y relanzarlas
        raise he
    except Exception as e:
        # Capturar cualquier otra excepción y devolver un error 500
        raise HTTPException(status_code=500, detail=str(e))





#================================================================================================
# Endpoint get_actor
@app.get("/get_actor/{actor_name}")
def get_actor(actor_name: str):
    try:
        # Filtrar el DataFrame por nombre del actor
        actor_movies = director_actor_df[director_actor_df['actor'].apply(lambda lista_actores: any(actor_name.lower() in normalize_string(actor).lower() for actor in lista_actores))]
        if actor_movies.empty:
            raise HTTPException(status_code=404, detail=f"El actor {actor_name} no ha participado de ninguna filmación.")
        
        cantidad_filmaciones = actor_movies.shape[0]
        # Merge con df_movies_limpio para obtener los detalles de las películas
        actor_movies_details = pd.merge(actor_movies, df_movies_limpio, on='movie_id', how='inner')
        # Calcular retorno total y promedio en dólares
        actor_movies_details['return_dollars'] = actor_movies_details['return'] * actor_movies_details['budget']
        retorno_total_dollars = actor_movies_details['return_dollars'].sum()
        retorno_promedio_dollars = actor_movies_details['return_dollars'].mean()
        return {
            "actor": actor_name,
            "cantidad_filmaciones": cantidad_filmaciones,
            "retorno_total_dollars": retorno_total_dollars,
            "retorno_promedio_dollars": retorno_promedio_dollars
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


#================================================================================================
# Endpoint get_director
@app.get("/get_director/{director_name}")
def get_director(director_name: str):
    try:
        # Filtrar el DataFrame por nombre del director
        director_movies = director_actor_df[director_actor_df['director'].apply(lambda director: director_name.lower() in normalize_string(director).lower())]
        if director_movies.empty:
            raise HTTPException(status_code=404, detail=f"No se encontraron películas para el director {director_name}")
        # Obtener los movie_id de las películas dirigidas por el director
        movie_ids = director_movies['movie_id'].unique()
        # Filtrar df_movies_limpio por los movie_id obtenidos
        director_movies_details = df_movies_limpio[df_movies_limpio['movie_id'].isin(movie_ids)]
        # Calcular el retorno promedio en dólares de todas las películas del director
        director_movies_details['return_dollars'] = director_movies_details['return'] * director_movies_details['budget']
        avg_return_dollars = director_movies_details['return_dollars'].mean()
        return {
            "director": director_name,
            "avg_return_dollars": avg_return_dollars,
            "peliculas": director_movies_details.to_dict(orient="records")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

