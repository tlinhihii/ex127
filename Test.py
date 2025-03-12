from PyQt6.QtWidgets import QApplication, QMainWindow

from ex127.MainWindow127Ex import MainWindow127Ex

app=QApplication([])
myWindow=MainWindow127Ex()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()