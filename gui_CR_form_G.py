# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_CR_form_G.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QTabWidget,
    QTableView, QTextEdit, QWidget, QFileDialog)


import os # library working with names file

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(639, 479)
        MainWindow.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget_Main = QTabWidget(self.centralwidget)
        self.tabWidget_Main.setObjectName(u"tabWidget_Main")
        self.tabWidget_Main.setGeometry(QRect(30, 20, 601, 431))
        palette = QPalette()
        brush = QBrush(QColor(170, 170, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush)
        self.tabWidget_Main.setPalette(palette)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.pushButton_open_file_doi = QPushButton(self.tab)
        self.pushButton_open_file_doi.setObjectName(u"pushButton_open_file_doi")
        self.pushButton_open_file_doi.setGeometry(QRect(20, 10, 181, 31))
        self.push_button_open_file_DOI.clicked.connect(self.the_button_open_doi_was_clicked)

        self.textEdit_Path_File_DOI = QTextEdit(self.tab)
        self.textEdit_Path_File_DOI.setObjectName(u"textEdit_Path_File_DOI")
        self.textEdit_Path_File_DOI.setGeometry(QRect(20, 50, 551, 31))
        self.listWidget_Typs_Format = QListWidget(self.tab)
        self.listWidget_Typs_Format.setObjectName(u"listWidget_Typs_Format")
        self.listWidget_Typs_Format.setGeometry(QRect(20, 130, 131, 121))
        self.label_conver_to = QLabel(self.tab)
        self.label_conver_to.setObjectName(u"label_conver_to")
        self.label_conver_to.setGeometry(QRect(20, 110, 61, 16))
        self.label_selected = QLabel(self.tab)
        self.label_selected.setObjectName(u"label_selected")
        self.label_selected.setGeometry(QRect(20, 260, 61, 16))
        self.pushButton_Convert = QPushButton(self.tab)
        self.pushButton_Convert.setObjectName(u"pushButton_Convert")
        self.pushButton_Convert.setGeometry(QRect(40, 330, 75, 23))
        self.pushButton_clear = QPushButton(self.tab)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setGeometry(QRect(470, 330, 75, 23))
        self.label_Type_Selected = QLabel(self.tab)
        self.label_Type_Selected.setObjectName(u"label_Type_Selected")
        self.label_Type_Selected.setGeometry(QRect(20, 280, 101, 16))
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(290, 130, 241, 71))
        palette1 = QPalette()
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        self.frame.setPalette(palette1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_restrictions = QLabel(self.frame)
        self.label_restrictions.setObjectName(u"label_restrictions")
        self.label_restrictions.setGeometry(QRect(20, 10, 47, 13))
        self.spinBox_Num_Autorth = QSpinBox(self.frame)
        self.spinBox_Num_Autorth.setObjectName(u"spinBox_Num_Autorth")
        self.spinBox_Num_Autorth.setGeometry(QRect(130, 40, 51, 22))
        self.spinBox_Num_Autorth.setSingleStep(1)
        self.spinBox_Num_Autorth.setValue(3)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 111, 20))
        self.pushButton_close = QPushButton(self.tab)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setGeometry(QRect(470, 360, 75, 23))
        self.pushButton_close.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.tabWidget_Main.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tableView_Result = QTableView(self.tab_2)
        self.tableView_Result.setObjectName(u"tableView_Result")
        self.tableView_Result.setGeometry(QRect(30, 20, 541, 301))
        self.label__Res_saved = QLabel(self.tab_2)
        self.label__Res_saved.setObjectName(u"label__Res_saved")
        self.label__Res_saved.setGeometry(QRect(0, 340, 111, 20))
        self.textEdit_Seved_to_File = QTextEdit(self.tab_2)
        self.textEdit_Seved_to_File.setObjectName(u"textEdit_Seved_to_File")
        self.textEdit_Seved_to_File.setGeometry(QRect(120, 340, 451, 31))
        self.tabWidget_Main.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 639, 25))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.tabWidget_Main.setCurrentIndex(0)
        self.pushButton_open_file_doi.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PPG SIGNAL", None))
        self.pushButton_open_file_doi.setText(QCoreApplication.translate("MainWindow", u"Open file with DOI", None))
        self.label_conver_to.setText(QCoreApplication.translate("MainWindow", u"Convert to", None))
        self.label_selected.setText(QCoreApplication.translate("MainWindow", u"Selected", None))
        self.pushButton_Convert.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_Type_Selected.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_restrictions.setText(QCoreApplication.translate("MainWindow", u"Restrictions", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Num. Autorth", None))
        self.pushButton_close.setText(QCoreApplication.translate("MainWindow", u"\u0421lose", None))
        self.tabWidget_Main.setTabText(self.tabWidget_Main.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Main", None))
        self.label__Res_saved.setText(QCoreApplication.translate("MainWindow", u"Result seved to", None))
        self.tabWidget_Main.setTabText(self.tabWidget_Main.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Result", None))

    def the_button_open_doi_was_clicked(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "Выбрать файл",
                                                         ".",
                                                         "Text Files(*.txt);;JPEG Files(*.jpeg);;\
                                                         PNG Files(*.png);;GIF File(*.gif);;All Files(*)")

        result_file_name = os.path.basename(filename)  # name file
        result_file_path = os.path.dirname(filename)
        result_file_type = os.path.splitext(result_file_name)[1]
    # retranslateUi

