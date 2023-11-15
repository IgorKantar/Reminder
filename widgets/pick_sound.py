import os
import shutil

from PySide6.QtCore import QDir

from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QComboBox,
    QPushButton,
    QFileDialog,
)

class PickSoundWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.layout = QHBoxLayout()

        self.sound = QComboBox()
        self.new_sound = QPushButton("New Sound")

        self.fill_combobox()

        self.layout.addWidget(self.sound)
        self.layout.addWidget(self.new_sound)

        self.setLayout(self.layout)

        self.new_sound.clicked.connect(self.handle_new_sound)

    def fill_combobox(self):
        self.sound.clear()
        folder = QDir("sounds")
        # exclude '.' and '..' from list
        file_list = folder.entryList()[2:]
        for filename in file_list:
            self.sound.addItem(filename)

    def handle_new_sound(self):
        # get file path
        fpath = self.get_file_path()
        if fpath:
            head, fname = os.path.split(fpath)

            # copy file into sounds folder
            shutil.copy(src=fpath, dst="sounds")

            # refresh combobox
            self.fill_combobox()

            # set as current
            self.sound.setCurrentText(fname)

    def get_file_path(self) -> str:
        """Returns absolute path to selected audio file."""

        audioFormats = "*.mp3 *.wav *.ogg *.wma *.flac"
        filename, filter_ = QFileDialog.getOpenFileName(
            parent=None,
            caption="Select audio file",
            filter=audioFormats
        )
        return filename