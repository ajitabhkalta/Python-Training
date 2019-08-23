import openpyxl

book = openpyxl.load_workbook('xlf/4.xlsx')

sheet = book.active

cells = sheet['A1': 'B5']
print(cells)
for c1, c2 in cells:
    print("{0:8} {1:8}".format(c1.value, c2.value))