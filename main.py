import pandas as pd
import warnings
from utils import *

warnings.simplefilter(action='ignore', category=FutureWarning)

files= ['PIST_HER','PIST_AIG','PIST_LAS','PIST_RHO','PIST_RET']
for file in files:
    df = pd.read_csv('C:\\Users\StelD\\Documents\\GitHub\\syfak\\files\\' + file +'.CSV', delimiter=';', encoding='iso8859_7' )
    out_path = 'C:\\Users\\StelD\\Documents\\GitHub\\syfak\\files\\' + file +'.xlsx'
    newfile = csvtoexcel(df)
    newfile.to_excel(out_path, index=False)



