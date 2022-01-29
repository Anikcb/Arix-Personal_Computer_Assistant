import sys
from Arix import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
    
            
            
startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def __del__(self):
        sys.stdout = sys.__stdout__


    def startTask(self):

        self.ui.movie = QtGui.QMovie("run.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("heart.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("anik.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()

        startExecution.start()



app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())