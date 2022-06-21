from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QDialog, QApplication, QWidget, QFormLayout, QSpinBox, QMainWindow
from PyQt6.QtWidgets import (QVBoxLayout, QGridLayout, QTabWidget, QLabel, QPushButton, QFileDialog, QTextEdit,
                             QListWidget, QFrame, QTableView, QTableWidgetItem, QTableWidget, QHeaderView, QProgressBar)
#from PyQt6.QtWidgets import *
from PySide6.QtCore import QCoreApplication, QRect, Qt
# import tkFileDialog
import os  # library working with names file
from class_ref_conv import Reference_Convert, working_with_file

# global var
ref_conv = Reference_Convert()
work_file = working_with_file()
list_res_st=[]
global_table=''
Table_res=[]

class MainWindows(QDialog):   # TabDialog
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Reference_Convert   ver. 0.0.1.0")
        self.setWindowIcon(QIcon("icon.png"))
        self.setGeometry(100,100,400,400) # координаты начала и размеры

        tabwidget = QTabWidget(self)
        Tab_1 = MainTab()

        Tab_2 = ResultsTab()
        self.all_tabs = []
        self.all_tabs.append(QTabWidget())
        self.all_tabs[0] = Tab_1
        self.all_tabs[0].push_button_open_file_DOI.clicked.connect(self.the_button_open_doi_was_clicked_2)
        self.all_tabs[0].listWidget_convert_to.setCurrentRow(0)
        #self.all_tabs[0].listWidget_convert_to.listWidget_convert_to_clicked
        self.all_tabs.append(Tab_2)
        Table_res = self.all_tabs[1].table_result
        i1=tabwidget.addTab(self.all_tabs[0], "Main")
        i2=tabwidget.addTab(self.all_tabs[1], "Results")
        self.tabwidget = tabwidget
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(tabwidget)

        push_button_save = QPushButton()
        push_button_save.setGeometry(50, 150, 100, 50)
        push_button_save.setText('Save')
        push_button_save.clicked.connect(self.the_button_save)  # the_button_start
        self.push_save = push_button_save
        vboxLayout.addWidget(push_button_save)

        progressBar=QProgressBar(self)
        progressBar.resize(300, 100)
        progressBar.setValue(0)
        progressBar.setMaximum(100)
        progressBar.setMinimum(0)
        progressBar.setEnabled(0)
        progressBar.setVisible(False)
        self.progressBar=progressBar
        vboxLayout.addWidget(self.progressBar)

        push_button_start = QPushButton()
        push_button_start.setGeometry(50, 150, 50, 50)
        push_button_start.setText('Start')
        push_button_start.clicked.connect(self.the_button_start) #the_button_start
        self.push_start = push_button_start
        vboxLayout.addWidget(push_button_start)

        push_button_clear = QPushButton()
        push_button_clear.setGeometry(50, 150, 100, 50)
        push_button_clear.setText('Clear')
        push_button_clear.clicked.connect(self.the_button_clear)
        self.push_clear = push_button_clear
        vboxLayout.addWidget(self.push_clear)
        self.setLayout(vboxLayout)

    def the_button_clear(self):
        self.all_tabs[0].textEdit_Path_File_DOI.setText('')
        self.all_tabs[0].spinBox_Num_Autorth.setValue(3)
        self.all_tabs[1].table_result.setColumnCount(2)  # Set three columns
        self.all_tabs[1].table_result.setRowCount(1)  # and one row
        self.all_tabs[1].table_result.setItem(0, 0, QTableWidgetItem(""))  # Text in column 1
        self.all_tabs[1].table_result.setItem(0, 1, QTableWidgetItem(""))
       # global_table.setItem(0, 1, QTableWidgetItem("+++"))
        #tabl =

    def clarify_list_doi(self):
        # уточнение списка, если были внесены изменения вручную
        # вызывается из def the_button_start(self):
        n=self.all_tabs[1].table_result.rowCount()
        c=0
        work_file.st_list_DOI=[]
        while c<=n-1:
            st= self.all_tabs[1].table_result.item(c,0).text()
            st.split()
            work_file.st_list_DOI.append(st)
            c+=1

    def the_button_save(self):
        file_name = self.all_tabs[0].textEdit_Path_File_save.toPlainText()
        if file_name != '' and len(work_file.result_list) > 0:
           work_file.result_write_file(file_name)

    def the_button_start(self):
        st = self.all_tabs[0].textEdit_Path_File_DOI.toPlainText()  # get text
        print(str(st))

        self.progressBar.setValue(0)
        self.progressBar.setEnabled(True)
        self.progressBar.setVisible(True)
        self.progressBar.maximum =100
        self.progressBar.setRange(0, 100)
        self.show()
        flag=True
        try:
            self.clarify_list_doi() # уточнение списка, если были внесены изменения вручную
        except:
            flag=False

        L=len(work_file.st_list_DOI)
        if L>0 and flag==True:

            item_ = self.all_tabs[0].listWidget_convert_to.currentRow()
            st = Reference_Convert.type_result_Reference_list[item_]
            ref_conv.type_result=st

            ref_conv.settings_count_autors =self.all_tabs[0].spinBox_Num_Autorth.value()
           # self.clarify_list_doi() # уточнение списка, если были внесены изменения вручную
            list_res_st=[]
            c=0
            for doi in work_file.st_list_DOI:
                if c==57 or c==63 or c==97:
                    print('N woth err = ' + str(c+1))
                ref_conv.clear_dictinary()
                st=''
                if doi!= '':
                    bibtaxt=ref_conv.get_data_by_doi(doi)
                    if bibtaxt!='error':
                        st = ref_conv.convert(ref_conv.type_result)
                    else:
                        st ='error'

                else:
                    st=''
                list_res_st.append(st)
                print('N = ' + str(c+1))

                c+=1
                if c%2==0 and L>10:
                    self.progressBar.reset()
                    self.progressBar.setValue(round(c/L*100))
                else:
                    if L<=10:
                        self.progressBar.reset()
                        self.progressBar.setValue(round(c/L*100))

               
                self.progressBar.update()
        work_file.result_list = list_res_st
        add_list_result_to_Table(self.all_tabs[1].table_result, list_res_st)
        self.tabwidget.setCurrentIndex(1)

        self.progressBar.setValue(0)
        self.progressBar.setEnabled(0)
        self.progressBar.setVisible(0)

    def the_button_open_doi_was_clicked_2(self):


        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "Выбрать файл",
                                                         ".",
                                                         "Text Files(*.txt);;Excel(*.csv *.xls *.xlsx);;\
                                                         All Files(*)")

        result_file_name = os.path.basename(filename)  # name file
        result_file_path = os.path.dirname(filename)
        result_file_type = os.path.splitext(result_file_name)[1]
        self.all_tabs[0].textEdit_Path_File_DOI.setText(filename)

        L=0
        if filename !='':
            work_file.read_file_create_list_doi(filename)  # читает файл и создает в объекте список DOI
            L=len(work_file.st_list_DOI)
        if L > 0:
            add_row_DOI_to_Table(self.all_tabs[1].table_result, work_file.st_list_DOI)

        print(result_file_name)
        print(result_file_path)
        print(result_file_type)

        self.all_tabs[0].textEdit_Path_File_save.setText(result_file_path + '/' + os.path.splitext(result_file_name)[0] + '_res' + os.path.splitext(result_file_name)[1] )



class MainTab(QWidget):

    def __init__(self):
        super().__init__()  # super --- добавление к родительскому классу новых свойств и методов
        self.setObjectName("MainTab")
        self.push_button_open_file_DOI = ''
        self.textEdit_Path_File_DOI =''
        self.push_start =''
        self.label_convert_to=''
        self.listWidget_convert_to=''
        self.label_convert_to_selected=''
        self.type_result_Reference_list = Reference_Convert.type_result_Reference_list
        layout = QFormLayout()
        push_button_open_file_DOI = QPushButton()
        push_button_open_file_DOI.setGeometry(50,50, 100, 50)
        push_button_open_file_DOI.setText('Open file DOI')
        self.push_button_open_file_DOI=push_button_open_file_DOI
        layout.addWidget(push_button_open_file_DOI)

        textEdit_Path_File_DOI = QTextEdit()
        textEdit_Path_File_DOI.setGeometry(50, 50, 200, 50)
        textEdit_Path_File_DOI.setText('')
        textEdit_Path_File_DOI.Path = "a"
        textEdit_Path_File_DOI.name=""
        textEdit_Path_File_DOI.type_file=""
        self.textEdit_Path_File_DOI=textEdit_Path_File_DOI
        layout.addWidget(textEdit_Path_File_DOI)
        label_save_to = QLabel()
        label_save_to.setGeometry(50, 100, 100, 50)
        label_save_to.setText('Seve to:')
        layout.addWidget(label_save_to)

        textEdit_Path_File_save = QTextEdit()
        textEdit_Path_File_save.setGeometry(50, 50, 200, 50)
        textEdit_Path_File_save.setText('')
        textEdit_Path_File_save.Path = "a"
        textEdit_Path_File_save.name = ""
        textEdit_Path_File_save.type_file = ""
        self.textEdit_Path_File_save = textEdit_Path_File_save
        layout.addWidget(textEdit_Path_File_save)

        label_convert_to=QLabel()
        label_convert_to.setGeometry(50, 100, 100, 50)
        label_convert_to.setText('Convert to:')
        layout.addWidget(label_convert_to)

        label_convert_to_selected=QLabel()
        label_convert_to_selected.setGeometry(50, 100, 100, 50)
        label_convert_to_selected.setText('7')
        self.label_convert_to_selected= label_convert_to_selected
        layout.addWidget(label_convert_to_selected)

        listWidget_convert_to = QListWidget()
        listWidget_convert_to.setGeometry(50, 150, 100, 50)
        L=len(self.type_result_Reference_list)
        listWidget_convert_to.insertItems(0, self.type_result_Reference_list) # стандарты литературы
        listWidget_convert_to.clicked.connect(self.listWidget_convert_to_clicked)
        self.listWidget_convert_to=listWidget_convert_to
        self.listWidget_convert_to.setCurrentRow(0)
        self.listWidget_convert_to_clicked()


        layout.addWidget(listWidget_convert_to)

        frame_count_autorth=QFrame()
        frame_count_autorth.setGeometry(50, 100, 100, 50)
        frame_count_autorth.setStyleSheet('background-color: rgb(100,100,100)')
        self.frame_count_autorth=frame_count_autorth

        self.label_restrictions = QLabel(self.frame_count_autorth)
        self.label_restrictions.setObjectName(u"label_restrictions")
        self.label_restrictions.setGeometry(20, 10, 47, 13)  #?????????????  QRect
        self.label_restrictions.setText('Restric')

        self.label_Num_Autorth = QLabel(self.frame_count_autorth)
        self.label_Num_Autorth.setObjectName(u"label_Num_Autorth")
        self.label_Num_Autorth.setText('Count Autorth:')
        self.label_Num_Autorth.setGeometry(20, 40, 111, 20)

        self.spinBox_Num_Autorth = QSpinBox(self.frame_count_autorth)
        self.spinBox_Num_Autorth.setObjectName(u"spinBox_Num_Autorth")
        self.spinBox_Num_Autorth.setGeometry(130, 40, 51, 22)
        self.spinBox_Num_Autorth.setSingleStep(1)
        self.spinBox_Num_Autorth.setValue(3)



        layout.addWidget(self.frame_count_autorth)
        layout.addWidget(self.label_restrictions)
        layout.addWidget(self.label_Num_Autorth)
        layout.addWidget(self.spinBox_Num_Autorth)

        self.setLayout(layout)

    def listWidget_convert_to_clicked (self):
        #item_= item.text() #
        # self.listWidget_convert_to.currentItem() #self.listWidget_convert_to.currentItem()
        item_=self.listWidget_convert_to.currentRow()
        st = self.type_result_Reference_list[item_]
        self.label_convert_to_selected.setText(' ' + st) # view selected format result

class ResultsTab(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName('Tab_results')
        grid_layout = QGridLayout(self)  # Create QGridLayout
        #central_widget.setLayout(grid_layout)  # Set this layout in central widget

        table = QTableWidget(self)  # Create a table
        table.setColumnCount(2)  # Set two columns
        table.setRowCount(1)  # and one row
        table.setColumnWidth(0, 400)
        table.setColumnWidth(1, 400)

        self.edittable = QTextEdit(self) #поле редактирования ячейки
        self.tabledefault = QLabel(self) #поле сохранения изначального значения ячейки
        self.tabledefault.setWordWrap(True)
        self.savebutton = QPushButton(self)
        self.undobutton = QPushButton(self)

        self.savebutton.setText('Save to table')
        self.undobutton.setText('Undo')

        # Set the table headers
        table.setHorizontalHeaderLabels(["DOI", "Referens result"])
       # style=QHeaderView.Stretch
       # table.horizontalHeader(1).setSectionResizeMode(style)  #  setSectionResizeMode(1)  #

       # table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)

        # Set the tooltips to headings  - всплывающая подсказка
        table.horizontalHeaderItem(0).setToolTip("Исходные данные ")
        table.horizontalHeaderItem(1).setToolTip("Результат")


        # Set the alignment to the headers
        table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter) #Qt.AlignLeft
        table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
      #  table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)

        # Fill the first line
        table.setItem(0, 0, QTableWidgetItem(""))#Text in column 1
        table.setItem(0, 1, QTableWidgetItem(""))
       # table.setItem(0, 2, QTableWidgetItem("Text in column 3"))

        # Do the resize of the columns by content
        table.resizeColumnsToContents()

        grid_layout.addWidget(table, 0, 0, 1, 2)  # Adding the table to the grid
        grid_layout.addWidget(self.edittable, 1, 0, 1, 2)
        self.edittable.setMaximumSize(1000, 70)
        grid_layout.addWidget(self.tabledefault, 3, 0, 1, 2)
        grid_layout.addWidget(self.undobutton, 4, 1)
        grid_layout.addWidget(self.savebutton, 4, 0)
        self.table_result=table
        # global_table = self.table_result
        self.table_result.cellClicked.connect(self.handleCellClicked)
        self.undobutton.clicked.connect(self.textundo)
        self.savebutton.clicked.connect(self.textsave)

    def handleCellClicked(self, row, column): #функция копирования текста в поле при нажатии на ячейку
        text = self.table_result.item(row, column)
        text = text.text()
        self.edittable.setPlainText(text)
        self.tabledefault.setText(text)
        self.rowclick = row
        self.colclick = column

    def textsave(self): #функция сохранения значения ячейки из поля
        text = self.edittable.toPlainText()
        text = QTableWidgetItem(text)
        self.table_result.setItem(self.rowclick, self.colclick, text)

    def textundo(self): #функция отката текстового поля до изачального
        text = self.tabledefault.text()
        self.edittable.setPlainText(text)



""""

        layout = QFormLayout()

        tableView_Result = QTableView()


        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)


        tab_two_label_one = QLabel("tab_two_label_one")
        tab_two_label_two = QLabel("tab_two_label_two")

        second_layout = QVBoxLayout()
        second_layout.addWidget(tab_two_label_one)
        second_layout.addWidget(tab_two_label_two)
        self.setLayout(second_layout)
"""
"""
if __name__ == "__main__":
    app = QApplication(sys.argv)
    tabdialog = TabDialog()
    tabdialog.show()
    app.exec()
"""


def add_row_DOI_to_Table(Table_QT, List_DOI):
    Table_QT.setColumnCount(2)  # Set three columns
    Table_QT.setRowCount(1)  # and one row
    L= len(List_DOI)
    Table_QT.setRowCount(L)
    c=0
    for doi in List_DOI:
        Table_QT.setItem(c, 0, QTableWidgetItem(doi))
        c+=1

def add_list_result_to_Table(Table_QT, list_result):
   # Table_QT.setColumnCount(2)  # Set three columns
   # Table_QT.setRowCount(1)  # and one row
    L= len(list_result)
    # Table_QT.setRowCount(L)
    c=0
    for st in list_result:
        Table_QT.setItem(c, 1, QTableWidgetItem(st))
        c+=1