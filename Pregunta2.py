#2. Cuenta cuántos estudiantes aprobaron todas sus asignaturas (todas las notas > 4.0).

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