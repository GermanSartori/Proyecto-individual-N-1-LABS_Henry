from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

#Carga de datasets
df_movies_limpio = pd.read_csv(r"E:\Repositorios y bases de datos\Henry DS\Proyecto-individual-N-1---LABS---Henry\datos_procesados\movies_df.csv")
director_actor_df = pd.read_csv(r"E:\Repositorios y bases de datos\Henry DS\Proyecto-individual-N-1---LABS---Henry\datos_procesados\director_actor_df.csv", index_col=0)

@app.get("/cantidad_filmaciones_mes/{mes}")
def cantidad_filmaciones_mes(mes: str):
    try:
        mes = mes.capitalize()
        df_movies_limpio['release_date'] = pd.to_datetime(df_movies_limpio['release_date'])
        df_movies_limpio['mes'] = df_movies_limpio['release_date'].dt.strftime('%B')
        count = df_movies_limpio[df_movies_limpio['mes'] == mes].shape[0]
        return {"mes": mes, "cantidad": count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/peliculas_dia/{dia}")
def peliculas_dia(dia: str):
    try:
        dia = dia.capitalize()
        df_movies_limpio['release_date'] = pd.to_datetime(df_movies_limpio['release_date'])
        df_movies_limpio['dia'] = df_movies_limpio['release_date'].dt.strftime('%A')
        count = df_movies_limpio[df_movies_limpio['dia'] == dia].shape[0]
        return {"dia": dia, "cantidad": count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/score_titulo/{titulo}")
def score_titulo(titulo: str):
    try:
        pelicula = df_movies_limpio[df_movies_limpio['title'] == titulo].iloc[0]
        return {
            "titulo": titulo,
            "fecha_lanzamiento": pelicula['release_date'],
            "score": pelicula['vote_average']
        }
    except IndexError:
        raise HTTPException(status_code=404, detail="Película no encontrada")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/votos_titulo/{titulo}")
def votos_titulo(titulo: str):
    try:
        pelicula = df_movies_limpio[df_movies_limpio['title'] == titulo].iloc[0]
        if pelicula['vote_count'] < 2000:
            return {"titulo": titulo, "mensaje": "La película no cumple con el criterio de más de 2000 votos"}
        return {
            "titulo": titulo,
            "fecha_lanzamiento": pelicula['release_date'],
            "votos": pelicula['vote_count'],
            "score": pelicula['vote_average']
        }
    except IndexError:
        raise HTTPException(status_code=404, detail="Película no encontrada")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_actor/{actor_name}")
def get_actor(actor_name: str):
    try:
        actor_movies = director_actor_df[(director_actor_df['actor'] == actor_name) & (director_actor_df['director'] != actor_name)]
        if actor_movies.empty:
            raise HTTPException(status_code=404, detail="Actor no encontrado o también es director")

        total_movies = len(actor_movies)
        total_revenue = actor_movies['revenue'].sum()
        average_return = actor_movies['return'].mean()

        return {
            "actor": actor_name,
            "total_movies": total_movies,
            "total_revenue": total_revenue,
            "average_return": average_return
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_director/{director_name}")
def get_director(director_name: str):
    try:
        director_movies = director_actor_df[director_actor_df['director'] == director_name]
        if director_movies.empty:
            raise HTTPException(status_code=404, detail="Director no encontrado")

        total_revenue = director_movies['revenue'].sum()
        average_return = director_movies['return'].mean()
        movies_details = director_movies[['title', 'release_date', 'budget', 'revenue']].to_dict(orient='records')

        return {
            "director": director_name,
            "total_revenue": total_revenue,
            "average_return": average_return,
            "movies": movies_details
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
