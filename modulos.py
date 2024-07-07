import locale
import pandas as pd
import ast
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Carga de datasets
df_movies_limpio = pd.read_csv(r"E:\Repositorios y bases de datos\Henry DS\Proyecto-individual-N-1---LABS---Henry\datos_procesados\movies_df.csv")
director_actor_df = pd.read_csv(r"E:\Repositorios y bases de datos\Henry DS\Proyecto-individual-N-1---LABS---Henry\datos_procesados\director_actor_df.csv", index_col=0)

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


# Endpoint cantidad_filmaciones_mes
@app.get("/cantidad_filmaciones_mes/{mes}")
def cantidad_filmaciones_mes(mes):
    # Filtrar películas por el mes especificado
    filtered_movies = df_movies_limpio[df_movies_limpio['release_date'].dt.month_name(locale='es_ES').str.lower() == mes.lower()]
    
    # Contar la cantidad de películas filtradas
    cantidad = filtered_movies.shape[0]
    
    return {"cantidad": cantidad}


# Endpoint cantidad_filmaciones_dia
@app.get("/cantidad_filmaciones_dia/{dia}")
def cantidad_filmaciones_dia(dia):
    # Filtrar películas por el día especificado
    filtered_movies = df_movies_limpio[df_movies_limpio['release_date'].dt.day == dia]
    
    # Contar la cantidad de películas filtradas
    cantidad = filtered_movies.shape[0]
    
    return {"cantidad": cantidad}


# Endpoint score_titulo
@app.get("/score_titulo/{titulo}")
def score_titulo(titulo):
    # Filtrar película por título
    filtered_movie = df_movies_limpio[df_movies_limpio['title'].str.lower() == titulo.lower()]
    
    # Obtener título, año de estreno y score
    if not filtered_movie.empty:
        titulo = filtered_movie.iloc[0]['title']
        año_estreno = filtered_movie.iloc[0]['release_date'].year
        score = filtered_movie.iloc[0]['vote_average']  # Aquí podrías ajustar según el score o popularidad que necesites
        return {"titulo": titulo, "año_estreno": año_estreno, "score": score}
    else:
        raise HTTPException(status_code=404, detail=f"No se encontró la película con título `{titulo}` en el dataset")


# Endpoint votos_titulo
@app.get("/votos_titulo/{titulo}")
def votos_titulo(titulo):
    # Filtrar película por título
    filtered_movie = df_movies_limpio[df_movies_limpio['title'].str.lower() == titulo.lower()]
    
    # Verificar si se encontró la película y tiene al menos 2000 votos
    if not filtered_movie.empty:
        cantidad_votos = filtered_movie.iloc[0]['vote_count']
        promedio_votos = filtered_movie.iloc[0]['vote_average']
        
        if pd.notnull(cantidad_votos) and cantidad_votos >= 2000:
            return {"titulo": titulo, "cantidad_votos": cantidad_votos, "promedio_votos": promedio_votos}
        else:
            raise HTTPException(status_code=404, detail=f"La película `{titulo}` no cumple con la condición de tener al menos 2000 valoraciones.")
    else:
        raise HTTPException(status_code=404, detail=f"No se encontró la película con título `{titulo}` en el dataset")


# Endpoint get_actor
@app.get("/get_actor/{actor_name}")
def get_actor(actor_name):
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


# Endpoint get_director
@app.get("/get_director/{director_name}")
def get_director(director_name):
    # Filtrar el DataFrame por nombre del director
    director_movies = director_actor_df[director_actor_df['director'].apply(lambda director: director_name.lower() in director.lower())]

    if director_movies.empty:
        raise HTTPException(status_code=404, detail=f"No se encontraron películas para el director {director_name}")

    # Obtener los movie_id de las películas dirigidas por el director
    movie_ids = director_movies['movie_id'].unique()

    # Filtrar df_movies_limpio por los movie_id obtenidos
    director_movies_details = df_movies_limpio[df_movies_limpio['movie_id'].isin(movie_ids)]

    # Calcular el retorno promedio en dólares de todas las películas del director
    avg_return_dollars = director_movies_details['return'] * director_movies_details['budget']
    avg_return_dollars = avg_return_dollars.mean()

    return {
        "director": director_name,
        "avg_return_dollars": avg_return_dollars,
        "peliculas": director_movies_details.to_dict(orient="records")
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
