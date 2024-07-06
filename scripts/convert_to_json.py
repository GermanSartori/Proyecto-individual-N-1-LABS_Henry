import pandas as pd
import json

# Lee tu archivo parquet
merged_df = pd.read_parquet(r'E:\Repositorios y bases de datos\Henry DS\Proyecto final 1 - LABS\archivos VSC\merged_df.parquet')

# Convierte el DataFrame a JSON
json_data = merged_df.to_json(orient='split')

# Guarda el JSON en un nuevo archivo
with open('merged_data.json', 'w') as f:
    json.dump(json_data, f)

print("Conversión completada. El archivo merged_data.json ha sido creado.")