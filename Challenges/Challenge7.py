"""
Calcular el promedio de las notas de química de todos los alumnos en el archivo Datos.xlsx.
"""

import pandas as pd

dataframe = pd.read_excel("Datos.xlsx")

data = dataframe.to_dict("list")

for alumnos in range(len(data)):		
		suma = sum(data["Quimica"])
		prom = suma/6
print("Promedio de las notas en quimica de todos los alumnos: ",prom)
