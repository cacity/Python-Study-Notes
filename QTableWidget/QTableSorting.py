from PyQt6.QtWidgets import QApplication, QMainWindow,QWidget , QTableWidget, QTableWidgetItem, QLineEdit, QVBoxLayout
import sys,PyQt6
from PyQt6.QtCore import Qt

# 创建一个主窗口类，继承自QMainWindow
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(PyQt6.QtGui.QIcon("./icon/icons8-connect-240.png"))  # 设置窗口图标
        self.setWindowTitle("桥然：QTableWidget筛选、排序")  # 设置窗口标题
        self.resize(800,600)  # 设置窗口大小

        self.table_widget = QTableWidget()  # 创建一个表格控件
        self.filter_edit = QLineEdit()  # 创建一个文本输入框，用于输入过滤条件

        vbox = QVBoxLayout()  # 创建一个垂直布局
        vbox.addWidget(self.filter_edit)  # 将文本输入框添加到布局中
        vbox.addWidget(self.table_widget)  # 将表格控件添加到布局中

        main_widget = QWidget()  # 创建一个主控件
        main_widget.setLayout(vbox)  # 将布局设置到主控件中
        self.setCentralWidget(main_widget)  # 将主控件设置为窗口的中心控件

        self.setup_table()  # 设置表格
        self.setup_connections()  # 设置连接

    # 设置表格的方法
    def setup_table(self):
        self.table_widget.setColumnCount(4)  # 设置表格的列数
        self.table_widget.setHorizontalHeaderLabels(["Name", "Category", "Price", "Date"])  # 设置表格的列标题

        # 表格的数据
        data = [
            ("Product 1", "Category A", "10", "2023-05-15"),
            ("Product 2", "Category B", "15", "2023-06-10"),
            ("Product 3", "Category A", "20", "2023-07-20"),
            ("Product 4", "Category C", "25", "2023-08-05"),
            ("Product 5", "Category B", "30", "2023-09-15")
        ]

        self.table_widget.setRowCount(len(data))  # 设置表格的行数

        # 将数据添加到表格中
        for row, (name, category, price, date) in enumerate(data):
            self.table_widget.setItem(row, 0, QTableWidgetItem(name))
            self.table_widget.setItem(row, 1, QTableWidgetItem(category))
            self.table_widget.setItem(row, 2, QTableWidgetItem(price))
            self.table_widget.setItem(row, 3, QTableWidgetItem(date))

    # 设置连接的方法
    def setup_connections(self):
        # 当表头被点击时，调用sort_table方法对表格进行排序
        self.table_widget.horizontalHeader().sectionClicked.connect(self.sort_table)
        # 当文本输入框的内容改变时，调用filter_table方法对表格进行过滤
        self.filter_edit.textChanged.connect(self.filter_table)

    # 对表格进行排序的方法
    def sort_table(self, column):
        self.table_widget.sortItems(column, Qt.SortOrder.AscendingOrder)

    # 对表格进行过滤的方法
    def filter_table(self, filter_text):
        for row in range(self.table_widget.rowCount()):
            match = False
            for col in range(self.table_widget.columnCount()):
                item = self.table_widget.item(row, col)
                if filter_text.lower() in item.text().lower():
                    match = True
                    break
            self.table_widget.setRowHidden(row, not match)

# 创建应用程序实例
app = QApplication(sys.argv)
# 创建窗口实例
window = Window()
# 显示窗口
window.show()
# 进入应用程序的事件循环
sys.exit(app.exec())
