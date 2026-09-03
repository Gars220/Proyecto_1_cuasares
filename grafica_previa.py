 
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
