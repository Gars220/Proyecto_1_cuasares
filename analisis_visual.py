import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Conectamos con el archivo .db creado anteriormente

conexion = sqlite3.connect('datos_mision.db')

# Hacemos la consulta SQL

consulta = "SELECT * FROM galaxies ORDER BY z ASC;"

# Ahora creamos el Dataframe de análisis

df_final = pd.read_sql_query(consulta, conexion)

# Cerramos la conexión por seguridad.

conexion.close()

# MOstramos los datos que aparecen en la terminal

m=10
print(f"Primeros {m} elementos extraídos")
print(df_final.head(n=m))

# Ahora veamos qué quásares hay respecto a galaxias:{
objetos = np.array(df_final['class'])

mask_qs = objetos  == 'QSO'
quasars = np.array(df_final['class'])[mask_qs]
print(f"Total de cuasares: {len(quasars)}")

# El número de galaxias

mask_gs = objetos == "GALAXY"
galaxs = np.array(df_final['class'])[mask_gs]
print(f"Total de galaxias: {len(galaxs)}")

# Usaremos estas máscaras para plotear de diferentes colores los objetos:

mag_gs = np.array(df_final['mag_g'])
mag_rs = np.array(df_final['mag_r'])
zs = np.array(df_final['z'])

#Filtramos las galaxias

mag_gs_gx = mag_gs[mask_gs]
mag_rs_gx = mag_rs[mask_gs]
zs_gx = zs[mask_gs]

# FIltramos los cuásares
mag_gs_qs = mag_gs[mask_qs]
mag_rs_qs = mag_rs[mask_qs]
zs_qs = zs[mask_qs]

# Calculamos índices de color g-r:

index_qs = mag_gs_qs - mag_rs_qs
index_gx = mag_gs_gx - mag_rs_gx

# Ahora podemos plotear:

plt.style.use("dark_background")

plt.figure(figsize=(8,6))
plt.scatter(zs_qs, index_qs, color='red', alpha=0.7)
plt.scatter(zs_gx, index_gx, color='blue', alpha=0.7)
plt.title("Distribución de galaxias y cuásares según el índice g-r")
plt.xlabel("Redshift (z)")
plt.ylabel("Índice g-r")
plt.grid()
plt.savefig("resultado.png")
