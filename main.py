from fastapi import FastAPI, HTTPException
import pandas as pd
from modulos_endpoints import cantidad_filmaciones_mes, cantidad_filmaciones_dia, score_titulo, votos_titulo, get_actor, get_director

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "La API está en funcionamiento!"}

# Carga de datasets
df_movies_limpio = pd.read_csv(r"datos_procesados/movies_df.csv")
director_actor_df = pd.read_csv("datos_procesados/director_actor_df.csv", index_col=0)

# Endpoint cantidad_filmaciones_mes
app.get("/cantidad_filmaciones_mes/{mes}")(cantidad_filmaciones_mes)

# Endpoint peliculas_dia
app.get("/peliculas_dia/{dia}")(cantidad_filmaciones_dia)

# Endpoint score_titulo
app.get("/score_titulo/{titulo}")(score_titulo)

# Endpoint votos_titulo
app.get("/votos_titulo/{titulo}")(votos_titulo)

# Endpoint get_actor
app.get("/get_actor/{actor_name}")(get_actor)

# Endpoint get_director
app.get("/get_director/{director_name}")(get_director)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

