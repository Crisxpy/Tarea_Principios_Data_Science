#Una corredora de propiedades en Santiago quiere predecir el precio (en UF) de departamentos. Tienen los siguientes datos:
#datos = {'Superficie_m2': [50, 70, 65, 90, 45], 'Num_Habitaciones': [1, 2, 2, 3, 1], 'Distancia_Metro_km': [0.5, 1.2, 0.8, 0.2, 2.0], 'Precio_UF': [2500, 3800, 3500, 5200, 2100]}
#Construye un modelo de regresión lineal múltiple para predecir el 'Precio_UF' y evalúa su rendimiento.
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import sklearn.metrics as skm
import pandas as pd
import numpy as np
datos = {'Superficie_m2': [50, 70, 65, 90, 45], 'Num_Habitaciones': [1, 2, 2, 3, 1], 'Distancia_Metro_km': [0.5, 1.2, 0.8, 0.2, 2.0], 'Precio_UF': [2500, 3800, 3500, 5200, 2100]}
df = pd.DataFrame(datos)
feature = df[['Superficie_m2', 'Num_Habitaciones', 'Distancia_Metro_km']]
target = df['Precio_UF']
model = LinearRegression()
model.fit(feature,target)
predicc = model.predict(feature)
R2 = skm.r2_score(target,predicc)
MSE = skm.mean_squared_error(target,predicc)
RMSE = np.sqrt(MSE)
print(model)
print(df)
print(predicc)
print(R2)
print(MSE)
print(RMSE)
# No me gustan los resultados que da esto , esta solo viendo y copiando los datos. Voy a hacer un test y training set
Inputtrain, Inputtest, Outputtrain, Outputtest = train_test_split(feature, target, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(Inputtrain, Outputtrain)
predicc = model.predict(Inputtest)
R2 = skm.r2_score(Outputtest, predicc)
MSE = skm.mean_squared_error(Outputtest, predicc)
RMSE = np.sqrt(MSE)
print(model)
print(df)
print(predicc)
print(R2)
print(MSE)
print(RMSE)