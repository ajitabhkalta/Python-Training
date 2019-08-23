import openpyxl

book = openpyxl.load_workbook('xlf/3.xlsx')
sheet = book.active
for i in range(2,5):
    name=sheet[f"A{i}"]
    print(f"Name:{name.value}")
    email=sheet[f"C{i}"]
    print(f"\tEmail:{email.value}")
