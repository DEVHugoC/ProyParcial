# Script de ingesta de SQL a Datalake
import pandas as pd

df = pd.read_csv('input.csv')
df['processed'] = df['value'] * 100
df.to_csv('output4.csv', index=False)
print("ETL completado.")

