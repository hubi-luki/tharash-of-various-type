from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5 import QtCore


class Window(QWidget):
    def __init__(self, app):
        super().__init__()

        self.timer = QtCore.QTimer()

        # Overall look

        self.setStyleSheet("background-color: black")
        self.layout = QVBoxLayout()
        self.setWindowTitle("Traffic Light")
        self.setFixedSize(300, 900)

        # Top element

        self.top_light = QLabel()
        self.top_light.move(0, 0)
        self.top_light.resize(100, 100)
        self.top_light.setStyleSheet("background: red; border-radius: 137; width: 300; height: 300;")

        self.layout.addWidget(self.top_light)

        # Mid element

        self.mid_light = QLabel()
        self.mid_light.move(0, 300)
        self.mid_light.resize(300, 300)
        self.mid_light.setStyleSheet("background: black; border-radius: 137; width: 300; height: 300;")

        self.layout.addWidget(self.mid_light)

        # Bot element

        self.bot_light = QLabel()
        self.bot_light.move(0, 600)
        self.bot_light.resize(300, 300)
        self.bot_light.setStyleSheet("background: black; border-radius: 137; width: 300; height: 300;")

        self.layout.addWidget(self.bot_light)

        self.setLayout(self.layout)
        self.run()
        self.show()

    # Functions

    def set_red(self):
        self.top_light.setStyleSheet("background: red; border-radius: 137; width: 300; height: 300;")
        self.mid_light.setStyleSheet("background: black; border-radius: 137; width: 300; height: 300;")
        self.bot_light.setStyleSheet("background: black; border-radius: 137; width: 300; height: 300;")

    def set_red_yellow(self):
        self.top_light.setStyleSheet("background: red; border-radius: 137; width: 300; height: 300;")
        self.mid_light.setStyleSheet("background: yellow; border-radius: 137; width: 300; height: 300;")
        self.bot_light.setStyleSheet("background: black; border-radius: 137; width: 300; height: 300;")

    def set_green(self):
        self.top_light.setStyleSheet("background: black; border-radius: 137; width: 300; height: 300;")
        self.mid_light.setStyleSheet("background: black; border-radius: 137; width: 300; height: 300;")
        self.bot_light.setStyleSheet("background: green; border-radius: 137; width: 300; height: 300;")

    def set_yellow(self):
        self.top_light.setStyleSheet("background: black; border-radius: 137; width: 300; height: 300;")
        self.mid_light.setStyleSheet("background: yellow; border-radius: 137; width: 300; height: 300;")
        self.bot_light.setStyleSheet("background: black; border-radius: 137; width: 300; height: 300;")

    def run(self):
        self.set_red()
        self.timer.singleShot(5000, self.set_red_yellow)
        self.timer.singleShot(7000, self.set_green)
        self.timer.singleShot(12000, self.set_yellow)
        self.timer.singleShot(14000, self.run)


app = QApplication([])
new = Window(app)
app.exec_()
