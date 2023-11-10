from PyQt5.QtWidgets import (QMainWindow, QHBoxLayout, QLabel,
                            QPushButton, QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt

class University(QMainWindow):
    def __init__(self, users_window):
        super().__init__()
        self.__users_window = users_window

        self.setWindowTitle("University")
        self.__go_back_button = QPushButton("←")
        self.__go_back_button.clicked.connect(self.__go_back_button_clicked)
        self.__go_back_button.setMaximumWidth(40)
        self.__opening_label = QLabel(
                            "<html><b><font size='25'>SELECT NEEDED OPTION</html></b></font>"
                            )
        self.__search_by_id_button = QPushButton("search university by ID")
        self.__search_by_id_button.setMinimumHeight(80)
        self.__search_by_name_button = QPushButton("search university by NAME")
        self.__search_by_name_button.setMinimumHeight(80)
        self.__search_by_city_button = QPushButton("search university by CITY")
        self.__search_by_city_button.setMinimumHeight(80)

        self.__main_layout = self.__layout_maker(
                              True,
                              self.__go_back_button,
                              self.__opening_label,
                              self.__search_by_id_button,
                              self.__search_by_name_button,
                              self.__search_by_city_button
                        )
        self.__main_layout.setAlignment(self.__go_back_button, Qt.AlignLeft)
        self.__main_layout.setAlignment(self.__opening_label, Qt.AlignCenter)
        self.__main_widget = QWidget()
        self.__main_widget.setLayout(self.__main_layout)
        self.setCentralWidget(self.__main_widget)

    def __layout_maker(self, is_vertical, * widgets):
        if is_vertical:
            layout = QVBoxLayout()
        else:
            layout = QHBoxLayout()
        for widget in widgets:
            layout.addWidget(widget)
        return layout

    def __go_back_button_clicked(self):
        self.__users_window.resize(self.width(), self.height())
        self.__users_window.move(self.pos())
        self.hide()
        self.__users_window.show()

