"""
Se pide realizar un gráfico del valor del Bitcoin de los últimos 10 años, marcar con un punto el valor máximo del gráfico, calcular cuándo sucedió.
"""
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import pandas as pd
import numpy as np
import time

dataframe = pd.read_csv("BTC.csv")

data = dataframe.to_dict("list")

cant = len(data["Date"])

x = []
y = []

Max_precio = 0

Dia_record = " "

for i in range (cant):
	x.append(data["Date"][i])
	y.append(data["Open"][i])
	
	if y[i] > Max_precio:
		Max_precio = y[i]
		Dia_record = x[i]

print("El precio mas alto fue de:  $",Max_precio,"  el dia ",Dia_record)
record_label = 'Precio Record: {}\nDía del record: {}'.format(Max_precio, Dia_record)

plt.figure(figsize=(12, 4))
plt.plot(x,y)
plt.plot(Dia_record,Max_precio, 'ko', label = record_label)
plt.xticks(x[ : :200]) # Mostrar una de cada 200 fechas
plt.grid( axis='y' )   # Mostrar lineas horizontales detrás del gráfico
plt.legend()           # Mostrar etiquetas
plt.show()


