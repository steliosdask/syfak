import glob
import warnings
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import win32com.client as win32
import jinja2

warnings.simplefilter(action='ignore', category=FutureWarning)


#USER CHOOSE FOLDER WITH CSV FILES
root = tk.Tk()
root.withdraw()
path = filedialog.askdirectory()


#CREATES LIST WITH FILES
def listOfFiles():
    files = glob.glob(path + "\*.csv")
    files_new = []
    for file in files:
        files_new.append(file.replace(path + "\\", ''))
    return files_new


nameoffiles = listOfFiles()


#GIVES APPROPRIATE NAME ON NEW FILE
def finalExcelName():
    saveto = filedialog.askdirectory()
    #if ci == 'Y' or ci == 'Yes' or ci == 'y' or ci == 'yes':
    for file in nameoffiles:
        df = pd.read_csv(path + '\\' + file, delimiter=';', encoding='iso8859_7')
        xlsx_file = xlsform(df)
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
            else:
                print("WRONG FILE !!?")
        else:
            st3 = " 2"
            if namecheck[1] == 'AIG':
                st2 = "ΑΙΓΑΙΟ"
            elif namecheck[1] == 'HER':
                st2 = "ΗΡΑΚΛΕΙΟ"
            elif namecheck[1] == 'RHO':
                st2 = "ΡΟΔΟΣ"
            elif namecheck[1] == 'RET':
                st2 = "ΡΕΘΥΜΝΟ"
            elif namecheck[1] == 'LAS':
                st2 = "ΛΑΣΙΘΙ"
            else:
                print("WRONG FILE !!?")

        out_path = saveto + '\\' + st1 + st2 + st3 + '.xlsx'
        xlsx_file.to_excel(out_path, index=False)

        excel = win32.gencache.EnsureDispatch('Excel.Application')
        wb = excel.Workbooks.Open(out_path)
        ws = wb.Worksheets("Sheet1")
        ws.Range('A:F').ColumnWidth = 22
        ws.Columns(2).ColumnWidth = 50
        wb.Save()
        excel.Application.Quit()





#FORM OF THE NEW FILE
def xlsform(cf):
    cf = cf.loc[(cf['ΠΕΡΙΓΡΑΦΗ'] == '="ΜΕΛΟΣ"') | (cf['ΠΕΡΙΓΡΑΦΗ'] == '="ΜΗ ΜΕΛΟΣ-ΦΑΡΜΑΚΕΙΟ"')]

    cf = cf[['ΠΕΡΙΓΡΑΦΗ', 'ΚΩΔ. ΠΕΛΑΤΗ', 'ΕΠΩΝΥΜΙΑ', 'ΦΑΡΜΑΚΑ ΤΖΙΡΟΣ', 'ΠΑΡΑΦΑΡΜΑΚΑ ΤΖΙΡΟΣ', 'ΓΑΛΑΤΑ ΤΖΙΡΟΣ']].sort_values(['ΠΕΡΙΓΡΑΦΗ', 'ΕΠΩΝΥΜΙΑ'])

    cf = cf.drop(columns=['ΠΕΡΙΓΡΑΦΗ'])
    cf = cf.drop(cf.index[0])
    titlestofloat = ['ΦΑΡΜΑΚΑ ΤΖΙΡΟΣ','ΠΑΡΑΦΑΡΜΑΚΑ ΤΖΙΡΟΣ','ΓΑΛΑΤΑ ΤΖΙΡΟΣ']
    for i in titlestofloat:
        cf[i] = cf[i].str.replace(',', '.').astype(float)
    titlesvalues = ['ΚΩΔ. ΠΕΛΑΤΗ','ΕΠΩΝΥΜΙΑ']
    for j in titlesvalues:
        cf[j] = cf[j].str.replace('[=,"]', '')

    cf['ΣΥΝΟΛΟ'] = cf.iloc[:, 2:5].sum(axis=1)

    cf.loc[cf['ΕΠΩΝΥΜΙΑ'].str.contains('\d', regex=True), ['ΚΩΔ. ΠΕΛΑΤΗ', 'ΕΠΩΝΥΜΙΑ', 'ΦΑΡΜΑΚΑ ΤΖΙΡΟΣ', 'ΠΑΡΑΦΑΡΜΑΚΑ ΤΖΙΡΟΣ', 'ΓΑΛΑΤΑ ΤΖΙΡΟΣ','ΣΥΝΟΛΟ']] = ['ΚΩΔ. ΠΕΛΑΤΗ', 'ΕΠΩΝΥΜΙΑ', 'ΦΑΡΜΑΚΑ ΤΖΙΡΟΣ', 'ΠΑΡΑΦΑΡΜΑΚΑ ΤΖΙΡΟΣ', 'ΓΑΛΑΤΑ ΤΖΙΡΟΣ', 'ΣΥΝΟΛΟ']  # !!!

    cf = cf.style.set_properties(subset=['ΚΩΔ. ΠΕΛΑΤΗ', 'ΦΑΡΜΑΚΑ ΤΖΙΡΟΣ', 'ΠΑΡΑΦΑΡΜΑΚΑ ΤΖΙΡΟΣ', 'ΓΑΛΑΤΑ ΤΖΙΡΟΣ', 'ΣΥΝΟΛΟ'], **{'text-align': 'center'})  # CENTER ALIGNMENT ON SPECIFIC COLUNMS

    return cf


finalExcelName()