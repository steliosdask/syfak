import pandas as pd
import warnings
from utils import *

warnings.simplefilter(action='ignore', category=FutureWarning)

files = ['PIST_HER','PIST_AIG','PIST_LAS','PIST_RHO','PIST_RET']
files2 = ['ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΗΡΑΚΛΕΙΟ','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΑΙΓΑΙΟ','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΛΑΣΙΘΙ','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΡΟΔΟΣ','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΡΕΘΥΜΝΟ']
for num in range(len(files)):
    df = pd.read_csv('C:\\Users\StelD\\Documents\\GitHub\\syfak\\files\\' + files[num] +'.CSV', delimiter=';', encoding='iso8859_7' )

    newfile = csvtoexcel(df)


    out_path = 'C:\\Users\\StelD\\Documents\\GitHub\\syfak\\files\\' + files2[num] + '.xlsx'
    newfile.to_excel(out_path, index=False)



