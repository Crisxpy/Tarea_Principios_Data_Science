import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import seaborn 
#  1. Lectura de datos
#     -------------------
#     - Carga el archivo pokemon_primera_gen.csv en un DataFrame de Pandas.

def main():
    file = 'F:/Git/Tarea_Principios_Data_Science/Tarea pokemon/pokemon_primera_gen.csv'
    csv = pd.read_csv(file)
    df = pd.DataFrame(csv)
    print(df)
#     2. Filtrado y selección
#     -----------------------
#     - Filtra todos los Pokémon de tipo "Fuego".
#     - Selecciona solo las columnas Nombre, Tipo 1, Ataque y Velocidad.
    pkmtypFuego = df[df["Tipo 1"] == "Fuego"][["Nombre","Tipo 1", "Ataque" , "Velocidad"]]
    print(pkmtypFuego)
#     3. Estadística descriptiva básica
#     ---------------------------------
#     - Calcula el promedio, la mediana y la moda del ataque de todos los Pokémon.
#     - ¿Cuál es el Pokémon con mayor defensa? ¿Y el de menor velocidad?
#     - ¿Cuántos Pokémon tienen dos tipos?
#     - Calcula el rango y la desviación estándar de los PS (Puntos de Salud).
    promAtk = df["Ataque"].mean()
    medianAtk = df["Ataque"].median()
    modaAtk = df["Ataque"].mode()[0]
    print(f"El promedio,mediana y de ataque de los Pokemons es igual ")
    print(f"Promedio : {promAtk}")
    print(f"Mediana : {medianAtk}")
    print(f"Moda : {modaAtk}")
    peakDefensa = df.loc[df["Defensa"].idxmax(), ["Nombre", "Defensa"]]
    leastVelocity = df.loc[df["Velocidad"].idxmin(), ["Nombre", "Velocidad"]]
    print(f"El Pokemon con mayor defesa es: {peakDefensa["Nombre"]}")
    print(f"Y el Pokemon con menor velocidad es: {leastVelocity["Nombre"]}")
    rangoHP = df["PS"].max() - df["PS"].min()
    deviationHP = round(df["PS"].std(),2)
    print(f"El rango entre la menor y mayor cantidad de HP es de: {rangoHP} y su  deviacion estandar es de : {deviationHP}")

#     4. Visualización de datos
#     -------------------------
#     - Haz un histograma de los valores de ataque.
#     - Realiza un gráfico de dispersión entre ataque y velocidad.
#     - Haz un boxplot de los PS por tipo principal (Tipo 1).
#     - Grafica la distribución de la defensa usando un diagrama de violín.
    plot.figure(figsize=(8, 5))
    seaborn.histplot(df["Ataque"], bins=15, kde=True)
    plot.title("Histograma de Ataque")
    plot.show()
    plot.figure(figsize=(8, 5))
    seaborn.scatterplot(data=df, x="Ataque", y="Velocidad")
    plot.title("Ataque vs Velocidad")
    plot.show()
    plot.figure(figsize=(10, 6))
    seaborn.boxplot(data=df, x="Tipo 1", y="PS")
    plot.title("Boxplot de HP por tipo principal")
    plot.xticks(rotation=45)
    plot.show()
    plot.figure(figsize=(8, 5))
    seaborn.violinplot(data=df, y="Defensa")
    plot.title("Distribución de Defensa")
    plot.show()

#     5. Manipulación de datos
#     ------------------------
#     - Crea una nueva columna llamada "Poder Total" que sea la suma de ataque, defensa, velocidad y PS.
#     - Ordena el DataFrame por "Poder Total" de mayor a menor.

#     6. Agrupamiento y análisis por grupo
#     -------------------------------------
#     - Calcula el promedio, la mediana y la desviación estándar de ataque por cada tipo principal (Tipo 1).
#     - ¿Qué tipo tiene el mayor promedio de velocidad?
#     - Para cada tipo principal, ¿cuál es el Pokémon con mayor y menor PS?

#     7. Análisis exploratorio (EDA)
#     ------------------------------
#     - ¿Existen tipos de Pokémon que tienden a tener mayor ataque o defensa? Justifica con estadísticas.
#     - ¿Hay correlación entre ataque y velocidad? Calcula el coeficiente de correlación.
#     - ¿Qué tan dispersos están los PS dentro de cada tipo? (compara la desviación estándar de PS por tipo)
#     - Identifica posibles outliers en los valores de ataque y PS usando boxplots.

#     8. Ejercicios de interpretación
#     -------------------------------
#     - Interpreta los resultados de los gráficos y estadísticas: ¿qué conclusiones puedes sacar sobre los Pokémon de la primera generación?
#     - ¿Qué tipo de Pokémon sería "más balanceado" según las estadísticas? ¿Y el más especializado?

#     ---

#     Recuerda usar las funciones de Pandas como mean(), median(), mode(), std(), describe(), groupby(), así como las funciones de visualización de Matplotlib y Seaborn vistas en la Semana 3.
    return
main()

