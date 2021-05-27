from utils import finalExcelName
import tkinter as tk
from tkinter import filedialog


#USER CHOOSE DIRECTORY WITH CSV FILES
root = tk.Tk()
root.withdraw()
patheoffiles = filedialog.askdirectory()

#SAVE TO DIRECTORY
saveto = filedialog.askdirectory()
finalExcelName(saveto)

'''namelist = listOfFiles()
print("This is the list of csv files! proceed to xlsx form? \n", namelist)
checkinput = input()'''









