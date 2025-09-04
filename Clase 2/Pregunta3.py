import pandas as pd
import numpy as np
from DatosEstudiantes import estudiantes

# Convertir a DataFrame
df = pd.DataFrame(estudiantes)

# ¿Cuál es la nota más frecuente (moda) considerando todas las notas de todos los estudiantes?
todas_las_notas = np.concatenate(df['notas'].values)
moda = pd.Series(todas_las_notas).mode().iloc[0]

print("Nota más frecuente (moda):", moda)