import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Limpia el dataset aplicando las siguientes transformaciones:
    1. Elimina filas con valores vacíos en la columna 'Brand'.
    2. Elimina filas duplicadas.
    3. Convierte los nombres de las colunas a minúsculas en formato snake_case.

    :param df: DataFrame de Pandas con los datos de los vehículos.
    return: DataFrame limpio
    '''
    #Eliminar valores vacíos en la columna 'Brand'
    df = df.dropna(subset=['Brand'])

    #Eliminar filas duplicadas
    df = df.drop_duplicates()

    #Modificar nombres de columnas a snake_case
    df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')

    return df