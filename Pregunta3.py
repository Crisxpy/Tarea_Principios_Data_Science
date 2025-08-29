#3. ¿Cuál es la nota más frecuente (moda) considerando todas las notas de todos los estudiantes?
#4. ¿Qué porcentaje de estudiantes tiene al menos una nota bajo 4.0?
#5. Entrega un listado ordenado (de mayor a menor) de los estudiantes promedio.

import DatosEstudiantes

def main():
    TodaslasNotas = []
    for estudiante in DatosEstudiantes.estudiantes:
        for nota in estudiante["notas"]:
            TodaslasNotas.append(nota)
    moda(TodaslasNotas)
    return

def moda(TodaslasNotas):
    NotasDict = {}
    for nota in TodaslasNotas:
        if not(nota in NotasDict):            
            NotasDict[str(nota)] = 1
        elif(nota in NotasDict):
            NotasDict[str(nota)] =  NotasDict[str(nota)] + 1
        print(f"nota: {nota} ; {NotasDict[str(nota)]},{nota in NotasDict}")
        print(NotasDict)
    for nota in NotasDict:
        print(f"notas:{ nota } ; {NotasDict[nota]}")
    return


main()