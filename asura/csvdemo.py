#导入csv模块
import csv
#指定文件名，然后使用 with open() as 打开
filename = '0101.csv'
with open(filename) as f:
        #创建一个阅读器：将f传给csv.reader
        reader = csv.reader(f)
        #使用csv的next函数，将reader传给next，将返回文件的下一行
        header_row = next(reader)
        for index, column_header in enumerate(header_row):
            print(index, column_header)

