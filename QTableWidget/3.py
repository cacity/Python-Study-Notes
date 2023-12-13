import csv
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
import sys,PyQt6

# 定义CSVTable类，继承自QMainWindow
class CSVTable(QMainWindow):
    def __init__(self):
        super().__init__()  # 调用父类的初始化方法
        self.setWindowIcon(PyQt6.QtGui.QIcon("./icon/icons8-connect-240.png"))  # 设置窗口图标
        self.setWindowTitle("桥然：QTableWidget 自动加载csv表")  # 设置窗口标题
        self.resize(800,600)  # 设置窗口大小
        self.table = QTableWidget()  # 创建一个QTableWidget对象
        self.setCentralWidget(self.table)  # 将这个QTableWidget设置为窗口的中心部件

        self.load_csv('output.csv')  # 调用load_csv方法加载CSV文件

    # 定义load_csv方法，用于加载CSV文件
    def load_csv(self, filename):
        with open(filename, 'r') as f:  # 打开文件
            csvreader = csv.reader(f)  # 创建一个csv.reader对象
            for row_index, row in enumerate(csvreader):  # 遍历csv.reader对象的每一行
                if row_index == 0:  # 如果是第一行
                    self.table.setColumnCount(len(row))  # 设置表格的列数
                    self.table.setHorizontalHeaderLabels(row)  # 设置表格的列标题
                else:  # 如果不是第一行
                    self.table.insertRow(self.table.rowCount())  # 在表格的末尾插入一行
                    for column_index, item in enumerate(row):  # 遍历这一行的每一列
                        self.table.setItem(self.table.rowCount()-1, column_index, QTableWidgetItem(item))  # 在表格的相应位置插入一个QTableWidgetItem对象

if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建一个QApplication对象
    window = CSVTable()  # 创建一个CSVTable对象
    window.show()  # 显示这个窗口
    sys.exit(app.exec())  # 进入事件循环
