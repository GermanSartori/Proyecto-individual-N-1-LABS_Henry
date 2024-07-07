import pandas as pd
import calendar
import locale
import pyarrow.parquet as pq  # Importar para leer archivos Parquet


#Carga de datasets
df_movies_limpio = pd.read_csv(r"E:\Repositorios y bases de datos\Henry DS\Proyecto-individual-N-1---LABS---Henry\datos_procesados\movies_df.csv")
director_actor_df = pd.read_csv(r"E:\Repositorios y bases de datos\Henry DS\Proyecto-individual-N-1---LABS---Henry\datos_procesados\director_actor_df.csv", index_col=0)




df_movies_limpio['release_date'] = pd.to_datetime(df_movies_limpio['release_date'], errors='coerce')

# Eliminación de filas con fechas no válidas
df_movies_limpio = df_movies_limpio.dropna(subset=['release_date'])


#===================================
def cantidad_filmaciones_mes(mes):
    # Filtro películas por el mes especificado
    filtered_movies = df_movies_limpio[df_movies_limpio['release_date'].dt.month_name(locale='es_ES').str.lower() == mes.lower()]
    
    # Recuento la cantidad de películas filtradas
    cantidad = filtered_movies.shape[0]
    
    return cantidad

# Llamado a la función cantidad_filmaciones_mes con el mes 'enero'
cantidad_enero = cantidad_filmaciones_mes('enero')
print(f'Cantidad de películas estrenadas en enero: {cantidad_enero}')

# Llamado a la función cantidad_filmaciones_mes con el mes 'febrero'
cantidad_febrero = cantidad_filmaciones_mes('febrero')
print(f'Cantidad de películas estrenadas en febrero: {cantidad_febrero}')



#===================================



# Definición de la función cantidad defilmaciones por dia
def cantidad_filmaciones_dia(dia):
    # Converción de la columna de fechas a tipo datetime si aún no lo está
    df_movies_limpio['release_date'] = pd.to_datetime(df_movies_limpio['release_date'], errors='coerce')
    
    # Filtro de películas por el día especificado
    filtered_movies = df_movies_limpio[df_movies_limpio['release_date'].dt.day == dia]
    
    # Recuento de la cantidad de películas filtradas
    cantidad = filtered_movies.shape[0]
    
    return cantidad

# Prueba de la función con diferentes días
dias_a_consultar = [1, 15, 31]  

for dia in dias_a_consultar:
    cantidad = cantidad_filmaciones_dia(dia)
    print(f'Cantidad de películas estrenadas el día {dia}: {cantidad}')



#===================================




# Definición de la función score por titulo
def score_titulo(titulo):
    # Conversión de la columna de fechas a tipo datetime
    df_movies_limpio['release_date'] = pd.to_datetime(df_movies_limpio['release_date'], errors='coerce')
    
    # Filtro de película por título
    filtered_movie = df_movies_limpio[df_movies_limpio['title'].str.lower() == titulo.lower()]
    
    # Obtener título, año de estreno y score
    if not filtered_movie.empty:
        titulo = filtered_movie.iloc[0]['title']
        año_estreno = filtered_movie.iloc[0]['release_date'].year
        score = filtered_movie.iloc[0]['vote_average']  
        return f'La película `{titulo}` fue estrenada en el año `{año_estreno}` con un score/popularidad de `{score}`'
    else:
        return f'No se encontró la película con título `{titulo}` en el dataset'

# Ejemplo de uso de la función score_titulo
titulo_buscar = 'Avatar'  
resultado = score_titulo(titulo_buscar)
print(resultado)





#===================================





# Definición de la función votos_titulo
def votos_titulo(titulo):
    # Filtro de película por título
    filtered_movie = df_movies_limpio[df_movies_limpio['title'].str.lower() == titulo.lower()]
    
    # Verificación si se encontró la película y tiene al menos 2000 votos
    if not filtered_movie.empty:
        cantidad_votos = filtered_movie.iloc[0]['vote_count']
        promedio_votos = filtered_movie.iloc[0]['vote_average']
        
        if cantidad_votos >= 2000:
            return f'La película `{titulo}` fue estrenada en el año `{filtered_movie.iloc[0]["release_date"].year}`. La misma cuenta con un total de `{cantidad_votos}` valoraciones, con un promedio de `{promedio_votos}`.'
        else:
            return f'La película `{titulo}` fue estrenada en el año `{filtered_movie.iloc[0]["release_date"].year}`. Sin embargo, no cumple con la condición de tener al menos 2000 valoraciones.'
    else:
        return f'No se encontró la película con título `{titulo}` en el dataset'

# Ejemplo de uso de la función votos_titulo
titulo_buscar = 'Avatar'  
resultado = votos_titulo(titulo_buscar)
print(resultado)




#===================================






def get_actor(nombre_actor, df_movies_limpio, director_actor_df):
    nombre_actor = nombre_actor.lower()
    
    # Verificación si el actor existe en el DataFrame director_actor_df como actor
    actor_presente = director_actor_df['actor'].apply(lambda lista_actores: any(nombre_actor in actor.lower() for actor in lista_actores) if isinstance(lista_actores, list) else False)
    
    if not actor_presente.any():
        return f"{nombre_actor} no ha participado en ninguna película."
    
    # Verificación si el actor también es director en alguna película del director_actor_df
    director_presente = director_actor_df['director'].apply(lambda director: nombre_actor in director.lower() if isinstance(director, str) else False)
    
    if director_presente.any():
        return 0
    
    # Obtención de las películas en las que el actor ha participado como actor
    df_actor = director_actor_df[actor_presente]
    
    # Calculo del retorno total y promedio si 'return' está en df_movies_limpio
    if 'return' in df_movies_limpio.columns:
        # Filtro de las películas en las que el actor ha participado como actor
        df_actor_movies = df_movies_limpio[df_movies_limpio['movie_id'].isin(df_actor['movie_id'])]
        
        #if df_actor_movies.empty:
        #    return f"El actor {nombre_actor.capitalize()} ha participado en {df_actor.shape[0]:,} filmaciones, pero no hay información sobre el retorno de las películas."
        
        # Calculo del retorno total y promedio en dólares
        df_actor_movies.loc[:, 'return_dollars'] = df_actor_movies['return'] * df_actor_movies['budget']
        retorno_total_dollars = df_actor_movies['return_dollars'].sum()
        retorno_promedio_dollars = df_actor_movies['return_dollars'].mean()
        
        # Formateo de los números con puntos cada tres dígitos y sin decimales
        retorno_total_formatted = locale.format_string("%d", retorno_total_dollars, grouping=True)
        retorno_promedio_formatted = locale.format_string("%d", retorno_promedio_dollars, grouping=True)
        
        cantidad_filmaciones = df_actor.shape[0]
        return (f"{nombre_actor.capitalize()} ha participado en {cantidad_filmaciones:,} filmaciones. "
                f"Ha conseguido un retorno total de ${retorno_total_formatted} con un promedio de ${retorno_promedio_formatted} por filmación en dólares.")
    #else:
    #   return "No se puede calcular el retorno total y promedio porque 'return' no está presente en df_movies_limpio."

# Configuración de la localización para el formato de números
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

# Ejemplo de uso con df_movies_limpio y director_actor_df:
nombre_actor = 'Adam Sandler'
resultado_actor = get_actor(nombre_actor, df_movies_limpio, director_actor_df)
print(resultado_actor)





#===================================




def get_director(nombre_director):
    # Filtroo del DataFrame director_actor_df por el nombre del director
    director_movies = director_actor_df[director_actor_df['director'] == nombre_director]
    
    # Verificación si el director tiene películas en el dataset
    if director_movies.empty:
        return f"No se encontraron películas para el director {nombre_director}"
    
    # Obtención de los movie_id de las películas dirigidas por el director
    movie_ids = director_movies['movie_id'].unique()
    
    # Filtro del df_movies_limpio por los movie_id obtenidos
    director_movies_details = df_movies_limpio[df_movies_limpio['movie_id'].isin(movie_ids)]
    
    # Calculo del retorno en dólares (revenue - budget)
    director_movies_details['return_dollars'] = director_movies_details['revenue'] - director_movies_details['budget']
    
    # Calculo del retorno promedio en dólares de todas las películas del director
    avg_return_dollars = director_movies_details['return_dollars'].mean()
    
    # Formateo de los valores numéricos como dólares
    def format_dollars(value):
        return f"${value:,.0f}"
    
    director_movies_details['budget'] = director_movies_details['budget'].apply(format_dollars)
    director_movies_details['revenue'] = director_movies_details['revenue'].apply(format_dollars)
    director_movies_details['return_dollars'] = director_movies_details['return_dollars'].apply(format_dollars)
    
    # Eliminación de la hora del día de la fecha de lanzamiento
    director_movies_details['release_date'] = pd.to_datetime(director_movies_details['release_date']).dt.date
    
    # Preparación del texto para cada película
    peliculas_info = []
    for index, row in director_movies_details.iterrows():
        pelicula_info = (
            f"Título: {row['title']}\n"
            f"Fecha de Lanzamiento: {row['release_date']}\n"
            f"Retorno en Dólares: {row['return_dollars']}\n"
            f"Presupuesto: {row['budget']}\n"
            f"Ingresos: {row['revenue']}\n"
            f"Calificación Promedio: {row['vote_average']}\n"
            "----------------------------------------"
        )
        peliculas_info.append(pelicula_info)
    
    # Creación del diccionario de respuesta
    resultado = {
        'director': nombre_director,
        'retorno_promedio': format_dollars(avg_return_dollars),
        'peliculas': peliculas_info
    }
    
    return resultado

# Prueba de la función con un ejemplo
nombre_director_ejemplo = 'Steven Spielberg'  
resultado = get_director(nombre_director_ejemplo)

# Imprimir los resultados
print(f"Director: {resultado['director']}")
print(f"Retorno Promedio: {resultado['retorno_promedio']}")
print("Detalles de las películas:")
print("----------------------------------------")
for pelicula_info in resultado['peliculas']:
    print(pelicula_info)