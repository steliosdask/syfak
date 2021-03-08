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
        namecheck = file.split('_')
        st1 = "ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ "
        st2 = ""
        st3 = ""
        if len(namecheck) < 3:
            if namecheck[1] == 'AIG.CSV':
                st2 = "ΑΙΓΑΙΟ"
            elif namecheck[1] == 'HER.CSV':
                st2 = "ΗΡΑΚΛΕΙΟ"
            elif namecheck[1] == 'RHO.CSV':
                st2 = "ΡΟΔΟΣ"
            elif namecheck[1] == 'RET.CSV':
                st2 = "ΡΕΘΥΜΝΟ"
            elif namecheck[1] == 'LAS.CSV':
                st2 = "ΛΑΣΙΘΙ"
            else :
                print("WRONG FILE!?")
        else:
            if namecheck[1] == 'AIG':
                st2 = "ΑΙΓΑΙΟ"
                st3 = " 2"
            elif namecheck[1] == 'HER':
                st2 = "ΗΡΑΚΛΕΙΟ"
                st3 = " 2"
            elif namecheck[1] == 'RHO':
                st2 = "ΡΟΔΟΣ"
                st3 = " 2"
            elif namecheck[1] == 'RET':
                st2 = "ΡΕΘΥΜΝΟ"
                st3 = " 2"
            elif namecheck[1] == 'LAS':
                st2 = "ΛΑΣΙΘΙ"
                st3 = " 2"
            else :
                print("WRONG FILE!?")

        out_path = 'C:\\Users\\StelD\\Documents\\GitHub\\syfak\\files\\' +st1 + st2 +st3 +'.xlsx'
        xlsx_file.to_excel(out_path, index=False)

print('You are ready!')


'''startfiles = ['PIST_HER','PIST_AIG','PIST_LAS','PIST_RHO','PIST_RET','PIST_HER2','PIST_AIG2','PIST_LAS2','PIST_RHO2','PIST_RET2']
finalfiles = ['ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΗΡΑΚΛΕΙΟ','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΑΙΓΑΙΟ','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΛΑΣΙΘΙ','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΡΟΔΟΣ','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΡΕΘΥΜΝΟ','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΗΡΑΚΛΕΙΟ 2','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΑΙΓΑΙΟ 2','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΛΑΣΙΘΙ 2','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΡΟΔΟΣ 2','ΤΖΙΡΟΙ ΓΙΑ ΠΙΣΤΩΤΙΚΑ ΡΕΘΥΜΝΟ 2']


for num in range(len(startfiles)):
    df = pd.read_csv('C:\\Users\StelD\\Documents\\GitHub\\syfak\\files\\' + startfiles[num] +'.CSV', delimiter=';', encoding='iso8859_7' )

    newfile = csvtoexcel(df)


    out_path = 'C:\\Users\\StelD\\Documents\\GitHub\\syfak\\files\\' + finalfiles[num] + '.xlsx'
    newfile.to_excel(out_path, index=False)'''




