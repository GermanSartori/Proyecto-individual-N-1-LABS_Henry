import locale
import pandas as pd
import ast
from fastapi import FastAPI, HTTPException
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


app = FastAPI()

# Carga de datasets
current_dir = os.path.dirname(os.path.abspath(__file__))
movies_path = os.path.join(current_dir, "datos_procesados", "movies_df.csv")
director_actor_path = os.path.join(current_dir, "datos_procesados", "director_actor_df.csv")

df_movies_limpio = pd.read_csv(movies_path)
director_actor_df = pd.read_csv(director_actor_path, index_col=0)

# Conversión de la columna 'release_date' a datetime
df_movies_limpio['release_date'] = pd.to_datetime(df_movies_limpio['release_date'], format='%Y-%m-%d', errors='coerce')

# Conversión de la columna 'actor' de string a lista
director_actor_df['actor'] = director_actor_df['actor'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

# Conversión de movie_id a string en ambos DataFrames
df_movies_limpio = df_movies_limpio.assign(movie_id=df_movies_limpio['movie_id'].astype(str))
director_actor_df = director_actor_df.assign(movie_id=director_actor_df['movie_id'].astype(str))

# Configuración de la localización para el formato de números
try:
    locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
except locale.Error:
    print("Locale es_ES.UTF-8 no disponible. Usando el locale por defecto.")

# Normalización de cadenas de texto
def normalize_string(s):
    return ''.join(c.lower() for c in s if c.isalnum())


#================================================================================================
# Endpoint cantidad_filmaciones_mes
@app.get("/cantidad_filmaciones_mes/{mes}")
def cantidad_filmaciones_mes(mes: str):
    try:
        # Filtrado de películas por el mes especificado
        filtered_movies = df_movies_limpio[df_movies_limpio['release_date'].dt.strftime('%B').str.lower() == mes.lower()]
        # Recuento de la cantidad de películas filtradas
        cantidad = filtered_movies.shape[0]
        return {"cantidad": cantidad}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


#================================================================================================
# Endpoint cantidad_filmaciones_dia


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
        # Conversión del nombre del día a minúsculas
        dia = dia.lower()

        # Verificación de si el nombre del día es válido
        if dia not in dias_a_numeros:
            raise ValueError(f"Nombre de día inválido: {dia}")

        # Obtención del número correspondiente al día
        dia_semana = dias_a_numeros[dia]

        # Filtrado de películas por el día de la semana especificado
        filtered_movies = df_movies_limpio[df_movies_limpio['release_date'].dt.dayofweek == dia_semana]
        # Recuento de la cantidad de películas filtradas
        cantidad = filtered_movies.shape[0]
        
        return {"día": dia, "cantidad": cantidad}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#================================================================================================
# Endpoint score_titulo
@app.get("/score_titulo/{titulo}")
def score_titulo(titulo: str):
    try:
        # Filtrado de película por título
        filtered_movie = df_movies_limpio[df_movies_limpio['title'].str.lower() == titulo.lower()]
        # Obtención de título, año de estreno y score
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
        # Filtrado de película por título
        filtered_movie = df_movies_limpio[df_movies_limpio['title'].str.lower() == titulo.lower()]
        
        # Verificación de si se encontró la película
        if filtered_movie.empty:
            raise HTTPException(status_code=404, detail=f"No se encontró la película con título {titulo} en el dataset")
        
        # Obtención del primer resultado (debería ser único, pero por si acaso)
        movie_data = filtered_movie.iloc[0]
        
        # Obtención de cantidad de votos y promedio de votos
        cantidad_votos = movie_data['vote_count']
        promedio_votos = movie_data['vote_average']
        
        # Verificación de si cantidad_votos es un número válido y es mayor o igual a 2000
        try:
            cantidad_votos = float(cantidad_votos)  # Conversión a float
            if cantidad_votos >= 2000:
                return {"titulo": titulo, "cantidad_votos": cantidad_votos, "promedio_votos": promedio_votos}
            else:
                raise HTTPException(status_code=404, detail=f"La película {titulo} no cumple con la condición de tener al menos 2000 valoraciones.")
        except ValueError:
            raise HTTPException(status_code=404, detail=f"No se puede convertir `vote_count` de la película {titulo} a un número válido.")
        
    except HTTPException as he:
        # Captura de las excepciones HTTPException para relanzarlas
        raise he
    except Exception as e:
        # Captura de cualquier otra excepción para devolver un error 500
        raise HTTPException(status_code=500, detail=str(e))





#================================================================================================
# Endpoint get_actor

@app.get("/get_actor/{actor_name}")
def get_actor(actor_name: str):
    try:
        # Filtrado del DataFrame por nombre del actor
        actor_movies = director_actor_df[director_actor_df['actor'].apply(lambda lista_actores: any(actor_name.lower() in [normalize_string(actor).lower() for actor in lista_actores]))]
        
        if actor_movies.empty:
            raise HTTPException(status_code=404, detail=f"El actor {actor_name} no ha participado de ninguna filmación.")
        
        # Merge con df_movies_limpio para obtener los detalles de las películas
        actor_movies_details = pd.merge(actor_movies, df_movies_limpio, on='movie_id', how='inner')
        
        cantidad_filmaciones = actor_movies_details.shape[0]
        
        # Cálculo del retorno total y promedio en dólares
        actor_movies_details['return_dollars'] = actor_movies_details['return'] * actor_movies_details['budget']
        retorno_total_dollars = actor_movies_details['return_dollars'].sum()
        retorno_promedio_dollars = actor_movies_details['return_dollars'].mean()
        
        return {
            "actor": actor_name,
            "cantidad_filmaciones": cantidad_filmaciones,
            "retorno_total_dollars": retorno_total_dollars,
            "retorno_promedio_dollars": retorno_promedio_dollars
        }
    
    except HTTPException as he:
        # Captura de las excepciones HTTPException para relanzarlas
        raise he
    
    except Exception as e:
        # Captura de cualquier otra excepción para devolver un error 500
        error_message = f"Error en get_actor para el actor {actor_name}: {str(e)}"
        print(error_message)  # Impresión del error en la consola
        raise HTTPException(status_code=500, detail="Ocurrió un error interno al procesar la solicitud.")




#================================================================================================
@app.get("/get_director/{director_name}")
def get_director(director_name: str):
    try:
        # Filtrado del DataFrame por nombre del director
        director_movies = director_actor_df[director_actor_df['director'].apply(lambda director: director_name.lower() in normalize_string(director).lower())]
        if director_movies.empty:
            raise HTTPException(status_code=404, detail=f"No se encontraron películas para el director {director_name}")
        
        # Obteneción de los movie_id de las películas dirigidas por el director
        movie_ids = director_movies['movie_id'].unique()
        
        # Filtrado de df_movies_limpio por los movie_id obtenidos
        director_movies_details = df_movies_limpio[df_movies_limpio['movie_id'].isin(movie_ids)]
        
        # Cáluclo del retorno promedio en dólares de todas las películas del director
        director_movies_details['return_dollars'] = director_movies_details['return'] * director_movies_details['budget']
        avg_return_dollars = director_movies_details['return_dollars'].mean()
        
        return {
            "director": director_name,
            "avg_return_dollars": avg_return_dollars,
            "peliculas": director_movies_details.to_dict(orient="records")
        }
    
    except KeyError as e:
        raise HTTPException(status_code=404, detail=f"No se encontraron datos clave: {str(e)}")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




#================================================================================================
@app.get("/recomendar/{titulo}")
def recomendacion(titulo: str):
    try:
        # Verificar que df_movies_limpio es un DataFrame
        if not isinstance(df_movies_limpio, pd.DataFrame):
            raise TypeError("df_movies_limpio no es un DataFrame")

        # Verificar si el título existe en el DataFrame
        if titulo not in df_movies_limpio['title'].values:
            raise HTTPException(status_code=404, detail=f"No se encontró la película '{titulo}'")

        # Filtrado de películas por el mismo género que la película de referencia
        genre = df_movies_limpio.loc[df_movies_limpio['title'] == titulo, 'genre'].iloc[0]
        similar_movies = df_movies_limpio[df_movies_limpio['genre'] == genre]

        # Vectorización TF-IDF de las características relevantes (género y título)
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(similar_movies['genre'] + ' ' + similar_movies['title'])

        # Cálculo de la similitud de coseno entre la película de referencia y todas las películas similares
        reference_index = similar_movies[similar_movies['title'] == titulo].index[0]
        similarities = cosine_similarity(tfidf_matrix[reference_index:reference_index+1], tfidf_matrix).flatten()

        # Obtención de las películas, ordenadas por similitud (excluyendo la película de referencia)
        similar_movies_indices = similarities.argsort()[::-1][1:6]  # Excluye la primera (la misma película)
        recommended_movies = similar_movies.iloc[similar_movies_indices]['title'].tolist()

        return recommended_movies
    
    except TypeError as te:
        raise HTTPException(status_code=500, detail=str(te))
    except IndexError:
        raise HTTPException(status_code=404, detail=f"No se encontraron películas similares a '{titulo}'")
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
    

    print(f"Tipo de df_movies_limpio: {type(df_movies_limpio)}")
print(f"Columnas en df_movies_limpio: {df_movies_limpio.columns}")
print(f"Primeras filas de df_movies_limpio:\n{df_movies_limpio.head()}")
