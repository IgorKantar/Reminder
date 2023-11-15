#!/usr/bin/env python
from os.path import (
    dirname,
    exists,
)

import sys

from PySide6.QtCore import QDir

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
)

from widgets.tab import MainTab
from qss import QSS_STRING

basedir = dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # WIDGETS
        self.mainView = MainTab(self)

        # menu = self.menuBar()
        # for menu_name in ["File", "Help"]:
        #     menu.addMenu(menu_name)

        # WINDOW ATTRIBUTES
        self.setWindowTitle("Reminder")
        self.setFixedSize(350, 300)
        # self.setStyleSheet(QSS_STRING)

        self.setCentralWidget(self.mainView)

def check_folders(folder_names: list[str]):
    for name in folder_names:
        if not QDir(name).exists():
            QDir().mkdir(name)

def check_data():
    # create files if they dont exist
    for fname in ["presets.txt","settings.txt","last_picked.txt",]:
        if not exists(f"data/{fname}"):
            with open(f"data/{fname}", "x") as f:
                pass

if __name__ == "__main__":
    app = QApplication()

    check_folders([
        "sounds",
        "data",
    ])

    check_data()

    window = MainWindow()
    window.show()

    app.exec()
