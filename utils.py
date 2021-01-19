import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

def csvtoexcel(df):
    df = df.loc[(df['ΠΕΡΙΓΡΑΦΗ']=='="ΜΕΛΟΣ"') | (df['ΠΕΡΙΓΡΑΦΗ']== '="ΜΗ ΜΕΛΟΣ-ΦΑΡΜΑΚΕΙΟ"')]

    df = df[['ΠΕΡΙΓΡΑΦΗ','ΚΩΔ. ΠΕΛΑΤΗ','ΕΠΩΝΥΜΙΑ','ΦΑΡΜΑΚΑ ΤΖΙΡΟΣ','ΠΑΡΑΦΑΡΜΑΚΑ ΤΖΙΡΟΣ','ΓΑΛΑΤΑ ΤΖΙΡΟΣ']].sort_values(['ΠΕΡΙΓΡΑΦΗ','ΕΠΩΝΥΜΙΑ'])

    df = df.drop(columns=['ΠΕΡΙΓΡΑΦΗ'])
    df = df.drop(df.index[0])
    df['ΦΑΡΜΑΚΑ ΤΖΙΡΟΣ'] = df['ΦΑΡΜΑΚΑ ΤΖΙΡΟΣ'].str.replace(',', '.').astype(float)
    df['ΠΑΡΑΦΑΡΜΑΚΑ ΤΖΙΡΟΣ'] = df['ΠΑΡΑΦΑΡΜΑΚΑ ΤΖΙΡΟΣ'].str.replace(',', '.').astype(float)
    df['ΓΑΛΑΤΑ ΤΖΙΡΟΣ'] = df['ΓΑΛΑΤΑ ΤΖΙΡΟΣ'].str.replace(',', '.').astype(float)
    df['ΚΩΔ. ΠΕΛΑΤΗ'] = df['ΚΩΔ. ΠΕΛΑΤΗ'].str.replace('[=,"]', '')
    df['ΕΠΩΝΥΜΙΑ'] = df['ΕΠΩΝΥΜΙΑ'].str.replace('[=,"]', '')


    df['ΣΥΝΟΛΟ'] = df.iloc[:, 2:5].sum(axis=1)
    out_path = "C:\\Users\StelD\\Documents\\GitHub\\syfak\\files\\PIST_HER.xlsx"
    df.to_excel(out_path, 'test.xlsx', index=False)