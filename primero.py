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
df = df.dropna()
#para los datos duplicados igual lo quitamos
df = df.drop_duplicates()
#Tranformamo dato, además de agregar las columnas
df_dummies = pd.get_dummies(df, dummy_na = True)
print(df_dummies)
#guardamos datos limpios
df.to_csv("datos moviles limpios.csv", index=False)