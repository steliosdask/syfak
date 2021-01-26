import pandas as pd
import warnings
from utils import *

warnings.simplefilter(action='ignore', category=FutureWarning)

startfiles = ['PIST_HER','PIST_AIG','PIST_LAS','PIST_RHO','PIST_RET']
finalfiles = ['ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΗΡΑΚΛΕΙΟ','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΑΙΓΑΙΟ','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΛΑΣΙΘΙ','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΡΟΔΟΣ','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΡΕΘΥΜΝΟ']


for num in range(len(startfiles)):
    df = pd.read_csv('C:\\Users\StelD\\Documents\\GitHub\\syfak\\files\\' + startfiles[num] +'.CSV', delimiter=';', encoding='iso8859_7' )

    newfile = csvtoexcel(df)


    out_path = 'C:\\Users\\StelD\\Documents\\GitHub\\syfak\\files\\' + finalfiles[num] + '.xlsx'
    newfile.to_excel(out_path, index=False)



