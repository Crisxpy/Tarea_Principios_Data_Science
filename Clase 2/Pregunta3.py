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
        StrNota = str(nota)
        if not(StrNota in NotasDict):            
            NotasDict[StrNota] = 1
        else:
            NotasDict[StrNota]+=1
    Moda = 0
    NotaModa = 0
    for nota in NotasDict:
        if(NotasDict[str(nota)] > Moda):
            Moda = NotasDict[str(nota)]
            NotaModa = nota
    print(f"La nota mas frecuente (moda) fue: {NotaModa} con una frecuencia de: {Moda}")
    return


main()