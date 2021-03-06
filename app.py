
from controller import *
from model import *
from view import *
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFontDatabase,QIcon
import sys


class App(QMainWindow):
    def __init__(self) -> None:
        super(App,self).__init__()
        self.model = Model()
        self.view = View(self.model)
        self.controller = Controller(view=self.view,model=self.model)
        
    
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont('resources/fonts/segoeui.ttf')
    app.setWindowIcon(QIcon("resources/mcord_icon.ico"))
    my_app = App()
    sys.exit(app.exec())