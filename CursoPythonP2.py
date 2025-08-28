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

#PARTE 2.3
#Filtrar planes para las columnas que sean del tipo de datos "object"
#Recorrer las columnas del conjunto de datos
#Añadir el iterador de columna a la sentencia print y, a continuación, llama a la función para que devuelva el número de valores únicos de la columna
non_numeric = planes.select_dtypes("object")
for col in non_numeric.columns:
    print(f"Number of unique values in {col} column: ", non_numeric[col].nunique())

#PARTE 2.4
#Crear una lista de categorías que contenga "Short-haul", "Medium", y "Long-haul"
flight_categories = ["Short-haul", "Medium", "Long-haul"]

#Crear short_flights, una cadena para capturar valores de "0h", "1h", "2h", "3h", o "4h" teniendo cuidado de evitar valores como "10h"
#Crear medium_flights para capturar cualquier valor entre cinco y nueve horas
#Crear long_flights para capturar cualquier valor comprendido entre 10 y 16 horas, ambos inclusive
flight_categories = ["Short-haul", "Medium", "Long-haul"] 
short_flights = "^0h|^1h|^2h|^3h|^4h"
medium_flights = "^5h|^6h|^7h|^8h|^9h"
long_flights = "^10h|^11h|^12h|^13h|^14h|^15h|^16h"

#PARTE 2.5
#Crear conditions, una lista que contenga subconjuntos de planes["Duration"] basados en short_flights, medium_flights y long_flights
#Crear la columna "Duration_Category" llamando a una función que acepte tu lista conditions y flight_categories, estableciendo los valores no encontrados en "Extreme duration"
#Crear un gráfico que muestre el recuento de cada categoría
conditions = [
    (planes["Duration"].str.contains(short_flights)),
    (planes["Duration"].str.contains(medium_flights)),
    (planes["Duration"].str.contains(long_flights))
]

planes["Duration_Category"] = np.select(conditions, 
                                        flight_categories,
                                        default="Extreme duration")

sns.countplot(data=planes, x="Duration_Category")
plt.show()

#PARTE 2.6
#Imprimir los cinco primeros valores de la columna "Duration"
print(planes["Duration"].head())

#Retirar "h" de la columna
planes["Duration"] = planes["Duration"].str.replace("h", "")

#Convertir la columna al tipo de datos float.
planes["Duration"] = planes["Duration"].astype(float)

#Trazar un histograma de los valores de "Duration".
sns.histplot(data=planes, x="Duration", bins=20)
plt.show()

#PARTE 2.7
#Añadir una columna a planes que contenga la desviación típica de "Price" basada en "Airline"
planes["airline_price_st_dev"] = planes.groupby("Airline")["Price"].transform(lambda x: x.std())
print(planes[["Airline", "airline_price_st_dev"]].value_counts())

#Calcular la mediana de "Duration" en "Airline", almacenándola como una columna llamada "airline_median_duration"
planes["airline_median_duration"] = planes.groupby("Airline")["Duration"].transform(lambda x: x.median())
print(planes[["Airline","airline_median_duration"]].value_counts())

#Encontrar la media "Price" por "Destination", guardándola como una columna llamada "price_destination_mean"
planes["price_destination_mean"] = planes.groupby("Destination")["Price"].transform(lambda x: x.mean())
print(planes[["Destination","price_destination_mean"]].value_counts())

#PARTE 2.8
#TrazaR la distribución de la columna "Price" de planes
sns.histplot(data=planes, x="Price")
plt.show()

#Mostrar las estadísticas descriptivas de la duración del vuelo
print(planes["Duration"].describe())

#PARTE 2.9
#Hallar los percentiles 75 y 25, guardando como price_seventy_fifth y price_twenty_fifth respectivamente
price_seventy_fifth = planes["Price"].quantile(0.75)
price_twenty_fifth = planes["Price"].quantile(0.25)

#Calcular el IQR, almacenándolo como prices_iqr
prices_iqr = price_seventy_fifth - price_twenty_fifth

#Calcular los umbrales superior e inferior de valores atípicos
upper = price_seventy_fifth + (1.5 * prices_iqr)
lower = price_twenty_fifth - (1.5 * prices_iqr)

#Eliminar los valores atípicos de planes
planes = planes[(planes["Price"] > lower) & (planes["Price"] < upper)]
print(planes["Price"].describe())