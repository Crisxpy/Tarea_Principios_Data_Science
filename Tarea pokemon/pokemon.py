import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import seaborn 
import os
#  1. Lectura de datos
#     -------------------
#     - Carga el archivo pokemon_primera_gen.csv en un DataFrame de Pandas.

def main():
    scriptDir = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(scriptDir, "pokemon_primera_gen.csv")
    csv = pd.read_csv(file)
    df = pd.DataFrame(csv)
    print(df)
#   1.5 Limpiar los datos
    df = df.drop_duplicates(subset=['Nombre'], keep = "first")
    stats = ["Ataque", "Defensa", "Velocidad", "PS"]
    df[stats] = df[stats].clip(lower=0, upper=254)
    df.loc[df["Tipo 1"] == df["Tipo 2"], "Tipo 2"] = pd.NA
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
    print(f"El promedio,mediana y de ataque de los Pokemons es igual a... ")
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
    df["Poder Total"] = df["Ataque"] + df["Defensa"] + df["Velocidad"] + df["PS"]
    dfTotalMayorMenor = df.sort_values("Poder Total", ascending=False)
    print(f"Top 5 pokemon por poder total: ")
    print(dfTotalMayorMenor[["Nombre", "Poder Total"]])
#     6. Agrupamiento y análisis por grupo
#     -------------------------------------
#     - Calcula el promedio, la mediana y la desviación estándar de ataque por cada tipo principal (Tipo 1).
#     - ¿Qué tipo tiene el mayor promedio de velocidad?
#     - Para cada tipo principal, ¿cuál es el Pokémon con mayor y menor PS?
    stsAtkMean = df.groupby("Tipo 1")["Ataque"].mean()
    stsAtkMedian = df.groupby("Tipo 1")["Ataque"].median()
    stsAtkStndr = df.groupby("Tipo 1")["Ataque"].std()

    print("Estadísticas de ataque por tipo principal: \n")
    print(f"El promedio de ATK por tipo es de: {stsAtkMean}\n")
    print(f"La mediana de ATK por tipo es de: {stsAtkMedian}\n")
    print(f"La desviacion estandar de ATK por tipo es de: {stsAtkStndr}\n")

    tipoVel = df.groupby("Tipo 1")["Velocidad"].mean().idxmax()
    print("Tipo con mayor promedio de velocidad:\n", tipoVel)

    maxVida = df.loc[df.groupby("Tipo 1")["PS"].idxmax(), ["Tipo 1", "Nombre", "PS"]]
    minVida = df.loc[df.groupby("Tipo 1")["PS"].idxmin(), ["Tipo 1", "Nombre", "PS"]]
    print("\nPokémon con mayor PS por tipo:")
    print(maxVida)
    print("\nPokémon con menor PS por tipo:")
    print(minVida)

#     7. Análisis exploratorio (EDA)
#     ------------------------------
#     - ¿Existen tipos de Pokémon que tienden a tener mayor ataque o defensa? Justifica con estadísticas.
#     - ¿Hay correlación entre ataque y velocidad? Calcula el coeficiente de correlación.
#     - ¿Qué tan dispersos están los PS dentro de cada tipo? (compara la desviación estándar de PS por tipo)
#     - Identifica posibles outliers en los valores de ataque y PS usando boxplots.
    print(f"Promedios de ataque por tipo: \n")
    print(df.groupby("Tipo 1")["Ataque"].mean().sort_values(ascending=False))
    print("Hay una tendencia a tipos con ataque alto ser los tipos relaiconados a peleas fisicas, siendo lucha el n#1 con un promedio de 102 de ATK.")

    print(f"Promedios de defensa por tipo: \n")
    print(df.groupby("Tipo 1")["Defensa"].mean().sort_values(ascending=False))
    print("Los tipo tierra y roca especialmente tienden a tener una cantidad superior de defensa en general con un promedio de 110 DEF.")
    correlacion = df["Ataque"].corr(df["Velocidad"])
    print("correlación ataque vs velocidad: \n", correlacion)
    print("con una correlacio de 0.19~ no podemos concluir una correlacion entre el ATK y la VEL , de hecho podriamos decir que NO estan correlacionadas.")

    print("Desviación estándar de PS por tipo: \n")
    print(df.groupby("Tipo 1")["PS"].std())
    print("En general los PS varian entre 17~ y 30~ puntos de salud dentro de los tipos , excepto en el tipo normal , donde existe una variacion de 50 puntos dentro de la categoria.")

    plot.figure(figsize=(8, 5))
    seaborn.boxplot(data=df, y="Ataque")
    plot.title("Detección de Outliers en Ataque")
    plot.show()
    print("No se observan outliers en ATK")
    plot.figure(figsize=(8, 5))
    seaborn.boxplot(data=df, y="PS")
    plot.title("Detección de Outliers en PS")
    plot.show()
    print("Se observa un OUTLIER con el MAX posible de salud de 255 PS.")
#     8. Ejercicios de interpretación
#     -------------------------------
#     - Interpreta los resultados de los gráficos y estadísticas: ¿qué conclusiones puedes sacar sobre los Pokémon de la primera generación?
#     - ¿Qué tipo de Pokémon sería "más balanceado" según las estadísticas? ¿Y el más especializado?
#       El tipo planta se ve el mas balanceado , redondea los 70 puntos en casi todos sus median , mean , con un bajo STD . estadisticamente hablando seria el mas "balanceado"
#       El tipo fantasma se ve muy desbalanceado , es muy especializado siendo parate de los mayores en los promedio de algunas estadisticas y el peor en otras. 

#     ---

#     Recuerda usar las funciones de Pandas como mean(), median(), mode(), std(), describe(), groupby(), así como las funciones de visualización de Matplotlib y Seaborn vistas en la Semana 3.
    return
main()

