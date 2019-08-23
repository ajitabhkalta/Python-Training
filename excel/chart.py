from openpyxl import Workbook
from openpyxl.chart import (
    Reference,
    BarChart,
    PieChart3D
)

book = Workbook()
sheet = book.active

rows = [
    ("USA", 46),
    ("China", 38),
    ("UK", 29),
    ("Russia", 22),
    ("South Korea", 13),
    ("India", 100)
]

for row in rows:
    sheet.append(row)
    
data = Reference(sheet,min_row=1, min_col=2, max_col=2, max_row=6)
categs = Reference(sheet, min_col=1, min_row=1, max_row=6)

chart = BarChart()
chart.add_data(data=data)
chart.set_categories(categs)

chart.varyColors = True
chart.title = "Olympic Gold medals"

sheet.add_chart(chart, "A8")    

chart = PieChart3D()
chart.add_data(data=data)
chart.set_categories(categs)
sheet.add_chart(chart, "J16") 

book.save("xlf/10.xlsx")