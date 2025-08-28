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