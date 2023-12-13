import csv
import random

# 定义列标题
headers = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5', 'Column6', 'Column7', 'Column8']

# 生成数据
data = [[random.randint(0, 100) for _ in range(8)] for _ in range(50)]

# 写入CSV文件
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data)
