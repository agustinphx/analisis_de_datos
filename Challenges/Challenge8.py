"""
Escribir una funcion que reciba como parámetros: una variable de tipo DataFrame (la tabla de alumnos) y el índice de un alumno. 
Luego debe devolver con return el promedio de sus notas en las diferentes materias.
"""

import pandas as pd

dataframe = pd.read_excel("Datos.xlsx")

indice = int(input("Indique el alumno a evaluar: "))

data = dataframe.loc[indice]

for alumnos in range(len(data)):
	suma = (data["Quimica"] + data["Fisica"] + data["Matematica"])
	prom = suma / 3
	nom = data["Nombre"]

print("Promedio del alumno:",nom," es ",prom)

