import sys
import mainWinSignalSolt
from PyQt5.QtWidgets import QMainWindow,QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = mainWinSignalSolt.Ui_MainWindow()
    #向主窗口添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())