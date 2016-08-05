import sys
from PyQt4.QtGui import QApplication, QMainWindow, QPushButton,QVBoxLayout, QWidget, QTextEdit
app = QApplication([])
mainwindow = QMainWindow()
mainwindow.setWindowTitle("Koidu ja Martini Maagia")
button_MAGIC = QPushButton("DO MAGIC")
#button_dancing = QPushButton("Dancing now")
#button_right = QPushButton("Right")
#button_left = QPushButton("Turn left")
#button_exit = QPushButton("Stop")
#button_distance = QPushButton("Show the condinate")
vbox = QVBoxLayout()
vbox.addStretch(1)
#vbox.addWidget(button_exit)
vbox.addWidget(button_MAGIC)
#vbox.addWidget(button_dancing)
#vbox.addWidget(button_right)
#vbox.addWidget(button_left)
#vbox.addWidget(button_distance)
textedit = QTextEdit("")
vbox.addWidget(textedit)
# This is some silly Qt-ism
container = QWidget()
container.setLayout(vbox)
mainwindow.setCentralWidget(container)
mainwindow.show()

def MAGIC(MAGIC):
    print (textedit)
    


button_MAGIC.clicked.connect(MAGIC)

sys.exit(app.exec_()) # This is basically infinite loop here, it blocks everything else!

