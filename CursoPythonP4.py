import pandas as pd

#PARTE 4
#Imprimir la frecuencia relativa de la columna "Job_Category" de salaries DataFrame
print(salaries["Job_Category"].value_counts(normalize=True))

#PARTE 4.1
#Realizar una tabulación cruzada, estableciendo "Company_Size" como índice, y las columnas a las clases en "Experience"
print(pd.crosstab(salaries["Company_Size"], salaries["Experience"]))

#Cruzar "Job_Category" y las clases de "Company_Size" como nombres de columna
print(pd.crosstab(salaries["Job_Category"], salaries["Company_Size"]))

#Actualizar pd.crosstab() para que devuelva los valores medios de "Salary_USD"
print(pd.crosstab(salaries["Job_Category"], salaries["Company_Size"],
                  values=salaries["Salary_USD"], aggfunc="mean"))

#PARTE 4.2
#Extraer el mes de "date_of_response", almacenándolo como una columna llamada "month"
#Crear la columna "weekday", que contiene el día de la semana en que los participantes completaron la encuesta
#Trazar un mapa de calor, incluyendo las puntuaciones del coeficiente de correlación de Pearson
salaries["month"] = salaries["date_of_response"].dt.month
salaries["weekday"] = salaries["date_of_response"].dt.weekday
sns.heatmap(salaries.corr(numeric_only=True), annot=True)
plt.show()

#PARTE 4.3
#Hallar el percentil 25 de "Salary_USD"
#Guardar la mediana de "Salary_USD" como salaries_median
#Obtener el percentil 75 de los salarios
twenty_fifth = salaries["Salary_USD"].quantile(0.25)
salaries_median = salaries["Salary_USD"].median()
seventy_fifth = salaries["Salary_USD"].quantile(0.75)
print(twenty_fifth, salaries_median, seventy_fifth)

#PARTE 4.4
#Crear salary_labels, una lista que contenga "entry", "mid", "senior", y "exec"
salary_labels = ["entry", "mid", "senior", "exec"]

#Terminar salary_ranges, añadiendo el percentil 25, la mediana, el percentil 75 y el valor más grande de "Salary_USD"
salary_ranges = [0, twenty_fifth, salaries_median, seventy_fifth, salaries["Salary_USD"].max()]

#Dividir "Salary_USD" en función de las etiquetas y rangos que hayas creado
salaries["salary_level"] = pd.cut(salaries["Salary_USD"],
                                  bins=salary_ranges,
                                  labels=salary_labels)

#Utilizar sns.countplot() para visualizar el recuento de "Company_Size", factorizando las etiquetas de nivel salarial
sns.countplot(data=salaries, x="Company_Size", hue="salary_level")
plt.show()
