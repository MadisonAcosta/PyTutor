# Importamos pandas y numpy
import pandas as pd
import numpy as np

# Cargamos el archivo con el separador correcto
df = pd.read_csv("moviles.csv", sep=";")

# Verificamos los nombres de las columnas
print("Columnas del DataFrame:", df.columns)

# Función para verificar si una columna está vacía (todos los valores son nulos o cadenas vacías)
def is_empty_column(column):
    """
    Verifica si una columna está compuesta solo por cadenas vacías o valores nulos.
    """
    return all(pd.isna(cell) or (isinstance(cell, str) and cell.strip() == "") for cell in column)


# Elimina columnas que están completamente vacías
columns_to_drop = [col for col in df.columns if is_empty_column(df[col])]
df = df.drop(columns=columns_to_drop)

# Elimina filas donde TODOS los valores son nulos o cadenas vacías
df = df.dropna(how="all")

# Elimina filas con demasiados valores vacíos o espacios en blanco
# Definimos un umbral (por ejemplo, si más del 50% de los valores en una fila están vacíos, la eliminamos)
umbral = 0.6  # 50% de los valores en la fila
df = df[df.apply(lambda row: row.notna().sum() / len(row) >= umbral, axis=1)]

# Elimina columnas numéricas con media nula o cero
numeric_df = df.select_dtypes(include=[np.number])
column_means = numeric_df.mean()
columns_to_drop = column_means[column_means.isna() | (column_means == 0)].index
df = df.drop(columns=columns_to_drop)

# Elimina filas duplicadas
df = df.drop_duplicates()

# Verificamos nuevamente los nombres de las columnas después de la limpieza
print("Columnas después de la limpieza:", df.columns)

# Ordenamos el DataFrame por las columnas deseadas (solo las que existen)
columnas_ordenar = [col for col in ["Nombre", "RAM", "Almacenamiento", "Pulgadas", "Valoracion"] if col in df.columns]
df = df.sort_values(by=columnas_ordenar, ascending=[True] * len(columnas_ordenar))

# Guardamos los datos limpios y ordenados
df.to_csv("datos_moviles_limpios.csv", index=False, encoding='utf-8')

# Mostramos el DataFrame completo
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(df)