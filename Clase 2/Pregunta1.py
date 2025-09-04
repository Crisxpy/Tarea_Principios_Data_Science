#datos
# archivo: lista_estudiantes.py
#1. Calcula el promedio de notas de cada estudiante y determina quién tiene el promedio más alto y más bajo.


import DatosEstudiantes
import numpy as np
import pandas as pd

def main():
    notaMax = 1.0
    notaMin = 7.0
    EstudianteNotaMin = ""
    EstudianteNotaMax = ""
    if len(DatosEstudiantes.estudiantes) == 0:return 

    for estudiante in DatosEstudiantes.estudiantes:
        promedio = DatosEstudiantes.promedio(estudiante["notas"])
        estudiante["promedio"] = promedio
        print(f"El promedio de {estudiante["nombre"]} fue :{promedio}")
        if (notaMax < estudiante["promedio"]):
            notaMax = estudiante["promedio"]
            EstudianteNotaMax = estudiante["nombre"]
        if (notaMin > estudiante["promedio"]):
            notaMin = estudiante["promedio"]
            EstudianteNotaMin =estudiante["nombre"]
    print(f"El promedio mas alto fue de {EstudianteNotaMax} con un promedio de :{notaMax}")
    print(f"Y el promedio mas bajo fue {EstudianteNotaMin}, con un promedio de : {notaMin}")

main()