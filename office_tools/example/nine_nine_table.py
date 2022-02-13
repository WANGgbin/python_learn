# 创建一个 9*9 乘法表

import openpyxl as xl

def run():
    wb = xl.Workbook()
    ws = wb.active
    for limit, row in enumerate(ws.iter_rows(min_row=1, max_row=9, min_col=1, max_col=9)):
        for index, cell in enumerate(row):
            if index > limit:
                break
            cell.value = f'{limit + 1} * {index + 1} = {(limit + 1) * (index + 1)}'
    wb.save('99_table.xlsx')

# 设置字体格式

if __name__ == '__main__':
    run()