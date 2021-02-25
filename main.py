import pandas as pd
import glob
import warnings
from utils import *

warnings.simplefilter(action='ignore', category=FutureWarning)

path = 'C:\\Users\\StelD\\Documents\\GitHub\\syfak\\files\\'
files = glob.glob(path + "*.csv")

print(files)
li = []

for filename in files:
    df = pd.read_csv(filename, delimiter=';', encoding='iso8859_7')
    li.append(df)
frame = pd.concat(li, axis=0, ignore_index=True)
print(frame)
#print(li)
#startfiles = ['PIST_HER','PIST_AIG','PIST_LAS','PIST_RHO','PIST_RET','PIST_HER2','PIST_AIG2','PIST_LAS2','PIST_RHO2','PIST_RET2']
#finalfiles = ['ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΗΡΑΚΛΕΙΟ','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΑΙΓΑΙΟ','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΛΑΣΙΘΙ','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΡΟΔΟΣ','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΡΕΘΥΜΝΟ','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΗΡΑΚΛΕΙΟ 2','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΑΙΓΑΙΟ 2','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΛΑΣΙΘΙ 2','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΡΟΔΟΣ 2','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΡΕΘΥΜΝΟ 2']


#for num in range(len(startfiles)):
    #df = pd.read_csv('C:\\Users\StelD\\Documents\\GitHub\\syfak\\files\\' + startfiles[num] +'.CSV', delimiter=';', encoding='iso8859_7' )

    #newfile = csvtoexcel(df)


    #out_path = 'C:\\Users\\StelD\\Documents\\GitHub\\syfak\\files\\' + finalfiles[num] + '.xlsx'
    #newfile.to_excel(out_path, index=False)



