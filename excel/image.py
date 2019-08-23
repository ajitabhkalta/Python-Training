from openpyxl import Workbook
from openpyxl.drawing.image import Image
#please do install Pillow module
#pip install Pillow to use images

book = Workbook()
sheet = book.active

img = Image("xlf/apple.jpg")
sheet['A1'] = 'This is apple'

sheet.add_image(img, 'B2')

book.save("xlf/9.xlsx")