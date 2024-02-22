"""    
Leer el archivo Tabla1.xlsx que contiene los puntos de un campeonato. 
El archivo tiene cuatro columnas, Equipo, Puntos, Goles a favor y Goles en contra. 
Determinar de cada equipo la diferencia de gol (goles a favor - goles en contra), y mostrar todas las diferencias de gol usando print.
"""

import pandas as pd

dataframe = pd.read_excel("Tabla1.xlsx")

data = dataframe.to_dict("list")

for equipo in range(len(data)):		
		diferencia = data["Goles a favor"][equipo]- data["Goles en contra"][equipo]
		print("Equipo ",equipo,"diferencia de goles: ",diferencia)
