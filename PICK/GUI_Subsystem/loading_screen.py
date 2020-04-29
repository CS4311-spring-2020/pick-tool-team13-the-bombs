from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QMovie, QPixmap, QImage, QPalette, QBrush

class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(450,450)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
        oImage = QImage("loading.jpg")
        sImage = oImage.scaled(QSize(450,450))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                     # 10 = Windowrole
        self.setPalette(palette)

        self.show()

    def stopLoading(self):
        self.close()