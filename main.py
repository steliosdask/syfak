import pandas as pd

df = pd.read_csv('C:\\Users\\user\\PycharmProjects\\SyfakProject\\stoch\\test1.csv', delimiter=';', encoding='iso8859_7' )

df = df.loc[(df['ΠΕΡΙΓΡΑΦΗ']=='="ΜΕΛΟΣ"') | (df['ΠΕΡΙΓΡΑΦΗ']== '="ΜΗ ΜΕΛΟΣ-ΦΑΡΜΑΚΕΙΟ"')]

df = df[['ΠΕΡΙΓΡΑΦΗ','ΚΩΔ. ΠΕΛΑΤΗ','ΕΠΩΝΥΜΙΑ','Φαρμακα Συντ/μενα ΤΖΙΡΟΣ','ΠΑΡΑΦΑΡΜΑΚΑ ΤΖΙΡΟΣ','ΓΑΛΑΤΑ ΤΖΙΡΟΣ']].sort_values(['ΠΕΡΙΓΡΑΦΗ','ΕΠΩΝΥΜΙΑ'])

df = df.drop(columns=['ΠΕΡΙΓΡΑΦΗ'])
df = df.drop(df.index[0])
df['Φαρμακα Συντ/μενα ΤΖΙΡΟΣ'] = df['Φαρμακα Συντ/μενα ΤΖΙΡΟΣ'].str.replace(',', '.').astype(float)
df['ΠΑΡΑΦΑΡΜΑΚΑ ΤΖΙΡΟΣ'] = df['ΠΑΡΑΦΑΡΜΑΚΑ ΤΖΙΡΟΣ'].str.replace(',', '.').astype(float)
df['ΓΑΛΑΤΑ ΤΖΙΡΟΣ'] = df['ΓΑΛΑΤΑ ΤΖΙΡΟΣ'].str.replace(',', '.').astype(float)
df['ΚΩΔ. ΠΕΛΑΤΗ']= df['ΚΩΔ. ΠΕΛΑΤΗ'].str.replace('[=,"]', '')
df['ΕΠΩΝΥΜΙΑ']= df['ΕΠΩΝΥΜΙΑ'].str.replace('[=,"]', '')


df['ΣΥΝΟΛΟ'] = df.iloc[:, 2:5].sum(axis=1)
df.to_excel('test.xlsx', index=False)