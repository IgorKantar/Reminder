import json

from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QLabel,
    QFormLayout,
    QVBoxLayout,
    QLineEdit,
    QMessageBox,
    QApplication,
)

from widgets.player import SoundPlayer
from widgets.pick_sound import PickSoundWidget

class SavePresetDialog(QDialog):
    def __init__(self, parent) -> None:
        super().__init__()
        self.parent = parent
        self.form   = QFormLayout()
        self.layout = QVBoxLayout()

        self.setWindowTitle("Save Reminder")

        # WIDGETS
        buttons = QDialogButtonBox.Save | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(buttons)
        self.nameEdit  = QLineEdit()

        # FILL LAYOUTS
        self.layout.addWidget(QLabel("Enter name for reminder preset"))
        self.form.addRow(QLabel("Name: "), self.nameEdit)

        self.layout.addLayout(self.form)
        self.layout.addWidget(self.buttonBox)

        self.setLayout(self.layout)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def accept(self):
        self.save_preset()
        self.parent.mainView.refresh_presets_list()

    def save_preset(self):
        preset_json = self.collect_preset_data()
        with open("data/presets.txt", "a") as f:
            json.dump(preset_json, f)
            f.write("\n")

    def collect_preset_data(self):
        form = self.parent.mainView.form
        preset_json = {
            "name":     self.nameEdit.text(),
            "message":  form.message.text(),
            "hours":    form.wait.hours.value(),
            "minutes":  form.wait.minutes.value(),
            "seconds":  form.wait.seconds.value(),
            "sound":    form.pickSound.sound.currentText(),
            "is_repeat":form.repeat.toggle.value(),
            "times":    form.repeat.repeat.value(),
        }
        return preset_json

class MessageDialog(QMessageBox):
    def __init__(self, parent, message: str, sound: str, will_repeat: bool) -> None:
        super().__init__()
        self.parent = parent
        self.player = SoundPlayer(sound)

        with_cancel = QMessageBox.Cancel | QMessageBox.Ok
        buttons = with_cancel if will_repeat else QMessageBox.Ok

        self.setIcon(QMessageBox.Warning)
        self.setWindowTitle("Reminder Alarm")
        self.setText(message)
        self.setStandardButtons(buttons)

    def open(self):
        self.player.play() if self.player.sound else QApplication.beep()
        button = self.exec_()

        if button == QMessageBox.Ok:
            self.reject()
        if button == QMessageBox.Cancel:
            # to stop reminder repeat
            self.parent.alert_times = 0
            self.reject()