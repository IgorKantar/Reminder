from PySide6.QtCore import (
    Qt,
)

from PySide6.QtWidgets import (
    QWidget,
    QFormLayout,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QMessageBox,
    QLineEdit,
    QSpinBox,
    QSlider,
)

from time import sleep
from .dialogs import *

class ReminderForm(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.form_lay = QFormLayout()

        self.message = QLineEdit()
        self.wait = TimeInsertWidget(parent)
        self.repeat = RepeatInsertWidget(parent)
        self.buttons = ButtonsWidget(parent)
        self.pickSound = PickSoundWidget()

        for text, widget in [
            ("Message:", self.message),
            ("Wait:", self.wait),
            ("Sound:", self.pickSound),
            ("Repeat:", self.repeat),
            ]:
            self.form_lay.addRow(QLabel(text), widget)

        self.layout.addLayout(self.form_lay)
        self.layout.addWidget(self.buttons)

        self.setLayout(self.layout)

class ReminderMessageBox(QMessageBox):
    def __init__(self, parent: QWidget, message: str) -> None:
        super().__init__(parent)
        self.setWindowTitle("Reminder Alarm")
        self.setText(message)

class TimeInsertWidget(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.layout = QHBoxLayout()

        # SPINBOXES
        self.hours   = QSpinBox()
        self.minutes = QSpinBox()
        self.seconds = QSpinBox()

        for sbox, label in [
            (self.hours, "h"),
            (self.minutes, "min"),
            (self.seconds, "sec"),
        ]:
            self.layout.addWidget(sbox)
            self.layout.addWidget(QLabel(label))

        self.setLayout(self.layout)

class RepeatInsertWidget(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.layout = QHBoxLayout()

        # WIDGETS
        self.label  = QLabel(" times")
        self.repeat = QSpinBox()
        self.toggle = QSlider(Qt.Orientation.Horizontal)

        # WIDGET ATTRIBUTES
        self.toggle.setMaximum(1)
        self.toggle.setMinimum(0)
        self.toggle.setSingleStep(1)
        self.toggle.setFixedWidth(40)

        # FILL LAYOUT
        for w in [self.toggle, self.repeat, self.label]:
            self.layout.addWidget(w)

        self.setLayout(self.layout)

class ButtonsWidget(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.parent = parent
        self.layout = QHBoxLayout()

        self.setButton  = QPushButton("Set")
        self.saveButton = QPushButton("Save")

        for b in [self.saveButton, self.setButton]:
            self.layout.addWidget(b)

        self.setLayout(self.layout)

        self.saveButton.clicked.connect(self.save_clicked)
        self.setButton.clicked.connect(self.on_set_click)

    def save_clicked(self):
        dlg = SavePresetDialog(self.parent)
        dlg.exec_()

    def on_set_click(self):
        tab = self.parent.mainView
        current_data = tab.get_current_json()
        # save as last set alarm
        tab.set_last_picked(current_data)

        sound   = current_data.sound
        message = current_data.message
        repeat_times   = current_data.times
        repeat_toggled = current_data.is_repeat
        seconds = tab.get_seconds()

        # begin alarm loop
        self.alert_times = repeat_times+1 if repeat_toggled else 1
        while self.alert_times > 0:
            will_repeat = repeat_toggled and self.alert_times > 1
            dialog  = MessageDialog(self, message, sound, will_repeat)
            self.wait(seconds)
            # show message after time runs out
            dialog.open()
            self.alert_times -= 1

    def wait(self, seconds: int):
        self.parent.hide()
        sleep(seconds)
        self.parent.show()
        # self.parent.showMinimized()
        # self.parent.showMaximized()