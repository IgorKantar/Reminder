from PySide6.QtCore import (
    QSize,
)

from PySide6.QtGui import (
    QStandardItemModel,
    QStandardItem,
)

from PySide6.QtWidgets import (
    QWidget,
    QFormLayout,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QStyle,
    QListView,
)


class PresetList(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent=parent)
        self.parent = parent
        self.layout = QVBoxLayout()

        # LIST WIDGET
        self.list = QListView()
        self.list_model = QStandardItemModel(self.list)
        self.list.setModel(self.list_model)
        self.fill_list()

        self.layout.addWidget(self.list)
        self.setLayout(self.layout)

    def fill_list(self):
        for i, preset in enumerate(self.parent.preset_list):
            item = QStandardItem("")
            item.setSizeHint(QSize(10,40))
            self.list_model.appendRow(item)
            widget = PresetItem(self.parent, i, Preset(preset))
            self.list.setIndexWidget(item.index(), widget)

class PresetItem(QWidget):
    def __init__(self, parent: QWidget, index: int, preset) -> None:
        super().__init__()
        self.layout = QHBoxLayout()

        # BUTTONS
        self.preset_button = PresetButton(parent, preset)
        self.del_button = PresetDeleteButton(parent, index)

        self.layout.addWidget(self.preset_button)
        self.layout.addWidget(self.del_button)

        self.setLayout(self.layout)

class PresetButton(QPushButton):
    def __init__(self, parent: QWidget, preset) -> None:
        super().__init__()
        # parent is MainTab
        self.parent = parent
        sound_name  = preset.sound.split(".")[0]
        button_text = [
            f"{preset.name}    sound: {sound_name}    ",
            f"time: {preset.hours}h {preset.minutes}m {preset.seconds}s"
        ]
        self.setText(" ".join(button_text))

        self.clicked.connect(lambda y=False,x=preset: self.parent.set_preset(x))

class PresetDeleteButton(QPushButton):
    def __init__(self, parent, index) -> None:
        super().__init__()
        self.parent = parent

        # CANCEL ICON
        pixmap = getattr(QStyle, "SP_DialogCancelButton")
        icon = self.style().standardIcon(pixmap)

        # ATTRIBUTES
        self.setIcon(icon)
        self.setFixedWidth(30)

        self.clicked.connect(lambda y=False, x=index: self.handle_delete(x))

    def handle_delete(self, index: int):
        self.remove_preset(index)
        self.parent.refresh_presets_list()

    def remove_preset(self, index: int):
        lines = []
        with open("data/presets.txt", "r") as f:
            lines = f.readlines()

        with open("data/presets.txt", "w") as f:
            for i, line in enumerate(lines):
                # write all same except index line
                if i != index:
                    f.write(line)

class Preset:
    def __init__(self, json: dict):
        # set attributes
        self.json = json

        for key, val in json.items():
            setattr(self, key, val)

    def __repr__(self) -> str:
        attr_list = [f"{key}: {val}" for key, val in self.__dict__.items()]
        return "\n".join(attr_list)