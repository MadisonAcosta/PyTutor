#primero importamos las libreerias a usar
import pandas as pd
import numpy as np

#cargamos el arvhico subido
df = pd.read_csv("moviles.csv")

#imprimimos
#inciamos exploracion
print(df.head())# primeras filas

print(df.info())#estructura de dataframe

print(df.describe())

#pa manejar debemos identifica
print(df.isnull().sum())

#para manejar los valores que faltan las vamos a quita
df = df.dropna(axis=1, how="all")
df = df.dropna(axis=0, how="all")

numeric_df = df.select_dtypes(include=[np.number])  # Solo columnas numéricas
column_means = numeric_df.mean()

# Calculamos la media de cada columna
#dentificamos columnas donde la media no es significativa 
columns_to_drop = column_means[column_means.isna() | (column_means == 0)].index
df = df.drop(columns=columns_to_drop)

#para los datos duplicados igual lo quitamos
df = df.drop_duplicates()

#Tranformamo dato, además de agregar las columnas
df_dummies = pd.get_dummies(df, dummy_na = True)
print(df_dummies)

#guardamos datos limpios
df.to_csv("datos moviles limpios.csv", index=False)

# Mostrar todas las filas y columnas
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print(df)