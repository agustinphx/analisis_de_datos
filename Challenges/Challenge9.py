"""
Obtener la suma total de las notas, la cantidad de aprobados y  
el promedio general sólo para aquellos alumnos que aprobaron Fisica en el archivo Datos.xlsx.
"""

import pandas as pd

dataframe = pd.read_excel("Datos.xlsx")

aprob = 0	
suma = 0
for alumnos in range(len(dataframe)):
	if dataframe["Fisica"][alumnos] >= 4:
		suma += dataframe["Fisica"][alumnos]
		aprob += 1
prom = suma / aprob		
print("Suma total: ",suma)	
print("Cantidad aprobados en fisica:",aprob,"\nPromedio: ",prom)
