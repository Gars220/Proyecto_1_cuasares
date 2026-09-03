# Proyecto 1: cuásares y galaxias
Primero proyecto del curso de Minería de Datos de la Universidad de Antioquia.

Este proyecto trata de analizar los cuásares y las galaxias a determinado
redshift (z). Para ello se accedió a la base de datos del SDSS a la cual
se hizo un SQL para bajar datos de cerca de 5000 galaxias, entre ellas
cuásares del universo temprano.

A continuación verás lo siguiente:

- Un archivo .gitignore que no permitirá cargar arvchivos .csv o .png.
- Un ejecutable de bash, descarga_datos.sh, el cual hará La consulta a
SDSS.
- Ejecuta primero el archivo creador_db.py para poder crear una base de
datos llamada datos_mision.db.
- Puedes ejecutar para ver el contendio de esta base de datos el archivo
de python grafica_previa.
- Finalmente el resultado del procesamiento será con analisis_visual.py.

Lo que hace primero creador_db.py es limpiar la base de datos de aquellos
que son incoherentes o extraños, como valores negativos u outlairs.

Para este trabajo trabajamos con magnitudes en los filtros g y r del SDSS
y queremos hallar el índice g-r, para ello este procedimiento se ejecuta
cuando corres analisis_visual.py. Aquí dentro entonces se hace el cálculo
del índice g-r y separa las galaxias de los cuásares, siendo los cuásares
puntos rojos y las galaxias azules.

Verás que al final los cuásares tienen un brillo que tiende a colores
rojizos, especialmente en el universo temprano. Además que éstos se ubican
hasta redshit cercano a 0.2.

Por otro lado las galaxias se ubican a partir de z < 1.0, más o menos,
y algunas tienen un brillo más azul.
