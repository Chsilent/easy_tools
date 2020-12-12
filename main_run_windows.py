import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_window.main_windows import Ui_MainWindow


class MyWindows(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        """
        init my windows
        :param parent:
        """
        super(MyWindows, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindows()
    myWin.show()
    sys.exit(app.exec_())
