from fastapi import FastAPI, HTTPException
import pandas as pd
from modulos import cantidad_filmaciones_mes, cantidad_filmaciones_dia, score_titulo, votos_titulo, get_actor, get_director
import os
import uvicorn


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "La API está en funcionamiento!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))



# Carga de datasets
current_dir = os.path.dirname(os.path.abspath(__file__))

movies_path = os.path.join(current_dir, "datos_procesados", "movies_df.csv")

director_actor_path = os.path.join(current_dir, "datos_procesados", "director_actor_df.csv")




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




