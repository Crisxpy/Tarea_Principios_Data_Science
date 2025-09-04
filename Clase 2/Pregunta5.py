import pandas as pd
import numpy as np
from DatosEstudiantes import estudiantes

# Convertir a DataFrame
df = pd.DataFrame(estudiantes)
df['promedio'] = df['notas'].apply(np.mean)

# Entrega un listado ordenado (de mayor a menor) de los estudiantes según su promedio.
ordenados = df.sort_values(by='promedio', ascending=False)

print("Listado ordenado por promedio:")
print(ordenados[['nombre','promedio']])