from PyQt5.QtWidgets import (QMainWindow, QHBoxLayout, QLabel,
                            QPushButton, QVBoxLayout, QWidget,
                            QLineEdit, QTextEdit)
from PyQt5.QtCore import Qt

class AddNewCity(QMainWindow):
    def __init__(self, admin_window):
        super().__init__()
        self.__admin_window = admin_window

        self.setWindowTitle("Add new city")
        self.__go_back_button = QPushButton("←")
        self.__go_back_button.setMinimumWidth(40)
        self.__go_back_button.clicked.connect(self.__go_back_button_clicked)

        self.__requiring_label = QPushButton("<html><b><font size='5'>enter new city name</html></b></font>")

        self.__main_line_edit = QLineEdit()
        self.__main_line_edit.setPlaceholderText("enter here")

        self.__button_to_add = QPushButton("add")
        self.__button_to_add.setMinimumSize(200, 80)

        self.__information_about_operation = QTextEdit()
        self.__information_about_operation.setReadOnly(True)
    
    def __layout_maker(self, is_vertical, * widgets):
        if is_vertical:
            layout = QVBoxLayout()
        else:
            layout = QHBoxLayout()
        for widget in widgets:
            layout.addWidget(widget)
        return layout


    def __go_back_button_clicked(self):
        self.__admin_window.resize(self.width(), self.height())
        self.__admin_window.move(self.pos())
        self.hide()
        self.__admin_window.show()


