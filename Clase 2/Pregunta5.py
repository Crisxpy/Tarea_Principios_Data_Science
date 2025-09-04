#5. Entrega un listado ordenado (de mayor a menor) de los estudiantes promedio.

import DatosEstudiantes

def main():
    estudiantado = DatosEstudiantes.estudiantes
    for estudiante in estudiantado:
        promedio = DatosEstudiantes.promedio(estudiante["notas"])
        estudiante["promedio"] = promedio
    OrdenarEstudiantes(estudiantado)
    return

def OrdenarEstudiantes(estudiantado):
    EstudiantesOrdenado = sorted(estudiantado,key=lambda x: x["promedio"],reverse=True)
    print(f"Estudiantes ordenados:")
    for estudiante in EstudiantesOrdenado:
        print(f"Nombre : {(estudiante["nombre"]):<12} promedio: {estudiante["promedio"]} ")
    return
main()

