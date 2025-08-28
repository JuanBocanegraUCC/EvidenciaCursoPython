import pandas as pd

#PARTE 1
#Función pandas para imprimir las cinco primeras filas del Dataframe
print(unemployment.head())

#Función pandas para imprimir un resumen de valores  y tipos de datos de las columnas que no faltan del Dataframe
print(unemployment.info())

#Imprimir las estadísticas de resumen de cada columna numérica
print(unemployment.describe())


#PARTE 1.1
#Utilizar un método para contar los valores asociados a cada campo especificado del Dataframe
print(unemployment["continent"].value_counts())


#PARTE 1.2
#Importa las bibliotecas de visualización necesarias
#Crear un histograma de la distribución de los porcentajes de desempleo de 2021 en todos los paises; muestra un punto porcentual completo en cada casilla
import seaborn as sns
import matplotlib.pyplot as plt

# Histograma de desempleo en 2021
sns.histplot(data=unemployment, x="2021", binwidth=1)

plt.title("Distribución del desempleo mundial en 2021")
plt.xlabel("Tasa de desempleo (%)")
plt.ylabel("Número de países")
plt.show()

#PARTE 1.3
#Actualizar el tipo de datos de la columna 2019 a float
unemployment["2019"] = unemployment["2019"].astype(float)
print(unemployment.dtypes)

#PARTE 1.4
#Describir una serie de booleanos que describan si cada continent está o no fuera de Oceania, llamar a esa serie not_oceania
not_oceania = unemployment["continent"] != "Oceania"

#Utilizar la indexación booleana para imprimir el DataFrame sin ninguno de los datos relacionados con los países de Oceanía
not_oceania = ~unemployment["continent"].isin(["Oceania"])
print(unemployment[not_oceania])

#PARTE 1.5
#Imprimir las tasas de desempleo mínima y máxima, en ese orden, durante 2021
#Crea un diagrama de caja de las tasas de desempleo de 2021 (en el eje x), desglosadas por continente (en el eje y)
print(unemployment["2021"].min(), unemployment["2021"].max())
sns.boxplot(x="2021", y="continent", data=unemployment)
plt.show()

#PARTE 1.6
#Imprimir la media y la desviación estándar de las tasas de paro para 2019 y 2020
print(unemployment[["2019", "2020"]].agg(["mean", "std"]))

#Imprimir la media y la desviación estándar de las tasas de desempleo para 2019 y 2020, agrupadas por continente
print(unemployment[["continent", "2019", "2020"]].groupby("continent").agg(["mean", "std"]))

#PARTE 1.7
#Crear una columna llamada mean_rate_2021 que muestre la tasa de paro media de 2021 para cada continente.
#Crear una columna llamada std_rate_2021 que muestre la desviación típica de la tasa de paro de 2021 para cada continente.
continent_summary = unemployment.groupby("continent").agg(
    mean_rate_2021=("2021", "mean"),
    std_rate_2021=("2021", "std")
)
print(continent_summary)

#PARTE 1.8
#Crear un diagrama de barras que muestre los continentes en el eje x y sus respectivas tasas medias de desempleo en 2021 en el eje y
import seaborn as sns
import matplotlib.pyplot as plt

sns.barplot(x="continent", y="2021", data=unemployment)
plt.show()