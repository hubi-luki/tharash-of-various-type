rom PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDialog, QLineEdit, QLabel
from PyQt5 import QtCore


class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.textbox = QLineEdit("0")

        self.button_yes = QPushButton("Ok")
        self.button_no = QPushButton("Cancel")

        self.button_yes.clicked.connect(self.accept)
        self.button_no.clicked.connect(self.reject)

        self.layout.addWidget(self.textbox)
        self.layout.addWidget(self.button_yes)
        self.layout.addWidget(self.button_no)
        self.setLayout(self.layout)


class MainWindow(QWidget):
    def __init__(self, app):
        super().__init__()
        self.numbers = []
        self.counter = 0

        self.setFixedSize(150, 150)
        self.layout = QVBoxLayout()
        self.button = QPushButton("Show Dialog")
        self.button.clicked.connect(self.on_show_dialog)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.label = QLabel("Result: ")

        self.label.setAlignment(QtCore.Qt.AlignTop)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.layout.addWidget(self.label)
        self.show()

    def on_show_dialog(self):
        dial = Dialog()
        self.label.setText("Result: ")
        if dial.exec_() == QDialog.Accepted:

            self.counter += 1
            print(dial.textbox.text())
            try:
                self.numbers.append(float(dial.textbox.text()))
            except Exception:
                print("Invalid number")

            if self.counter == 2:
                self.label.setText("Result: " + str(self.numbers[0] + self.numbers[1]))
                self.counter = 0
                self.numbers = []

        elif dial.exec_() == QDialog.Rejected:
            print("rejected")


app = QApplication([])
new = MainWindow(app)
app.exec_()
