import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        bar = self.menuBar() #获取菜单栏

        file = bar.addMenu("File")
        file.addAction("New")

        save = QAction("Save as",self)
        save.setShortcut("Command + S")
        file.addAction(save)

        save.triggered.connect(self.process)


    def process(self,a):
        print(self.sender().text())

if __name__ == '__main__':
    app =QApplication(sys.argv)
    main = Menu()
    main.show()
    sys.exit(app.exec_())
