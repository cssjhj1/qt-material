from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from qt_material import QtStyleTools


########################################################################
class RuntimeStylesheets(QMainWindow, QtStyleTools):
    # ----------------------------------------------------------------------
    def __init__(self):
        """"""
        super().__init__()
        self.main = QUiLoader().load('main_window.ui', self)

        self.main.pushButton.clicked.connect(lambda: self.apply_stylesheet(self.main, 'dark_teal.xml'))
        self.main.pushButton_2.clicked.connect(lambda: self.apply_stylesheet(self.main, 'light_red.xml'))
        self.main.pushButton_3.clicked.connect(lambda: self.apply_stylesheet(self.main, 'light_blue.xml'))


if __name__ == "__main__":
    app = QApplication()
    frame = RuntimeStylesheets()
    frame.main.show()
    app.exec_()

