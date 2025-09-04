import pandas as pd
import numpy as np
from DatosEstudiantes import estudiantes

# Convertir a DataFrame
df = pd.DataFrame(estudiantes)

# Calcular promedios
df['promedio'] = df['notas'].apply(np.mean)

# Calcula el promedio de notas de cada estudiante y determina quién tiene el promedio más alto y más bajo.
mejor = df.loc[df['promedio'].idxmax()]
peor = df.loc[df['promedio'].idxmin()]

print("Promedio más alto:", mejor['nombre'], round(mejor['promedio'], 1))
print("Promedio más bajo:", peor['nombre'], round(peor['promedio'], 1))