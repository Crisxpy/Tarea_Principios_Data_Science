#4. ¿Qué porcentaje de estudiantes tiene al menos una nota bajo 4.0?
#5. Entrega un listado ordenado (de mayor a menor) de los estudiantes promedio.

import DatosEstudiantes

def main():
    Alumnosmaoma = 0
    for estudiante in DatosEstudiantes.estudiantes:
        notaMenor4 = Menora4(estudiante["notas"])
        if(not notaMenor4):
            Alumnosmaoma+=1
    PorcAlumnos = (Alumnosmaoma/len(DatosEstudiantes.estudiantes)*100)
    print(f"El porcentaje de alumnos con almenos una nota bajo 4.0 es un: {PorcAlumnos}%")

    return

def Menora4(Estudiante):
    for nota in Estudiante:
        if(nota<4.0):
            return False
    return True
main()