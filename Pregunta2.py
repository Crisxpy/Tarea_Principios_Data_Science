#2. Cuenta cuántos estudiantes aprobaron todas sus asignaturas (todas las notas > 4.0).
#3. ¿Cuál es la nota más frecuente (moda) considerando todas las notas de todos los estudiantes?
#4. ¿Qué porcentaje de estudiantes tiene al menos una nota bajo 4.0?
#5. Entrega un listado ordenado (de mayor a menor) de los estudiantes promedio.
import DatosEstudiantes

def main():
    CantAlumnosDestacados = 0
    for estudiante in DatosEstudiantes.estudiantes:
        paso = True
        for nota in estudiante["notas"]:
            if (nota < 4.0):
                paso = False
                break
        if(paso):
            CantAlumnosDestacados+=1
            print(f"{estudiante["nombre"]} paso todas sus asignaturas")
    print(f"El total de alumnos que pasaron sin ninguna asignatura reprobada fue: {CantAlumnosDestacados}")




    return

main()