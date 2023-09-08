from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QLabel,QVBoxLayout
from random import randint

app = QApplication([])

main_win = QWidget()
main_win.show()
main_win.setWindowTitle("Визначник переможця")
main_win.resize(400,200)

winner = QLabel('Натисни, щоб дізнатися переможця')
number = QLabel('?')
button = QPushButton('Згенерувати')

line = QVBoxLayout()
line.addWidget(winner ,alignment=Qt.AlignCenter)
line.addWidget(number ,alignment=Qt.AlignCenter)
line.addWidget(button ,alignment=Qt.AlignCenter)

main_win.setLayout(line)

def show_winner():
    randnumb = randint(1, 100)
    winner.setText ("Переможець:")
    number.setText (str(randnumb))

button.clicked.connect(show_winner)

app.exec_()


