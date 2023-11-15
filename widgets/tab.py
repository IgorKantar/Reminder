import json

from os.path import exists

from PySide6.QtWidgets import(
    QTabWidget,
    QLabel
)

from widgets.form import ReminderForm
from widgets.presets import PresetList, Preset

class MainTab(QTabWidget):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.preset_list = self.get_presets()
        self.last_preset = self.get_last_picked()

        self.form = ReminderForm(parent)
        self.presets = PresetList(self)

        self.addTab(self.form, "Form")
        self.addTab(self.presets, "Presets")

        self.set_preset(self.last_preset)

    def get_presets(self) -> list[dict]:
        "Returns list od dicts representing form presets."

        with open("data/presets.txt", "r") as f:
            preset_list = [json.loads(line) for line in f.readlines()]

        return preset_list

    def set_preset(self, preset: Preset):
        # set message
        self.form.message.setText(preset.message)

        # set time
        self.form.wait.hours.setValue(int(preset.hours))
        self.form.wait.minutes.setValue(int(preset.minutes))
        self.form.wait.seconds.setValue(int(preset.seconds))

        # set sound
        self.form.pickSound.sound.setCurrentText(preset.sound)

        # set repeat
        self.form.repeat.toggle.setValue(int(preset.is_repeat))
        self.form.repeat.repeat.setValue(int(preset.times))

    def set_last_picked(self, preset: Preset):
        with open("data/last_picked.txt", "w") as f:
            json.dump(preset.json, f)

    def get_last_picked(self) -> Preset:
        with open("data/last_picked.txt", "r") as f:
            json_ = json.loads(f.readline())

        return Preset(json=json_)

    def get_current_json(self) -> Preset:
        current_json = {
            "message":  self.form.message.text(),
	        "hours":    self.form.wait.hours.value(),
	        "minutes":  self.form.wait.minutes.value(),
	        "seconds":  self.form.wait.seconds.value(),
	        "sound":    self.form.pickSound.sound.currentText(),
	        "is_repeat":self.form.repeat.toggle.value(),
	        "times":    self.form.repeat.repeat.value(),
        }
        return Preset(current_json)

    def get_seconds(self) -> int:
        """Returns time from the form tab converted into seconds."""

        hours   = self.form.wait.hours.value()
        minutes = self.form.wait.minutes.value()
        seconds = self.form.wait.seconds.value()
        return hours * 3600 + minutes * 60 + seconds

    def refresh_presets_list(self):
        # clear list
        self.presets.list_model.removeRows(0, self.presets.list_model.rowCount())
        # get updated presets
        self.preset_list = self.get_presets()
        # fill list
        self.presets.fill_list()