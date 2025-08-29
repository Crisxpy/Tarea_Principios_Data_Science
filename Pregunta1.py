#datos
# archivo: lista_estudiantes.py
#1. Calcula el promedio de notas de cada estudiante y determina quién tiene el promedio más alto y más bajo.
#2. Cuenta cuántos estudiantes aprobaron todas sus asignaturas (todas las notas > 4.0).
#3. ¿Cuál es la nota más frecuente (moda) considerando todas las notas de todos los estudiantes?
#4. ¿Qué porcentaje de estudiantes tiene al menos una nota bajo 4.0?
#5. Entrega un listado ordenado (de mayor a menor) de los estudiantes promedio.

import DatosEstudiantes
def main():
    notaMax = 1.0
    notaMin = 7.0
    EstudianteNotaMin = ""
    EstudianteNotaMax = ""
    if len(DatosEstudiantes.estudiantes) == 0:return 

    for estudiante in DatosEstudiantes.estudiantes:
        promedio = round(sum(estudiante["notas"])/len(estudiante["notas"]),1)
        promedio = 
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