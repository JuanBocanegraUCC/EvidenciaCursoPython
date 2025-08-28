import pandas as pd

#PARTE 3
#Importar divorce.csv, guardando como DataFrame, divorce; indica en la función de importación que las columnas divorce_date, dob_man, dob_woman, y marriage_date deben importarse como valores DateTime.
divorce = pd.read_csv(
    "divorce.csv",
    parse_dates=["divorce_date", "dob_man", "dob_woman", "marriage_date"]
)

print(divorce.dtypes)

#PARTE 3.1
#Convertir la columna marriage_date del DataFrame divorce en valores de DateTime
divorce["marriage_date"] = pd.to_datetime(divorce["marriage_date"])

#PARTE 3.2
#Definir una columna llamada marriage_year, que solo contiene la parte del año de la columna marriage_date
divorce["marriage_year"] = divorce["marriage_date"].dt.year

#Crear un gráfico de líneas que muestre el número medio de hijos que tuvo una pareja durante su matrimonio, ordenado por el año en que la pareja se casó
sns.lineplot(x="marriage_year", y="num_kids", data=divorce)
plt.show()

#PARTE 3.3
#Crear un diagrama de dispersión que muestre marriage_duration en el eje x y num_kids en el eje y
sns.scatterplot(x="marriage_duration", y="num_kids", data=divorce)
plt.show()

#PARTE 3.4
#Crear un diagrama de pares para visualizar las relaciones entre income_woman y marriage_duration en el DataFrame divorce
sns.pairplot(data=divorce, vars=["income_woman", "marriage_duration"])
plt.show()

#PARTE 3.5
#Crear un gráfico de dispersión que muestre woman_age_marriage en el eje de abscisas y income_woman en el eje de ordenadas; cada punto de datos debe colorearse en función del nivel educativo de la mujer, representado por education_woman
sns.scatterplot(x="woman_age_marriage", y="income_woman", hue="education_woman", data=divorce)
plt.show()

#PARTE 3.6
#Crear un gráfico KDE que muestre marriage_duration en el eje x y una línea de color diferente para cada posible número de hijos que pueda tener una pareja, representada por num_kids
sns.kdeplot(x="marriage_duration", hue="num_kids", data=divorce, common_norm=False)
plt.show()

#Observar que el gráfico muestra actualmente duraciones del matrimonio inferiores a cero; actualizar el gráfico KDE para que la duración del matrimonio no pueda suavizarse más allá de los puntos de datos extremos
sns.kdeplot(data=divorce, x="marriage_duration", hue="num_kids", cut=0)

#Actualizar el código del gráfico KDE del paso anterior para que muestre una función de distribución acumulativa para cada número de hijos que tiene una pareja
sns.kdeplot(data=divorce, x="marriage_duration", hue="num_kids", cut=0, cumulative=True)
plt.show()