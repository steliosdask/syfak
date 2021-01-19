import pandas as pd
import warnings
from utils import *


warnings.simplefilter(action='ignore', category=FutureWarning)


df = pd.read_csv('C:\\Users\StelD\\Documents\\GitHub\\syfak\\files\\PIST_HER.CSV', delimiter=';', encoding='iso8859_7' )
out_path = "C:\\Users\\StelD\\Documents\\GitHub\\syfak\\files\\PIST_HER.xlsx"


newfile = csvtoexcel(df)
newfile.to_excel(out_path, index=False)

