import openpyxl

Book = openpyxl.loadworkbook("Path")
Sheet = Book.active
Cell_41 = Sheet.cell(row=4,column=1).value
print(Cell_41)

