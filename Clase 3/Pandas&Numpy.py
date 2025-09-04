import pandas as pd
import DatosEstudiantes
import numpy as np

estudiantes = DatosEstudiantes.estudiantes

# Example of PANDA USE
excel = pd.read_excel('.\datos.xlsx')
print(excel)


#Example of NUMPY USE
lista_notas = [6.5,7.0,5.8,4.9]
array_notas = np.array(lista_notas)
print(array_notas)  

df_alumnos = pd.DataFrame(estudiantes)
print(df_alumnos)
print(f"nombres{df_alumnos["notas"]}")

#ejercicio 2 , convertir de °c a °f 
import numpy as np
#formula  $F = c * (9/5)+32+

grados_c = np.array([0,15,25,30,100])
grados_f = grados_c*(9/5)+32
print(grados_c,grados_f)

#ejercucio 3 matrix 6
matrix = np.arange(1,10).reshape(3,3)
print(matrix)
numeroA = matrix[1,2]
numeroB = matrix[1,:]
numeroC = matrix[2,:]
print(f"Numeroa: {numeroA} \n numero b : { numeroB } ,\n  numero c: {numeroC}")
print(np.arange(1,19))

#ejercicio 4
notas = np.array([4.5,6.2,3.9,7.0,5.5,2.1])
print(f"Promedio : {notas.mean()} , desviacion estandar: {notas.std()} , \n Nota maxima:  {notas.max()} , nota minima:  {notas.min()}")

# ejercicio 5 filtrar bool, dado el array filtrar <= 40
print(notas)
notMascarasMayor4 = notas>=4.0
Notasmasque4 = notas[notMascarasMayor4]

print(Notasmasque4)
