import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import datetime as dt
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from main_window import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QMessageBox, QDialog, QTableWidgetItem, \
    QTableWidget
import numpy as np
import tensorflow as tf
import  pandas as pd
from random import *
from prediction import Ui_Dialog
from views import predict
global folder_path,resuls,all_result
from PyQt5.QtGui import QGuiApplication

folder_path = []
resuls = []
all_result=[]


class QmyWidget(QWidget,Ui_Form):

    def __init__(self):
        super(QmyWidget,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.example.clicked.connect(self.push_button_click)
        self.ui.selectfile.clicked.connect(self.select_file)

        self.ui.reset.clicked.connect(self.resets)
        self.ui.submit.clicked.connect(self.submit)
        self.ui.filesite.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ui.mainOptionsGroupBox.setStyleSheet("QGroupBox {border: 8px solid transparent;}")
        self.ui.scrollArea.setStyleSheet("QScrollArea {border: 0px solid transparent;}")
        self.show()
    def resets(self):
        global folder_path
        folder_path=[]
        self.ui.fastatext.clear()
        self.ui.filesite.clear()
        QMessageBox.information(self, "successful",
                             "Clear successfully!")

    def push_button_click(self):
        self.ui.fastatext.setPlainText('>tr|A0A0N7A486|\nSHSMRYFFTSVSRPGRGEPRFIAVGYVDDTQFVRFDSDAASQRMEPRAPWIEQEGPEYWD\nGETRKVKAHSQIDRVDLGTLRGYYNQSEAGSHTVQRMYGCDVGSDWRFLRGYHQYAYDGK\nDYIALKEDLRSWTAADMAAQTTKHKWEAAHVAEQLRAYLEGTCVEWLRRYLENGKETLQR')


    def select_file(self):
        self.ui.fastatext.clear()
        global folder_path
        folder_path = QFileDialog.getOpenFileName(self, "select a file","C:",("文本文件(*txt *fasta)"))[0]
        self.ui.filesite.setText(str(folder_path))
        f=open(folder_path,encoding='utf-8')
        self.ui.fastatext.setPlainText(f.read())

    def submit(self):
        global folder_path, results, all_result

        if self.ui.pLys.isChecked() == True:
            if self.ui.fastatext.toPlainText() == '':
                # print(self.ui.fastatext.toPlainText())
                QMessageBox.critical(self, "error", "Please input the peptide sequence or select a fasta file")
            elif self.ui.fastatext.toPlainText().count('>')>300:
                QMessageBox.critical(self, "error", "The number of input sequences at one time cannot exceed 100!")
                self.ui.fastatext.clear()
                self.ui.filesite.clear()
            else:
                results, all_result = predict(folder_path, self.ui.fastatext.toPlainText(), 'K')
                if results == 0 or results == 20 or results == 10 or results == 30:
                    QMessageBox.critical(self, "error",
                                         "Please check the correctness of the file or text format you uploaded")

                else:
                    self.w = predict_window()
                    # self.w.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                    self.w.ui.results.setEditTriggers(QTableWidget.NoEditTriggers)
                    self.w.ui.results.horizontalHeader().setStyleSheet("QHeaderView::section{ background-color : #EAEAEA }")
                    self.w.ui.results.setRowCount(len(results))
                    self.w.ui.results.setColumnCount(5)
                    # horizontalHeader = ["Protein", "Position", "Sequence", "Prediction score", "Prediction category"]
                    # self.w.ui.tableWidget.setHorizontalHeaderLabels(horizontalHeader)
                    # self.w.ui.tableWidget.resizeColumnsToContents()
                    # self.w.ui.tableWidget.resizeRowsToContents()
                    # self.w.ui.tableWidget.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.w.ui.results.verticalHeader().setVisible(False)

                    # self.w.ui.results.horizontalHeader().setSectionResizeMode(QHeaderView.)

                    self.w.ui.results.horizontalHeader().resizeSection(0, 120)
                    self.w.ui.results.horizontalHeader().resizeSection(1, 92)
                    self.w.ui.results.horizontalHeader().resizeSection(2, 360)
                    self.w.ui.results.horizontalHeader().resizeSection(3, 100)
                    self.w.ui.results.horizontalHeader().resizeSection(4, 160)

                    for i in range(len(results)):
                        tm1 = QTableWidgetItem(results[i]['protein'])
                        tm2 = QTableWidgetItem(results[i]['position'])
                        tm3 = QTableWidgetItem(results[i]['sequence_l'] + "k"+ results[i]['sequence_r'])
                        tm3.setFont(QFont('Courier New', 11))
                        tm4 = QTableWidgetItem(str(format(results[i]['score'], '.4f')))
                        tm5 = QTableWidgetItem(results[i]['prediction'])
                        if results[i]['prediction'] == 'Very High confidence':
                            tm5.setForeground(QBrush(QColor("red")))
                        elif results[i]['prediction'] == 'High confidence':
                            tm5.setForeground(QBrush(QColor("brown")))
                        elif results[i]['prediction'] == 'Medium confidence':
                            tm5.setForeground(QBrush(QColor("green")))
                        self.w.ui.results.setItem(i, 0, tm1)
                        self.w.ui.results.setItem(i, 1, tm2)
                        self.w.ui.results.setItem(i, 2, tm3)
                        self.w.ui.results.setItem(i, 3, tm4)
                        self.w.ui.results.setItem(i, 4, tm5)
                        tm1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                        tm2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                        tm3.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                        tm4.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                        tm5.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

                    self.w.ui.Legend.setEditTriggers(QTableWidget.NoEditTriggers)
                    self.w.ui.Legend.setRowCount(4)
                    self.w.ui.Legend.setColumnCount(2)
                    horizontalHeader = ["Label", "Score Range", ]
                    self.w.ui.Legend.horizontalHeader().setStyleSheet(
                        "QHeaderView::section{ background-color : #EAEAEA }")
                    self.w.ui.Legend.setHorizontalHeaderLabels(horizontalHeader)
                    self.w.ui.Legend.verticalHeader().setVisible(False)
                    self.w.ui.Legend.horizontalHeader().resizeSection(0, 154)
                    self.w.ui.Legend.horizontalHeader().resizeSection(1, 101)
                    self.w.ui.Legend.setShowGrid(False)
                    ff = ['Very High confidence', 'High confidence', 'Medium confidence', 'No']
                    cc = ['red', 'brown', 'green', 'black']
                    nn = ['(0.85-1]', '(0.7-0.85]', '(0.5-0.7]', '[0,0.5]']
                    for i in range(4):
                        tm1 = QTableWidgetItem(ff[i])
                        # tm1 = QTableWidgetItem.
                        tm1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

                        tm1.setForeground(QBrush(QColor(cc[i])))
                        tm2 = QTableWidgetItem(nn[i])
                        tm2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                        self.w.ui.Legend.setItem(i, 0, tm1)
                        self.w.ui.Legend.setItem(i, 1, tm2)

                    self.w.show()
        elif self.ui.pHis.isChecked() == True:
            if self.ui.fastatext.toPlainText() == '':
                # print(self.ui.fastatext.toPlainText())
                QMessageBox.critical(self, "error", "Please input the peptide sequence or select a fasta file")
            elif self.ui.fastatext.toPlainText().count('>') > 200:
                QMessageBox.critical(self, "error", "The number of input sequences at one time cannot exceed 100!")
                self.ui.fastatext.clear()
                self.ui.filesite.clear()
            else:
                results, all_result = predict(folder_path, self.ui.fastatext.toPlainText(), 'H')
                print(results)
                if results == 0 or results == 20 or results == 10 or results == 30:
                    QMessageBox.critical(self, "error",
                                         "Please check the correctness of the file or text format you uploaded")
                else:
                    print(0)
                    self.w = predict_window()
                    # self.w.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                    self.w.ui.results.setEditTriggers(QTableWidget.NoEditTriggers)
                    self.w.ui.results.setRowCount(len(results))
                    self.w.ui.results.setColumnCount(5)

                    self.w.ui.results.verticalHeader().setVisible(False)
                    self.w.ui.results.horizontalHeader().setStyleSheet(
                        "QHeaderView::section{ background-color : #EAEAEA }")

                    # self.w.ui.results.horizontalHeader().setSectionResizeMode(QHeaderView.)

                    self.w.ui.results.horizontalHeader().resizeSection(0, 120)
                    self.w.ui.results.horizontalHeader().resizeSection(1, 92)
                    self.w.ui.results.horizontalHeader().resizeSection(2, 360)
                    self.w.ui.results.horizontalHeader().resizeSection(3, 100)
                    self.w.ui.results.horizontalHeader().resizeSection(4, 160)

                    for i in range(len(results)):
                        tm1 = QTableWidgetItem(results[i]['protein'])
                        tm2 = QTableWidgetItem(results[i]['position'])
                        tm3 = QTableWidgetItem(results[i]['sequence_l'] + "h" + results[i]['sequence_r'])
                        tm3.setFont(QFont('Courier New', 11))
                        tm4 = QTableWidgetItem(str(format(results[i]['score'], '.4f')))
                        tm5 = QTableWidgetItem(results[i]['prediction'])
                        if results[i]['prediction'] == 'Very High confidence':
                            tm5.setForeground(QBrush(QColor("red")))
                        elif results[i]['prediction'] == 'High confidence':
                            tm5.setForeground(QBrush(QColor("brown")))
                        elif results[i]['prediction'] == 'Medium confidence':
                            tm5.setForeground(QBrush(QColor("green")))
                        # else:
                        #    pass
                        self.w.ui.results.setItem(i, 0, tm1)
                        self.w.ui.results.setItem(i, 1, tm2)
                        self.w.ui.results.setItem(i, 2, tm3)
                        self.w.ui.results.setItem(i, 3, tm4)
                        self.w.ui.results.setItem(i, 4, tm5)
                        tm1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                        tm2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                        tm3.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                        tm4.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                        tm5.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

                    self.w.ui.Legend.setEditTriggers(QTableWidget.NoEditTriggers)
                    self.w.ui.Legend.setRowCount(4)
                    self.w.ui.Legend.setColumnCount(2)
                    horizontalHeader = ["Label", "Score Range", ]
                    self.w.ui.Legend.horizontalHeader().setStyleSheet(
                        "QHeaderView::section{ background-color : #EAEAEA }")
                    self.w.ui.Legend.setHorizontalHeaderLabels(horizontalHeader)
                    self.w.ui.Legend.verticalHeader().setVisible(False)
                    self.w.ui.Legend.horizontalHeader().resizeSection(0, 154)
                    self.w.ui.Legend.horizontalHeader().resizeSection(1, 101)
                    self.w.ui.Legend.setShowGrid(False)
                    ff = ['Very High confidence', 'High confidence', 'Medium confidence', 'No']
                    cc = ['red', 'brown', 'green', 'black']
                    nn = ['(0.85-1]', '(0.7-0.85]', '(0.5-0.7]', '[0,0.5]']
                    for i in range(4):
                        tm1 = QTableWidgetItem(ff[i])
                        # tm1 = QTableWidgetItem.
                        tm1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

                        tm1.setForeground(QBrush(QColor(cc[i])))
                        tm2 = QTableWidgetItem(nn[i])
                        tm2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                        self.w.ui.Legend.setItem(i, 0, tm1)
                        self.w.ui.Legend.setItem(i, 1, tm2)

                    self.w.show()
        else:
            if self.ui.fastatext.toPlainText() == '':
                # print(self.ui.fastatext.toPlainText())
                QMessageBox.critical(self, "error", "Please input the peptide sequence or select a fasta file")
            elif self.ui.fastatext.toPlainText().count('>') > 500:
                QMessageBox.critical(self, "error", "The number of input sequences at one time cannot exceed 100!")
                self.ui.fastatext.clear()
                self.ui.filesite.clear()
            else:
                results, all_result = predict(folder_path, self.ui.fastatext.toPlainText(), 'R')
                if results == 0 or results == 20 or results == 10 or results == 30:
                    QMessageBox.critical(self, "error",
                                         "Please check the correctness of the file or text format you uploaded")
                else:
                    self.w = predict_window()
                    # self.w.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                    self.w.ui.results.setEditTriggers(QTableWidget.NoEditTriggers)
                    self.w.ui.results.setRowCount(len(results))
                    self.w.ui.results.setColumnCount(5)
                    self.w.ui.results.verticalHeader().setVisible(False)
                    self.w.ui.results.horizontalHeader().setStyleSheet(
                        "QHeaderView::section{ background-color : #EAEAEA }")
                    self.w.ui.results.horizontalHeader().resizeSection(0, 120)
                    self.w.ui.results.horizontalHeader().resizeSection(1, 92)
                    self.w.ui.results.horizontalHeader().resizeSection(2, 360)
                    self.w.ui.results.horizontalHeader().resizeSection(3, 100)
                    self.w.ui.results.horizontalHeader().resizeSection(4, 160)
                    for i in range(len(results)):
                        tm1 = QTableWidgetItem(results[i]['protein'])
                        tm2 = QTableWidgetItem(results[i]['position'])
                        tm3 = QTableWidgetItem(results[i]['sequence_l'] + "r" + results[i]['sequence_r'])
                        tm3.setFont(QFont('Courier New', 11))
                        tm4 = QTableWidgetItem(str(format(results[i]['score'], '.4f')))
                        tm5 = QTableWidgetItem(results[i]['prediction'])
                        if results[i]['prediction'] == 'Very High confidence':
                            tm5.setForeground(QBrush(QColor("red")))
                        elif results[i]['prediction'] == 'High confidence':
                            tm5.setForeground(QBrush(QColor("brown")))
                        elif results[i]['prediction'] == 'Medium confidence':
                            tm5.setForeground(QBrush(QColor("green")))
                        # else:
                        #    pass
                        self.w.ui.results.setItem(i, 0, tm1)
                        self.w.ui.results.setItem(i, 1, tm2)
                        self.w.ui.results.setItem(i, 2, tm3)
                        self.w.ui.results.setItem(i, 3, tm4)
                        self.w.ui.results.setItem(i, 4, tm5)
                        tm1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                        tm2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                        tm3.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                        tm4.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                        tm5.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

                    self.w.ui.Legend.setEditTriggers(QTableWidget.NoEditTriggers)
                    self.w.ui.Legend.setRowCount(4)
                    self.w.ui.Legend.horizontalHeader().setStyleSheet(
                        "QHeaderView::section{ background-color : #EAEAEA }")
                    self.w.ui.Legend.setColumnCount(2)
                    horizontalHeader = ["Label", "Score Range"]
                    self.w.ui.Legend.setHorizontalHeaderLabels(horizontalHeader)
                    self.w.ui.Legend.verticalHeader().setVisible(False)
                    self.w.ui.Legend.horizontalHeader().resizeSection(0, 154)
                    self.w.ui.Legend.horizontalHeader().resizeSection(1, 101)
                    self.w.ui.Legend.setShowGrid(False)
                    ff = ['Very High confidence', 'High confidence', 'Medium confidence', 'No']
                    cc = ['red', 'brown', 'green', 'black']
                    nn = ['(0.85-1]', '(0.7-0.85]', '(0.5-0.7]', '[0,0.5]']
                    for i in range(4):

                        tm1 = QTableWidgetItem(ff[i])

                        tm1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

                        tm1.setForeground(QBrush(QColor(cc[i])))
                        tm2 = QTableWidgetItem(nn[i])
                        tm2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                        self.w.ui.Legend.setItem(i, 0, tm1)
                        self.w.ui.Legend.setItem(i, 1, tm2)

                    self.w.show()



class predict_window(QDialog,Ui_Dialog):
    def __init__(self):
        super(predict_window,self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.saved.clicked.connect(self.saves)

    def saves(self):
        directory1 = QFileDialog.getExistingDirectory(self,"Select the file address you want to save ", "C:/")
        now_time = dt.datetime.now().strftime('%g' + '%m' + "%d"+'%H'+'%M'+'%S')
        save_file = []
        for i in range(len(all_result)):
            c = []
            c.append(all_result[i]['protein'])
            c.append(all_result[i]['position'])
            c.append(all_result[i]['sequence_l'] + all_result[i]['sequence_19'] + all_result[i]['sequence_r'])
            c.append(str(all_result[i]['score']))
            c.append(all_result[i]['prediction'])
            save_file.append(c)
        save_file = pd.DataFrame(save_file)
        save_file.columns = ['protein', 'position', 'sequence', 'score', 'prediction']
        c = randint(100, 999)
        save_file.to_csv(directory1+'/'+now_time+str(c)+'.csv', index=False)
        QMessageBox.information(self, "save", "Successfully saved")




if  __name__=='__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app=QtWidgets.QApplication(sys.argv) #创建app，用QApplication类
    baseWidge=QtWidgets.QWidget() #创建窗体的基类Qwidget的实例

    ui=QmyWidget()
    ui.setupUi(baseWidge) #以baseWidget作为传递参数，创建完整窗体

    #baseWidge.show()
    #ui. LabHello.setText("Hello，被程序修改") 可以修改窗体上标签的文字
    sys.exit(app.exec())