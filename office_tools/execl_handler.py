# https://openpyxl.readthedocs.io/en/stable/tutorial.html#create-a-workbook
# @Description: 主要用来描述如何使用 excel
from openpyxl import Workbook
import datetime


if __name__ == '__main__':
    wb = Workbook()
    sheet = wb.active
    sheet['A1'] = 42
    sheet.append([1, 2, 3])
    sheet['A2'] = datetime.datetime.now()
    wb.save('test.xlsx')
