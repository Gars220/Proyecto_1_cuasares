#!/bin/bash

# 1. Consulta SQL a la base de datos SDSS:
#Aquí le decimos que seleccione las priemras 5000 galaxias, que tome los filtros
# g y r
QUERY="SELECT%20TOP%205000%20s.class,p.g,p.r,s.z%20FROM%20SpecObjAll%20AS%20s%20JOIN%20PhotoObjAll%20AS%20p%20ON%20s.bestObjID=p.objID%20WHERE%20s.class='QSO'%20OR%20s.class='GALAXY'"

# 2. Unimos la URL con la consulta anterior:
URL="https://skyserver.sdss.org/dr18/SkyServerWS/SearchTools/SqlSearch?format=csv&cmd=${QUERY}"

# 3. Descarga datos con wget
wget -O datos_sdss.csv "$URL"

echo "Descarga finalizada"

# Ahora bien veamos qué son esos datos que hay allí:

cat << 'EOF' > grafica_previa.py
 
import pandas as pd
import matplotlib.pyplot as plt

# Leemos el csv generado anteriormente con las galaxias

df0 = pd.read_csv("datos_sdss.csv", skiprows=1)

# Ahora graficamos

plt.figure(figsize=(8,5))
plt.scatter(df0['z'], df0['g'], color='g')
plt.title("Galaxias observadas en G en función de z")
plt.xlabel("z")
plt.ylabel("Mag G")
plt.savefig("grafico_magg.png")

print("Plot del filtro G")

plt.figure(figsize=(8,5))
plt.scatter(df0['z'], df0['r'], color='r')
plt.title("Galaxias observadas en R en función de z")
plt.xlabel("z")
plt.ylabel("Mag R") 
plt.savefig("grafico_magr.png")
print("Plot del filtro R")
EOF

# Ejecutamos el script de python:
python3 grafica_previa.py
