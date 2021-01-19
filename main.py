import pandas as pd
import warnings
from utils import *


warnings.simplefilter(action='ignore', category=FutureWarning)


df = pd.read_csv('C:\\Users\StelD\\Documents\\GitHub\\syfak\\files\\PIST_HER.CSV', delimiter=';', encoding='iso8859_7' )

csvtoexcel(df)
