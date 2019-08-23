from openpyxl import Workbook

book = Workbook()
sheet = book.active

sheet['A1']="Name"
sheet['B1']="Email"
sheet['C1']="Phone"
rows = (
    ("Mahesh", "mahesh@gmail.com", "123456789"),
    ("Suresh", "Suresh@gmail.com", "987654321"),
)

for row in rows:
    sheet.append(row)

book.save('xlf/2.xlsx')