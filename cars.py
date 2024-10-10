import pandas as pd

df = pd.read_csv('rdw.csv')
df = df.drop_duplicates(subset=['kenteken'])
df.to_csv('rdw.csv')