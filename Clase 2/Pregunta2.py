import pandas as pd
import numpy as np
from DatosEstudiantes import estudiantes

# Convertir a DataFrame
df = pd.DataFrame(estudiantes)

# Cuenta cuántos estudiantes aprobaron todas sus asignaturas (todas las notas >= 4.0).
df['aprueba_todo'] = df['notas'].apply(lambda notas: all(n >= 4.0 for n in notas))
aprueban_todo = df['aprueba_todo'].sum()

print("Estudiantes que aprobaron todo:", aprueban_todo)