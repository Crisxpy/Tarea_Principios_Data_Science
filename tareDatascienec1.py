#datos
import DatosEstudiantes

def ultimoCalculo():# archivo: lista_estudiantes.py

    AllNotas = []
    for estudiante in DatosEstudiantes.estudiantes:
        prom = round(sum(estudiante["notas"])/len(estudiante["notas"]),1)
        estudiante["promedio"] = prom
        aprobadisimo = True
        for nota in estudiante["notas"]:
            if nota < 4.0 :aprobadisimo = False
            AllNotas.append(nota)
        estudiante["Apruebo3"] = aprobadisimo

    print(DatosEstudiantes.estudiantes)
    moda(AllNotas)
    

    return

def moda(Notas):
    frecuencias = {}
    for nota in Notas:
        if nota in frecuencias:
            frecuencias[nota]+=1
        else:
            frecuencias[nota] = 1
    moda = max(frecuencias, key=frecuencias.get)
    print(moda)
    return

def calculoNotas():
    notas = [4.8,6.2,5.5,3.9,7.0,4.1,5.8,6.0,3.5,5.2,6.8,2.9,4.0,5.0,6.5]
    reprobados = []
    aprobados = []
    destacados = []
    for nota in notas:
        if 4.0 > nota:
            reprobados.append(nota)
        if( 4.0 >= nota and 5.9 > nota):
            aprobados.append(nota)
        if(6.0 <= nota):
            destacados.append(nota)
    promReprobados = sum(reprobados)/len(notas)
    promAprobados = sum(aprobados)/len(notas)
    promDestacados = sum(destacados)/len(notas)
    PerReprobados = (100*len(reprobados))/len(notas)
    PerAprobados = (100*len(aprobados))/len(notas)
    PerDestacados = (100*len(destacados))/len(notas)
    print(f"Las listas son:\n reprobados: {reprobados}\naprobados: {aprobados}\ndestacados: {destacados}")
    print(f"Promedio de los reprobados fue: {promReprobados}\nPromedio aprobados: {promAprobados}\nPromedio Destacados: { promDestacados}")
    print(f"Porcentajes de cada seccion , reprobados: {PerReprobados} , aprobados {PerAprobados} y destacados : {PerDestacados} ")
    

    print("ok")

def notacursoMayor5():
    #datos
    notas = [4.8,6.2,5.5,3.9,7.0,4.1,5.8,6.0,3.5,5.2]
    promedioNotas = 0
    notaMax = 0
    notaMin = 7
    Mayor5 = 0
    for nota in notas:
        promedioNotas+= nota
        if(notaMax<nota):
            notaMax=nota
        if(notaMin>nota):
            notaMin=nota
        if(nota > 5.0):
            Mayor5+=1
    print(f"El Promedio de el curso fue {(promedioNotas/len(notas))}\nLa nota mas baja fue: {notaMin}\nLa nota mas alta fue: { notaMax}\nY un total de {Mayor5} se sacaron mayor a 5.0")



def notacurso():
    notas_curos = [6.5,7.0,3.2,4.8,5.8,2.1,4.0]
    aprobados = 0
    promedio = 0
    for i in notas_curos:
        promedio += i
        if( i >= 4.0):
            aprobados+=1
    promedio = round((promedio/(len(notas_curos))),1)
    print(f"El promedio del curso fue {promedio:.1f}\nY aprovaron {aprobados}")
    
def main():
    #notacursoMayor5()
    #calculoNotas()
    ultimoCalculo()
main()
