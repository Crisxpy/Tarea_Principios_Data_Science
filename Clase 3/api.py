import requests
import pandas as pd
url = 'https://mindicador.cl/api/dolar'

response = requests.get(url)
print(response)
data = response.json()
Frameo = pd.DataFrame(data)
print(Frameo)
df_uf = pd.DataFrame(data["serie"])
print(df_uf)
print(df_uf.head())

