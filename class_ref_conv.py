# class_ref_conv.py
import sys
import re
import urllib.request
from urllib.error import HTTPError
import os  # library working with names file
from pylatexenc.latex2text import LatexNodes2Text

class Reference_Convert:
    type_card_list = ('BibTex', 'EndNote', 'Simple TEXT file', 'Reference meneger')  # kortege  tuple
    type_result_Reference_list = ("GOST","Harvard", "Vancouver")  # tuple
    type_lengv = ('Ru', 'Engl')

    def __init__(self):
        # dictinary
        self.dictinary = {
            "authors": [],
            "full_initial": [],
            "short_initial": [],  # инициалы с точкой, между ними пробелы
            "title": "",
            "volume": "",
            "number": "",
            "year": "",
            "doi": "",
            "ISSN": "",
            "url": "",
            "pages": "",
            "journal": "",
            "publishing_house": "",  # издательство
            "data": "",
            "type_print": "",
            "science_section": ""
        }
        self.flag_availability_data = False  # данные присутствуют, можно форматировать: False - нет, True - да

        self.settings_count_autors = 3
        self.type_card = 'BibTex'  # 'BibTex', 'EndNote'.....
        # self.curent_result=""
        self.Lengv = self.type_lengv[1]
        self.Result = ""
        self.type_result = self.type_result_Reference_list[0]

    def clear_dictinary(self):
       # dictinary
        self.dictinary = {
            "authors": [],
            "full_initial": [],
            "short_initial": [],  # инициалы с точкой, между ними пробелы
            "title": "",
            "volume": "",
            "number": "",
            "year": "",
            "doi": "",
            "ISSN": "",
            "url": "",
            "pages": "",
            "journal": "",
            "publishing_house": "",  # издательство
            "data": "",
            "type_print": "",
            "science_section": ""
        }
        self.flag_availability_data = False
        self.Result = ""

    def convert(self, type_result_Reference):

        if type_result_Reference == '':
            type_result_Reference = self.type_result

        match self.type_card:  # из какого типа файла берутся исходные данные, BibTex
            case "BibTex":
                if type_result_Reference == "GOST":  # ГОСТ
                    self.Result = ""
                    if self.flag_availability_data == True:
                        self.Result = self.convert_to_GOST()
                if type_result_Reference == "Harvard":  # ГОСТ
                    self.Result = ""
                    if self.flag_availability_data == True:
                        self.Result = self.convert_to_Harvard()        
        return self.Result

    def convert_to_Harvard(self):
        st = ''
        if self.flag_availability_data == True:

            # ------  Lengvich
            stt = self.dictinary["authors"][0]
            stt = stt[0]
            # print('st=' + stt + '...')
            if re.match('[а-яА-Я]', stt):
                self.Lengv = self.type_lengv[0]  # "Ru"
            elif re.match('[A-Za-z]', stt):
                self.Lengv = self.type_lengv[1]  # Engl
           # print(self.Lengv)
            # -------

            L = len(self.dictinary["authors"])
           # if L <= 3:
           #    st = self.dictinary["authors"][0] + " " + self.dictinary["short_initial"][0] + " "
           # else:
           #    st=''
           #st = st + self.dictinary["title"] + " / "
           #L2 = self.settings_count_autors
           # if L == self.settings_count_autors + 1:  # if count autorths max+1 then inclut them
           #     L2 = L
           #if L>4:
           #     L=3    
            M=min(self.settings_count_autors, L)
            arr = range(M)
            if M==L-1:
                M=self.settings_count_autors+1 #если количество авторов на 1 больше чем ограничение

            if L==1:
                st = st + self.dictinary["authors"][0] +','+ self.dictinary["short_initial"][0]
                                                #если количество авторов меньше, чем ограничение
            elif L<=self.settings_count_autors or M==self.settings_count_autors+1: 
                for i in arr:   
                    if i < M-1: 
                        st = st + self.dictinary["authors"][i] +','+ self.dictinary["short_initial"][i]+', '
                    elif i==M-1: #если количество авторов меньше, чем ограничение перед последним ставим AND
                         st = st + 'and ' + self.dictinary["authors"][i] +','+ self.dictinary["short_initial"][i]+', '
                                #если количество авторов больше? чем ограничение
                st = st[:len(st) - 2]  # delete last ", "

            elif L>self.settings_count_autors:
                for i in arr:   
                    if i < M-1: 
                        st = st + self.dictinary["authors"][i] +','+ self.dictinary["short_initial"][i]+', '
                    elif i==M-1:
                        st = st + self.dictinary["authors"][i] +','+ self.dictinary["short_initial"][i]+', '

                st = st[:len(st) - 2]  # delete last ", "
                if len(self.dictinary["authors"]) > self.settings_count_autors + 1:
                    if self.Lengv == self.type_lengv[1]:  # Engl
                        st = st + " et al. "
                    elif self.Lengv == self.type_lengv[0]:  # Ru
                        st = st + " и др. "
            
            st = st + '(' + self.dictinary["year"] + '),'
            st = st + '"' + self.dictinary["title"] + '", '
            
            st = st + self.dictinary["journal"] + ', '
           
            if self.Lengv == self.type_lengv[1]:  # Engl
                if len(self.dictinary["number"])>0:
                    st = st + self.dictinary["volume"] 
                    st = st + "(" + self.dictinary["number"] + "), "
                else:
                    st = st + self.dictinary["volume"] + ", "
                st = st + "pp. " + self.dictinary["pages"] + ". "
            elif self.Lengv == self.type_lengv[0]:  # Ru
                if len(self.dictinary["number"])>0:
                    st = st + self.dictinary["volume"] 
                    st = st + "(" + self.dictinary["number"] + "), "
                else:
                    st = st + self.dictinary["volume"] + ", "
                st = st + "cc. " + self.dictinary["pages"] + ". "

            st = st + "doi: https://doi.org/" + self.dictinary["doi"]
            self.Result = st
        return st
    def convert_to_GOST(self):
        st = ''
        if self.flag_availability_data == True:

            # ------  Lengvich
            stt = self.dictinary["authors"][0]
            stt = stt[0]
            # print('st=' + stt + '...')
            if re.match('[а-яА-Я]', stt):
                self.Lengv = self.type_lengv[0]  # "Ru"
            elif re.match('[A-Za-z]', stt):
                self.Lengv = self.type_lengv[1]  # Engl
           # print(self.Lengv)
            # -------

            L = len(self.dictinary["authors"])
            if L <= 3:
                st = self.dictinary["authors"][0] + " " + self.dictinary["short_initial"][0] + " "
            else:
                st=''
            st = st + self.dictinary["title"] + " / "
            L2 = self.settings_count_autors
            if L == self.settings_count_autors + 1:  # if count autorths max+1 then inclut them
                L2 = L
            if L>4:
                L=3 
            M= min(self.settings_count_autors, L2, L)  
            if L==self.settings_count_autors + 1:
                M=L
            
            arr = range(M)
            
            for i in arr:
                st = st + self.dictinary["short_initial"][i] + " " + self.dictinary["authors"][i] + ", "
            st = st[:len(st) - 2]  # delete last ", "
            
            if len(self.dictinary["authors"]) > self.settings_count_autors + 1:
                if self.Lengv == self.type_lengv[1]:  # Engl
                    st = st + " [et al.]"
                elif self.Lengv == self.type_lengv[0]:  # Ru
                    st = st + " [и др.] "

            st = st + " // "
            st = st + self.dictinary["journal"] + ". - "
            st = st + self.dictinary["year"] + ". - "
            if self.Lengv == self.type_lengv[1]:  # Engl
                if len(self.dictinary["number"])>0:
                    st = st + "Vol. " + self.dictinary["volume"] + ", "
                    st = st + "N. " + self.dictinary["number"] + ". - "
                else:
                    st = st + "Vol. " + self.dictinary["volume"] + ". - "
                st = st + "P. " + self.dictinary["pages"] + ". - "
            elif self.Lengv == self.type_lengv[0]:  # Ru
                if len(self.dictinary["number"])>0:
                    st = st + "Т. " + self.dictinary["volume"] + ", "
                    st = st + "№. " + self.dictinary["number"] + ". - "
                else:
                    st = st + "Т. " + self.dictinary["volume"] + ". - "
                st = st + "С. " + self.dictinary["pages"] + ". - "

            st = st + "DOI: " + self.dictinary["doi"]
            self.Result = st
        return st

    #######
    def get_data_by_doi(self, doi):
        bibtex = ''
        BASE_URL = 'http://dx.doi.org/'

        #doi = '10.3390/s18041190'
        self.flag_availability_data = False

        url = BASE_URL + doi
        req = urllib.request.Request(url)
        req.add_header('Accept', 'application/x-bibtex')
        try:
            with urllib.request.urlopen(req) as f:
                bibtex = f.read().decode()
                print(bibtex)
                self.parsing(bibtex)  # create dictinary by bibtex
                self.flag_availability_data = True
        except HTTPError as e:
            if e.code == 404:
                print('DOI not found.')
            else:
                print('Service unavailable.')
           # sys.exit(1)
            bibtex = 'error'
        return bibtex

    def parsing(self, bibtex):
        # вызывается по умолчанию get_data_by_doi(self, doi):
        """ find(str): поиск подстроки str ведется с начала строки до ее конца
            find(str, start): параметр start задает начальный индекс, с которого будет производиться поиск
            find(str, start, end): параметр end задает конечный индекс, до которого будет идти поиск """
        L = len(bibtex)

        st2_value = ""
        ind1 = bibtex.find("url = {")
        ind2 = bibtex.find("}", ind1)
        list_string = bibtex.split('\n\t')  # split -разделить . Формирование массива строк по разделителю
        L = len(list_string)
        if L<2:
            list_string = bibtex.split('\n')
        L = len(list_string)    
        # for i in range(L):
        for st0 in list_string:
            st2_value = ""
            ind1 = st0.find(' = {')
            st1_name = st0[:ind1]  # name of tag
            st1_name=st1_name.strip() # удаление крайних пробелов
            ind2 = st0.find('},')
            if ind2 > 0:
                
                st2_value = st0[ind1 + 4:ind2]  # value of tag
            else:
                ind_3 = st0.find('@')
                if ind_3 >= 0:
                    ind_4 = st0.find('{')
                    st2_value = st0[ind_3 + 1:ind_4]
                    st1_name = "type_print"
                else:
                    ind1 = st0.find(' = ')  # 'year = 2018,'
                    st1_name = st0[:ind1]
                    ind2 = st0.find(',')
                    if ind2 > 0:
                        st2_value = st0[len(st1_name) + 3:ind2]  # value of tag #  'year
                    else:
                        ind2 = st0.find('}\n')
                        if ind2 > 0:
                            st2_value = st0[len(st1_name) + 4:ind2]

            if st1_name == "author":
                self.Authors_Parsing(st2_value) # self.deleted_spetial_simbol віполняется автоматом
            else:
                if st1_name == "journal" or st1_name == "title":
                   st2_value = self.deleted_spetial_simbol(st2_value)
                self.dictinary[st1_name] = st2_value
        # self.dictinary["url"]=bibtex[ind1:ind2]

    def Authors_Parsing(self, st2_value):
        # "author = {Francisco Pizarro and Piero Villavicencio and Daniel Yunge and Mauricio Rodr{\\'{\\i}}guez and Gabriel Hermosilla and Ariel Leiva},"

        list_string = st2_value.split(' and ')

        ind_othet_format=list_string[0].find(',')
        flag_othet_format=False
        if ind_othet_format>0:
            flag_othet_format=True  # Potter, Adam W and Looney, David P and Hancock, Jason W. and Sanford
        
        L = len(list_string)
        # arr = range(L)
        # count = 0
        n = range(L - 1)
        i=0

        for a in list_string:  # numbers authors
            if flag_othet_format==False:
                        # if i%2==0: # i mod 2 -четное (начинается счет с 0) это Имя, нечетное - Фамилия
                st0 = list_string[i]
                # st0 = LatexNodes2Text().latex_to_text(st0)
                st2 = st0.split(' ')  # separete name and familia   "Francisco Pizarro"
                L2 = len(st2)
                # dictinary["authors"].append - add to list value

                st_familia=st2[L2 - 1]
                st_familia= self.deleted_spetial_simbol(st_familia)
                self.dictinary["authors"].insert(i, st_familia)  # Last Name - familia

                st_temp1 = ""
                st_temp2 = ""
                n2 = range(L2 - 1)
                for j in n2:
                    st_temp1 = st_temp1 + st2[j] + " "  # for "full_initial"
                    if st2[j]!='van' and st2[j]!='de':
                        st_temp2 = st_temp2 + st2[j][0] + "." + " "  # for "short_initial"
                    


                st_temp1 = st_temp1.strip()  # удаляем крайние пробелы
                st_temp2 = st_temp2.strip()
                self.dictinary["full_initial"].insert(i, st_temp1)
                self.dictinary["short_initial"].insert(i, st_temp2)
                i+=1
            if flag_othet_format==True:
                        # if i%2==0: # i mod 2 -четное (начинается счет с 0) это Имя, нечетное - Фамилия
                st0 = list_string[i]
                # st0 = LatexNodes2Text().latex_to_text(st0)
                st2 = st0.split(' ')  # separete name and familia   "Francisco Pizarro"
                L2 = len(st2)
                # dictinary["authors"].append - add to list value

                st_familia=st2[0]
                st_familia=st_familia[0:ind_othet_format]
                st_familia= self.deleted_spetial_simbol(st_familia)
                self.dictinary["authors"].insert(i, st_familia)  # Last Name - familia

                st_temp1 = ""
                st_temp2 = ""
                n2 = range(1, L2, 1)
                for j in n2:
                    st_temp1 = st_temp1 + st2[j] + " "  # for "full_initial"
                    if st2[j]!='van' and st2[j]!='de':
                        st_temp2 = st_temp2 + st2[j][0] + "." + " "  # for "short_initial"
                    


                st_temp1 = st_temp1.strip()  # удаляем крайние пробелы
                st_temp2 = st_temp2.strip()
                self.dictinary["full_initial"].insert(i, st_temp1)
                self.dictinary["short_initial"].insert(i, st_temp2)
                i+=1    

    def deleted_spetial_simbol(self, st):

        type_del_list = (
                        "{\textendash}",
                        "{\\&}amp$\\mathsemicolon$",
                        "{\\s",
                        "{\\v{s}}",
                        "{\\'{c}" ,
                        '{',
                        '}'
                        )    
        new_replase_list=(
                          '-',
                          '&',
                          '',
                          's',
                          'c',
                          '',
                          ''
                          )
        c=0                  
        for old_st in type_del_list:
            ind=st.find(old_st)
            if ind>=0:
                st=st.replace(old_st, new_replase_list[c])
            c+=1
        return st

class working_with_file:
    type_file_extation_list = ('.txt', ' ', '.xls', '.xlsx', '.csv', '.doc', '.docx')

    def __init__(self):
        # исходный файл ссылок
        self.init_file_path = ""
        self.init_file_name = ""
        self.init_file_type = self.type_file_extation_list[0]
        self.init_full_neme = self.init_file_path + self.init_file_name


        # файл результатов
        self.result_file_path = ""
        self.result_file_name = ""
        self.result_file_type = self.type_file_extation_list[0]
        self.init_full_neme = self.result_file_path + self.result_file_name

        self.separete_symbol_1 = ". "  #
        self.separete_symbol_2 = ".\t"  #
        self.separete_symbol_3 = "."  #
        self.st_list_DOI = ''
        self.result_list = ''

    def set_file_name(self, init_file):
        if init_file != '':  # если входной параметр init_file не равен пустой строке, то переменным класса присвоить его значение
            self.init_file_name = os.path.basename(init_file)  # name file
            self.init_file_path = os.path.dirname(init_file)
            self.init_file_type = os.path.splitext(self.init_file_name)[1]
            # curr_dirr=os.getcwd()
            self.init_full_neme = init_file

    def read_file_create_list_doi(self, init_file):  # читает файл и формирует result_list
        if init_file != '':  # если входной параметр init_file не равен пустой строке, то переменным класса присвоить его значение
            self.set_file_name(init_file)

        f = open(self.init_full_neme, 'r')
        c = 0
        st_list_DOI = []
        for line in f:
            ind = line.find(self.separete_symbol_1)  # надо удалять только первую точку. Проверит!!!!!!!!!
            if ind < 0:
                ind = line.find(self.separete_symbol_2)
                if ind < 0:
                    ind = line.find(self.separete_symbol_3)

            st = line[ind + 2:len(line)]  # delete number with '.'
            st = st.strip()  # удаляем крайние пробелы
            st_list_DOI.append(st)
        #     st2 = ''
        #     if st != '':
        #         CR = Reference_Convert()
        #         bibtex = CR.get_data_by_doi(st)
        #         st2 = CR.convert()
        #     st_res.append(st2)
        #     c += 1
        #
        # self.result_list = st_res
        self.st_list_DOI = st_list_DOI
        f.close()

    def init_read_file(self, init_file):  # читает файл и формирует result_list
        if init_file != '':  # если входной параметр init_file не равен пустой строке, то переменным класса присвоить его значение
            self.set_file_name(init_file)

        f = open(self.init_full_neme, 'r')
        c = 0
        st_res = ''
        for line in f:
            ind = line.find(self.separete_symbol)  # надо удаляь только первую точку. Проверит!!!!!!!!!
            st = line[ind + 2:len(line)]  # delete number with '.'
            st = st.strip()  # удаляем крайние пробелы
            st2 = ''
            if st != '':
                CR = Reference_Convert()
                bibtex = CR.get_data_by_doi(st)
                st2 = CR.convert()
            st_res.append(st2)
            c += 1

        self.result_list = st_res

        f.close()

    def result_write_file(self, result_file):  # save file

        if result_file != '':  # если входной параметр result_file не равен пустой строке, то переменным класса присвоить его значение
            self.result_file_name = os.path.basename(result_file)  # name file
            self.result_file_path = os.path.dirname(result_file)
            self.result_file_type = os.path.splitext(self.result_file_name)[1]
            # curr_dirr=os.getcwd()
            self.result_full_neme = result_file

        f = open(self.result_full_neme, 'w')
        # c=len(self.result_list)
        c = 1
        for st in self.result_list:
            st2 = str(str(c) + '. ' + st)
            print('len=' + str(len(st2)))
            try:
                f.write(st2 + '\n')
            except:
                f.write(str(c) + '. ' + '\n')   
                print(st2) 
            print(c)
            
            if c==80:
                print(st)

            c += 1
        f.close()
