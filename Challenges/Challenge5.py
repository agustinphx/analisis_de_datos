"""
Llévame en tu bicicleta.

El gobierno de la Ciudad de Buenos Aires recolecta datos acerca del uso de los servicios de bicicletas públicas (ecobici) y publica parte de ellos:
Elemento de la lista
Elemento de la lista

Para este ejemplo usaremos los primeros 10000 viajes de la base de datos del 2021.

Se quiere conocer más acerca del uso que le dan los usuarios al sistema, por lo cual su tarea será extraer la siguiente información:

¿Qué porcentaje de los viajes se completaron en estado NORMAL?

¿Cuál es la duración promedio de cada viaje? (Los datos están en segundos)

¿A qué hora del día se realizaron más viajes? (por ejemplo: de 16hs a 17hs)

¿Cuántas estaciones diferentes fueron utilizadas?

Para cada estación utilizada como inicio de un viaje, imprimirlas ordenadas por cantidad de viajes que iniciaron de la misma.
"""

import pandas as pd

dataframe = pd.read_csv("Rec_bicis_2021.csv")

data = dataframe.to_dict("list")

pd.set_option("display.max_rows",10)

print(dataframe)
