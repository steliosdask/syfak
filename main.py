import pandas as pd
import glob
import warnings
from utils import *

warnings.simplefilter(action='ignore', category=FutureWarning)

path = r'C:\Users\StelD\Documents\GitHub\syfak\files'
files = glob.glob(path + "\*.csv")

files_new = []
for file in files:
    files_new.append(file.replace(path + "\\" ,''))
print("This is the list of csv files! proceed? \n",files_new)

checkinput = input()

if checkinput == 'Y' or checkinput == 'Yes' or checkinput == 'y' or checkinput == 'yes':
    for file in files_new:
        df = pd.read_csv(path + '\\'+ file, delimiter=';', encoding='iso8859_7')
        xlsx_file = csvtoexcel(df)
        print(xlsx_file)
        #out_path = 'C:\\Users\\StelD\\Documents\\GitHub\\syfak\\files\\' + finalfiles[num] + '.xlsx'
        #xlsx_file.to_excel(out_path, index=False)



'''startfiles = ['PIST_HER','PIST_AIG','PIST_LAS','PIST_RHO','PIST_RET','PIST_HER2','PIST_AIG2','PIST_LAS2','PIST_RHO2','PIST_RET2']
finalfiles = ['ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΗΡΑΚΛΕΙΟ','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΑΙΓΑΙΟ','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΛΑΣΙΘΙ','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΡΟΔΟΣ','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΡΕΘΥΜΝΟ','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΗΡΑΚΛΕΙΟ 2','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΑΙΓΑΙΟ 2','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΛΑΣΙΘΙ 2','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΡΟΔΟΣ 2','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΡΕΘΥΜΝΟ 2']


for num in range(len(startfiles)):
    df = pd.read_csv('C:\\Users\StelD\\Documents\\GitHub\\syfak\\files\\' + startfiles[num] +'.CSV', delimiter=';', encoding='iso8859_7' )

    newfile = csvtoexcel(df)


    out_path = 'C:\\Users\\StelD\\Documents\\GitHub\\syfak\\files\\' + finalfiles[num] + '.xlsx'
    newfile.to_excel(out_path, index=False)'''




