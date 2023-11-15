import os

from PySide6.QtMultimedia import (
    QMediaPlayer,
    QAudioOutput,
    QMediaFormat,
)

from PySide6.QtCore import (
    QUrl,
)

basedir = os.path.dirname(__file__)

class SoundPlayer(QMediaPlayer):
    def __init__(self, sound: str) -> None:
        super().__init__()
        self.sound = sound
        url = QUrl.fromLocalFile(basedir + f"/../sounds/{sound}")

        self.output = QAudioOutput()
        self.output.setVolume(30)

        self.setAudioOutput(self.output)
        self.setSource(url)

        self.errorOccurred.connect(self.erroralert)

    def erroralert(self, *args):
        print(args)