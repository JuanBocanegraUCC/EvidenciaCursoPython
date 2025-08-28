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
