import sys

from PySide6.QtWidgets import QApplication

from MainWindow import Ui_MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Ui_MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
