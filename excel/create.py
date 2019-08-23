#create new workbook and save
import os
try:
    from openpyxl import Workbook
except ImportError:
        os.system(f'pip install openpyxl')

import time

book = Workbook()
sheet = book.active

sheet['A1'] = 56
sheet['A2'] = 43
sheet.cell(row=3,column=1,value=time.strftime("%x"))

book.save("xlf/1.xlsx")
print("Data saved succesfully")