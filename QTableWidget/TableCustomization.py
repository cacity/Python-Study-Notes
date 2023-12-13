from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
import sys,PyQt6


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(PyQt6.QtGui.QIcon("./icon/icons8-connect-240.png"))  # 设置窗口图标
        self.setWindowTitle("桥然：QTableWidget")
        self.resize(800,600)
        self.table_widget = QTableWidget()
        self.setCentralWidget(self.table_widget)

        self.setup_table()


    def setup_table(self):
        self.table_widget.setColumnCount(3)
        self.table_widget.setRowCount(5)

        for row in range(self.table_widget.rowCount()):
            for col in range(self.table_widget.columnCount()):
                item = QTableWidgetItem(f"Row {row + 1}, Column {col+1}")
                self.table_widget.setItem(row, col, item)

        #self.table_widget.resizeColumnsToContents()
        self.table_widget.setColumnWidth(0, 150)
        self.table_widget.setColumnWidth(1, 150)
        self.table_widget.setColumnWidth(2, 150)
        self.table_widget.setStyleSheet(

            """
            QTableWidget {
                background-color:#F5F5F5;
                font-family:Arial;
                border:1px solid black;
            
            
            }
            
            QTableWidget::item {
                border-bottom: 1px solid black;
                padding:5px;
            
            
            }
            
            
             QTableWidget::item:selected {
                background-color:#A9D9F7
             
             }
             
              QTableWidget::item:selected:!active {
                color:black
             
             }
            
            
            """
        )




app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())