from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
import secrets
class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.code_create.clicked.connect(self.generate_password)


    def generate_password(self):
        password = secrets.token_hex(6)
        self.ui.password_label.setText(password)
        with open("my pass.txt", "a") as file:
            file.write('\n' + password)


app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
