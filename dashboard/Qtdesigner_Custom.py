import sys

from PySide6.QtWidgets import QMainWindow, QApplication

from interface import *

from Custom_Widgets.Widgets import *

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self)
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


'''
(.venv) PS D:\Python\GiaoDienSample> cd D:\Python\GiaoDienSample\dashboard
(.venv) PS D:\Python\GiaoDienSample\dashboard> pyside6-uic interface.ui -o interface.py
(.venv) PS D:\Python\GiaoDienSample\dashboard> pyside6-rcc resources.qrc -o resources_rc.py

##QCustom
pip install QT-PyQt-PySide-Custom-Widgets
https://pypi.org/project/QT-PyQt-PySide-Custom-Widgets/

##JSON Style
https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/docs/widgets/custom-slide-menu-widgets
'''