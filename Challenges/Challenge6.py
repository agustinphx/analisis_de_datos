"""
Leer el archivo Tabla1.xlsx que contiene los puntos de un campeonato y determinar qué equipo es el campeón (1ro) y perdedor (último). 
El archivo tiene cuatro columnas, Equipo, Puntos, Goles a favor y Goles en contra.
"""

import pandas as pd

dataframe = pd.read_excel("Tabla1.xlsx")

data = dataframe.to_dict("list")

Max = 0
Min = 9999

for equipo in range(len(data)):		
	if data["Puntos"][equipo] > Max:
		Max = data["Puntos"][equipo]
		NomMax = data["Equipo"][equipo]
	else: 
		Min = data["Puntos"][equipo]
		NomMin = data["Equipo"][equipo]

print("Equipo campeón:",NomMax," con ",Max," puntos")
print("Equipo perdedor:",NomMin," con ",Min," puntos")
