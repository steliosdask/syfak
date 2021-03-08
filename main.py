from utils import *


namelist = listoffiles()

print("This is the list of csv files! proceed to xlsx form? \n", namelist)
checkinput = input()

finalExcelName(checkinput)

print('You are ready!')





