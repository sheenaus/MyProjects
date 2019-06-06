import xlwt
import xlrd
from xlwt import Workbook
loc = ("D:\sqlserverprogramming\erecords.xlsx")
outloc= ("D:\sqlserverprogramming\Jil")
# Workbook is created
##wb = Workbook()

# add_sheet is used to create sheet.
##sheet1 = wb.add_sheet('Sheet 1')
list =['EMPID','FName','Lname','DOJ','SAL']
wbr = xlrd.open_workbook(loc)
sheet = wbr.sheet_by_index(0)
for i in range(sheet.nrows):
    print(outloc + '_' + str(i) + '.' + 'txt')
    f = open(outloc + '_' + str(i) + '.' + 'txt',    "w+")
    for   j in range(sheet.ncols):
        f.write(list[j]+' : '+str(sheet.cell_value(i,j))+'\r\n')
    f.close()
