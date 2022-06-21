
# pip list > requirements.txt
# Pip freeze
# pip install -r requirements.txt


import sys

# from class_ref_conv import Reference_Convert
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt6.QtWidgets import QDialog
#import gui_CR_form_G
import gui_test
from PyQt6 import uic
"""


#import gui_CR_form_G
#

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(button)

"""
"""
app = QApplication([])
win = uic.loadUi("gui_CR_form_G.ui")  # расположение вашего файла .ui

win.show()
sys.exit(app.exec())
"""


app = QApplication(sys.argv)
# app = QApplication(__name__)
# window = QDialog()
#window = QWidget()
#window = QMainWindow()
#ui = gui_CR_form_G.Ui_MainWindow(window)

#ui.setup_ui()


#ui.show()


ui = gui_test.MainWindows()
ui.show()


"""
CR = class_ref_conv.Reference_Convert()
bibtex = CR.get_data_by_doi("10.3390/s18041190")
st = CR.convert('GOST')
print(bibtex)
"""
sys.exit(app.exec())

