import pandas as pd

#PARTE 2
#Imprimir el número de valores perdidos en cada columna del DataFrame
print(planes.isna().sum())

#Calcular a cuántas observaciones equivale el cinco por ciento del DataFrame planes
print(planes.isna().sum())
threshold = planes.shape[0] * 0.05
print(threshold)

#Crear cols_to_drop aplicando una indexación booleana a las columnas del DataFrame con valores perdidos menores o iguales que el umbral
#Utilizar este filtro para eliminar los valores que faltan y guardar el DataFrame actualizado
print(planes.isna().sum())
threshold = len(planes) * 0.05
cols_to_drop = planes.columns[planes.isna().sum() <= threshold]
planes.dropna(subset=cols_to_drop, inplace=True)

print(planes.isna().sum())

#PARTE 2.1
#Imprimir los valores y frecuencias de "Additional_Info"
print(planes["Additional_Info"].value_counts())

#Crear un boxplot de "Price" frente a "Airline"
print(planes["Additional_Info"].value_counts())
sns.boxplot(data=planes, x="Airline", y="Price")
plt.show()

#PARTE 2.2
#Agrupar planes por aerolínea y calcula el precio mediano
airline_prices = planes.groupby("Airline")["Price"].median()
print(airline_prices)

#Convertir los precios medios agrupados en un diccionario
airline_prices = planes.groupby("Airline")["Price"].median()
print(airline_prices)
prices_dict = airline_prices.to_dict()
print(prices_dict)

#Imputar condicionalmente los valores perdidos de "Price" asignando los valores de la columna "Airline" en función de prices_dict
#Comprobar si faltan valores
airline_prices = planes.groupby("Airline")["Price"].median()
print(airline_prices)
prices_dict = airline_prices.to_dict()
planes["Price"] = planes["Price"].fillna(planes["Airline"].map(prices_dict))
print(planes.isna().sum())
