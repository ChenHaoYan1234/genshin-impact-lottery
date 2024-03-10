import random

from PySide6 import QtMultimedia
from PySide6.QtCore import QSize, QUrl

import resource_rc
from BaseMainWindow import Ui_MainWindow


class MainWindow(Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.setFixedSize(QSize(1280, 720))

        self.media_player = QtMultimedia.QMediaPlayer(self.video)
        self.media_player.setVideoOutput(self.video)
        self.audio_output = QtMultimedia.QAudioOutput()
        self.media_player.setAudioOutput(self.audio_output)

        self.video.setVisible(False)
        self.result.setVisible(False)

        self.name.raise_()
        self.closeButton.raise_()

        self.one.clicked.connect(self.oneClicked)
        self.ten.clicked.connect(self.tenClicked)

        self.ten.setDisabled(True)

        self.setupList()

    def setupList(self):
        with open("list.txt", encoding="utf-8") as f:
            self.list = f.read().splitlines()

    def oneClosed(self):
        self.start.setVisible(True)
        self.result.setVisible(False)

    def onePlayed(self, status):
        if status == QtMultimedia.QMediaPlayer.MediaStatus.EndOfMedia:
            self.result.setVisible(True)
            self.video.setVisible(False)
            self.name.setText(random.choice(self.list))
            try:
                self.closeButton.clicked.disconnect()
            except:
                pass
            self.closeButton.clicked.connect(self.oneClosed)

    def oneClicked(self):
        self.video.setVisible(True)
        self.start.setVisible(False)
        self.media_player.setSource(QUrl("qrc:/videos/one.mp4"))
        try:
            self.media_player.mediaStatusChanged.disconnect()
        except:
            pass
        self.media_player.mediaStatusChanged.connect(self.onePlayed)
        self.media_player.setPosition(0)
        self.media_player.play()

    def tenClosed(self):
        if self.choiceList != []:
            self.name.setText(self.choiceList.pop())
        else:
            self.result.setVisible(False)
            self.start.setVisible(True)

    def tenPlayed(self, status):
        if status == QtMultimedia.QMediaPlayer.MediaStatus.EndOfMedia:
            self.result.setVisible(True)
            self.video.setVisible(False)
            self.choiceList = []
            tmp = self.list.copy()
            while len(self.choiceList) <= 9:
                choice = random.choice(tmp)
                tmp.remove(choice)
                self.choiceList.append(choice)
            self.name.setText(self.choiceList.pop())
            try:
                self.closeButton.clicked.disconnect()
            except:
                pass
            self.closeButton.clicked.connect(self.tenClosed)

    def tenClicked(self):
        self.video.setVisible(True)
        self.start.setVisible(False)
        self.media_player.setSource(QUrl("qrc:/videos/ten.mp4"))
        try:
            self.media_player.mediaStatusChanged.disconnect()
        except:
            pass
        self.media_player.mediaStatusChanged.connect(self.tenPlayed)
        self.media_player.setPosition(0)
        self.media_player.play()
