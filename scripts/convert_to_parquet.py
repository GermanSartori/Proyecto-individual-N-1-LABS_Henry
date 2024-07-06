import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

def convert_to_parquet(input_file, output_parquet, file_type='csv'):
    # Cargar el DataFrame desde el archivo según el tipo
    if file_type == 'csv':
        df = pd.read_csv(input_file, low_memory=False)
        # Intentar convertir la columna 'popularity' a float
        df['popularity'] = pd.to_numeric(df['popularity'], errors='coerce')
    elif file_type == 'excel':
        df = pd.read_excel(input_file)
    else:
        raise ValueError("Tipo de archivo no soportado. Use 'csv' o 'excel'.")

    # Convertir DataFrame a formato Parquet y guardar
    table = pa.Table.from_pandas(df)
    pq.write_table(table, output_parquet)

    print(f"Archivo convertido a Parquet: {output_parquet}")

if __name__ == "__main__":
    # Rutas de archivo para los DataFrames de merged y movies
    merged_parq = r'E:\Repositorios y bases de datos\Henry DS\Proyecto final 1 - LABS\archivos VSC\merged_df.xlsx'
    merged_parq_output = r'E:\Repositorios y bases de datos\Henry DS\Proyecto final 1 - LABS\archivos VSC\merged_df.parquet'

    movies_parq = r'E:\Repositorios y bases de datos\Henry DS\Proyecto final 1 - LABS\datos\movies_dataset.csv'
    movies_parq_output = r'E:\Repositorios y bases de datos\Henry DS\Proyecto final 1 - LABS\datos\movies_dataset.parquet'

    # Convertir los archivos a Parquet
    convert_to_parquet(merged_parq, merged_parq_output, file_type='excel')
    convert_to_parquet(movies_parq, movies_parq_output, file_type='csv')
