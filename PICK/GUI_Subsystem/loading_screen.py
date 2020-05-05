from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QMovie, QPixmap, QImage, QPalette, QBrush

class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(250,250)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)

        self.layout = QVBoxLayout()
        self.label = QLabel("Ingesting Files, please wait")

        self.layout.addWidget(self.label)
        self.setWindowTitle("Loading")
        self.setLayout(self.layout)
        self.show()

    def stopLoading(self):
        self.close()