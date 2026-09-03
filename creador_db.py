import sqlite3
import pandas as pd

# Leer el DataFrame y limpiarlo.

df1 = pd.read_csv("datos_sdss.csv", skiprows=1)

print("DataFrame sin limpiar")

df_limpio = df1.query("g > 0 and r > 0")

print("DataFrame filtrado")
print(len(df_limpio))

print("Aquí vamos a crear la base de datos")

# Definición de nobres y columnas:
db_name = "datos_mision.db"
table_name = "galaxies"

# Renombrar columnas del Dataframe:

df_limpio = df_limpio.rename(columns={
	'class': 'class',
	'z': 'z',
	'g': 'mag_g',
	'r': 'mag_r'
})

# 2. Conexión con la base de datos, creamos el archivo.

conexion = sqlite3.connect(db_name)

# 3. Creamos la tabla:

df_limpio.to_sql(name=table_name, con=conexion, if_exists='replace', index=False)


# 4. Guardar los cambios de estructura

conexion.close()

print(f"Base de datos '{db_name}' y tabla '{table_name}' creados con éxito.")
