import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget, QWidget, QMainWindow, QPushButton, QTextEdit, QTabWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from PyQt6 import uic
import time
from PyQt5 import QtGui

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("MainWindowSeagull.ui", self)
        self.setWindowTitle("Seagull Identifier")
        self.home.setCurrentIndex(0)
        self.setFixedSize(650,450)

        QTextEdit.isReadOnly = True

        def SetCurrentWindow(self, windowNumber):
            self.home.setCurrentIndex(windowNumber)
            print(f"Window number is = {windowNumber}")

        #WHITE HEAD FIRST

        self.bWhiteHead.clicked.connect(lambda: SetCurrentWindow(self,1))


        ##BLACK FEET

        self.BlackFeetButton.clicked.connect(lambda: SetCurrentWindow(self,9))

        self.GraKropp.clicked.connect(lambda: SetCurrentWindow(self,10))  
        self.HvitKropp.clicked.connect(lambda: SetCurrentWindow(self,11))  

        ##PINK FEET
        self.PinkFeetButton.clicked.connect(lambda: SetCurrentWindow(self,5))

        self.BlackFeathers.clicked.connect(lambda: SetCurrentWindow(self,6))  
        self.GrayFeathers.clicked.connect(lambda: SetCurrentWindow(self,7))  
        self.WhiteFeathers.clicked.connect(lambda: SetCurrentWindow(self,8))  

        ##YELLOW FEET
        self.YellowFeetButton.clicked.connect(lambda: SetCurrentWindow(self,2))  

        self.RedBeakButton.clicked.connect(lambda: SetCurrentWindow(self,3))
        self.NonRedBeakButton.clicked.connect(lambda: SetCurrentWindow(self,4))

        #BLACK HEAD

        self.bBlackHead.clicked.connect(lambda: SetCurrentWindow(self,12))

        self.DelvisSvart.clicked.connect(lambda: SetCurrentWindow(self,13))
        self.HeltSvart.clicked.connect(lambda: SetCurrentWindow(self,16))
        
        self.HelRodtNebb.clicked.connect(lambda: SetCurrentWindow(self,15))
        self.DelvisSvartNebb.clicked.connect(lambda: SetCurrentWindow(self,14))

        self.rodenebbsvarthode.clicked.connect(lambda: SetCurrentWindow(self,17))
        self.gultnebbsvarthode.clicked.connect(lambda: SetCurrentWindow(self,18))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myApp = MyApp()

    myApp.setStyleSheet('''

        QMainWindow {
            background-color: #85ccbb;
            }

        QTextEdit, QPushButton,QLineEdit {
            font-size: 15px;
            background-color: ##ffffff;
            }

    ''')

    myApp.show()

    app.exec()
