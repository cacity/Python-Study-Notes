from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
import sys,PyQt6

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(PyQt6.QtGui.QIcon("./icon/icons8-connect-240.png"))  # 设置窗口图标
        self.setWindowTitle("桥然：QTableWidget")
        self.resize(800,600)

        self.table = QTableWidget(5, 3, self)  # 创建一个5行3列的表格
        self.table.setHorizontalHeaderLabels(["Header 1", "Header 2", "Header 3"])  # 设置表头
        for i in range(5):
            for j in range(3):
                self.table.setItem(i, j, QTableWidgetItem(f"Cell {i+1}-{j+1}"))

        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)  # 设置表格为只读
        self.setCentralWidget(self.table)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
