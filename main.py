from utils import *


namelist = listOfFiles()


print("This is the list of csv files! proceed to xlsx form? \n", namelist)
checkinput = input()


finalExcelName(checkinput)

print('You are ready!')





