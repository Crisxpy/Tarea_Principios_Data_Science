import pandas as pd
import numpy as np
from DatosEstudiantes import estudiantes

# Convertir a DataFrame
df = pd.DataFrame(estudiantes)

# ¿Qué porcentaje de estudiantes tiene al menos una nota bajo 4.0?
df['tiene_bajo_4'] = df['notas'].apply(lambda notas: any(n < 4.0 for n in notas))
porcentaje_bajo_4 = df['tiene_bajo_4'].mean() * 100

print("Porcentaje con al menos una nota < 4.0:", round(porcentaje_bajo_4, 2), "%")