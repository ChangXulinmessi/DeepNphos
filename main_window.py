# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(865, 706)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(500, 0))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 841, 682))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_35 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_35.setObjectName("gridLayout_35")
        self.configurationTabWidget = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.configurationTabWidget.sizePolicy().hasHeightForWidth())
        self.configurationTabWidget.setSizePolicy(sizePolicy)
        self.configurationTabWidget.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.configurationTabWidget.setFont(font)
        self.configurationTabWidget.setMovable(True)
        self.configurationTabWidget.setObjectName("configurationTabWidget")
        self.optimizerTab = QtWidgets.QWidget()
        self.optimizerTab.setObjectName("optimizerTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.optimizerTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.optimizerTab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.configurationTabWidget.addTab(self.optimizerTab, "")
        self.mainTab = QtWidgets.QWidget()
        self.mainTab.setObjectName("mainTab")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.mainTab)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.mainOptionsGroupBox = QtWidgets.QGroupBox(self.mainTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainOptionsGroupBox.sizePolicy().hasHeightForWidth())
        self.mainOptionsGroupBox.setSizePolicy(sizePolicy)
        self.mainOptionsGroupBox.setTitle("")
        self.mainOptionsGroupBox.setObjectName("mainOptionsGroupBox")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.mainOptionsGroupBox)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.credentialsGroupBox = QtWidgets.QGroupBox(self.mainOptionsGroupBox)
        self.credentialsGroupBox.setObjectName("credentialsGroupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.credentialsGroupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.selectfile = QtWidgets.QPushButton(self.credentialsGroupBox)
        self.selectfile.setAutoDefault(False)
        self.selectfile.setObjectName("selectfile")
        self.horizontalLayout.addWidget(self.selectfile)
        self.filesite = QtWidgets.QLineEdit(self.credentialsGroupBox)
        self.filesite.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.filesite.setObjectName("filesite")
        self.horizontalLayout.addWidget(self.filesite)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_13.addWidget(self.credentialsGroupBox, 6, 0, 1, 3)
        self.tickerLabel = QtWidgets.QLabel(self.mainOptionsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tickerLabel.sizePolicy().hasHeightForWidth())
        self.tickerLabel.setSizePolicy(sizePolicy)
        self.tickerLabel.setObjectName("tickerLabel")
        self.gridLayout_13.addWidget(self.tickerLabel, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem1, 0, 2, 1, 1)
        self.accountTypeGroupBox = QtWidgets.QGroupBox(self.mainOptionsGroupBox)
        self.accountTypeGroupBox.setObjectName("accountTypeGroupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.accountTypeGroupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pHis = QtWidgets.QRadioButton(self.accountTypeGroupBox)
        self.pHis.setObjectName("pHis")
        self.horizontalLayout_2.addWidget(self.pHis)
        self.pLys = QtWidgets.QRadioButton(self.accountTypeGroupBox)
        self.pLys.setChecked(True)
        self.pLys.setObjectName("pLys")
        self.horizontalLayout_2.addWidget(self.pLys)
        self.pArg = QtWidgets.QRadioButton(self.accountTypeGroupBox)
        self.pArg.setChecked(False)
        self.pArg.setObjectName("pArg")
        self.horizontalLayout_2.addWidget(self.pArg)
        self.gridLayout_13.addWidget(self.accountTypeGroupBox, 7, 0, 1, 1)
        self.example = QtWidgets.QPushButton(self.mainOptionsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.example.sizePolicy().hasHeightForWidth())
        self.example.setSizePolicy(sizePolicy)
        self.example.setAutoDefault(False)
        self.example.setObjectName("example")
        self.gridLayout_13.addWidget(self.example, 0, 1, 1, 1)
        self.fastatext = QtWidgets.QTextEdit(self.mainOptionsGroupBox)
        self.fastatext.setObjectName("fastatext")
        self.gridLayout_13.addWidget(self.fastatext, 3, 0, 1, 3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.submit = QtWidgets.QPushButton(self.mainOptionsGroupBox)
        self.submit.setObjectName("submit")
        self.horizontalLayout_3.addWidget(self.submit)
        self.reset = QtWidgets.QPushButton(self.mainOptionsGroupBox)
        self.reset.setAutoDefault(False)
        self.reset.setObjectName("reset")
        self.horizontalLayout_3.addWidget(self.reset)
        self.gridLayout_13.addLayout(self.horizontalLayout_3, 9, 0, 2, 1)
        self.gridLayout_14.addWidget(self.mainOptionsGroupBox, 0, 0, 1, 1)
        self.configurationTabWidget.addTab(self.mainTab, "")
        self.simulationWidget = QtWidgets.QWidget()
        self.simulationWidget.setObjectName("simulationWidget")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.simulationWidget)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.simulationWidget)
        self.textBrowser_3.setStyleSheet("background-color: rgb(249, 249, 249);")
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout_29.addWidget(self.textBrowser_3, 0, 0, 1, 1)
        self.configurationTabWidget.addTab(self.simulationWidget, "")
        self.gridLayout_35.addWidget(self.configurationTabWidget, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.configurationTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "DeepNphos"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:600; color:#000000;\">Welcome to the DeepNphos</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:14pt;\">Phosphorylation, a common post-translational modification, is essential</span><span style=\" font-family:\'宋体\'; font-size:14pt;\"> </span><span style=\" font-family:\'Times New Roman\'; font-size:14pt;\">in regulating cellular activities. It includes O-phosphorylation (</span><span style=\" font-family:\'Times New Roman\'; font-size:14pt; font-style:italic;\">e.g.</span><span style=\" font-family:\'Times New Roman\'; font-size:14pt;\">, phosphoserine) and N-phosphorylation (</span><span style=\" font-family:\'Times New Roman\'; font-size:14pt; font-style:italic;\">e.g</span><span style=\" font-family:\'Times New Roman\'; font-size:14pt;\">., phospho-histidine (pH), phospho-lysine (pK) and phospho-arginine(pR)). Much research has been done on O-phosphorylation, but little has been done on N-phosphorylation. Various algorithms have been developed for predicting O-phosphorylation sites with good performance. However, no</span><span style=\" font-family:\'宋体\'; font-size:14pt;\"> </span><span style=\" font-family:\'Times New Roman\'; font-size:14pt;\">model has</span><span style=\" font-family:\'宋体\'; font-size:14pt;\"> </span><span style=\" font-family:\'Times New Roman\'; font-size:14pt;\">been constructed to predict the N-phosphorylation sites. In this study, we developed the integrated model, dubbed DeepNphos, to predict N-phosphorylation sites based on thousands of experimentally identified pH, pK</span><span style=\" font-family:\'宋体\'; font-size:14pt;\"> </span><span style=\" font-family:\'Times New Roman\'; font-size:14pt;\">and pR</span><span style=\" font-family:\'宋体\'; font-size:14pt;\"> </span><span style=\" font-family:\'Times New Roman\'; font-size:14pt;\">sites, respectively. We found that pK was somewhat similar to other lysine modification types. Such similarity could improve the pK prediction performance by integrating the deep-transfer learning strategy into the residual convolutional</span><span style=\" font-family:\'宋体\'; font-size:14pt;\"> </span><span style=\" font-family:\'Times New Roman\'; font-size:14pt;\">neural network model. By contrast, pR had little similarity to other arginine modification types, and the deep-transfer learning strategy integration did not affect the pR prediction performance. Since histidine modifications other than pH are limited, we developed the classifier for predicting pH sites directly using the known pH sites. All three classifiers have the Area Under the Curve values around 0.8 for cross-validation and independent test. Overall, DeepNphos</span><span style=\" font-family:\'宋体\'; font-size:14pt;\"> </span><span style=\" font-family:\'Times New Roman\'; font-size:14pt;\">is the first classifier for predicting N-phosphorylation sites, </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Contact For using DeepNphos</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Please cite:</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Xulin Chang et al.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:14pt;\">DeepNphos: A Deep-Learning Architecture for Prediction of N-phosphorylation Sites</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Contact:</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">*Xulin Chang</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma\'; font-size:11pt; font-weight:600;\">Address</span><span style=\" font-family:\'Tahoma\'; font-size:11pt;\">: School of Computer Science And Technology</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma\'; font-size:11pt;\">          Qingdao University</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma\'; font-size:11pt;\">      Qingdao, China</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma\'; font-size:11pt; font-weight:600;\">E-mail</span><span style=\" font-family:\'Tahoma\'; font-size:11pt;\">: 2021023949@qdu.edu.cn,  lileime@hotmail.com</span></p></body></html>"))
        self.configurationTabWidget.setTabText(self.configurationTabWidget.indexOf(self.optimizerTab), _translate("Form", "Home"))
        self.credentialsGroupBox.setTitle(_translate("Form", "Or upload a file"))
        self.selectfile.setToolTip(_translate("Form", "Load Binance and Telegram credentials. Program will try to load credentials automatically from default.json."))
        self.selectfile.setText(_translate("Form", "Select File"))
        self.tickerLabel.setText(_translate("Form", "Input your protein sequences with the FASTA format."))
        self.accountTypeGroupBox.setTitle(_translate("Form", "Prediction Type"))
        self.pHis.setText(_translate("Form", "pH"))
        self.pLys.setToolTip(_translate("Form", "Select this if the asset you are trading is isolated."))
        self.pLys.setText(_translate("Form", "pK"))
        self.pArg.setToolTip(_translate("Form", "Select this if the asset you are trading is not isolated."))
        self.pArg.setText(_translate("Form", "pR"))
        self.example.setToolTip(_translate("Form", "Saves Binance and Telegram credentials. By default, they will save to default.json."))
        self.example.setText(_translate("Form", "Example"))
        self.submit.setText(_translate("Form", "Submit"))
        self.reset.setToolTip(_translate("Form", "Test Binance API credentials."))
        self.reset.setText(_translate("Form", "Reset"))
        self.configurationTabWidget.setTabText(self.configurationTabWidget.indexOf(self.mainTab), _translate("Form", "Prediction"))
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Arial\'; font-size:26pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:26pt; font-weight:600;\">Help for Using DeepNphos</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Arial\'; font-size:26pt; font-weight:600;\"><br /></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Tahoma\'; font-size:48pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">The input accepted characters contain 20 amino acids and the dummy code X.   </span></li>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px; font-family:\'Arial\'; font-size:12pt;\"><br /></p>\n"
"<li style=\" font-family:\'Arial\'; font-size:12pt; color:#333333;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The prediction output consists of five columns:</li></ul>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Arial\'; font-size:12pt; color:#333333;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:12pt; color:#333333;\">1) Protein</span><span style=\" font-family:\'Arial\'; font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:12pt; color:#333333;\">2) Position</span><span style=\" font-family:\'Arial\'; font-size:12pt;\">  </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:12pt; color:#333333;\">3) Sequence</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:12pt; color:#333333;\">4) Prediction Score</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:12pt; color:#333333;\">5) Prediction Category</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px; font-family:\'Arial\'; font-size:12pt; color:#333333;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px; font-family:\'Arial\'; font-size:12pt; color:#333333;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px; font-family:\'Arial\'; font-size:12pt; color:#333333;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px; font-family:\'Arial\'; font-size:12pt; color:#333333;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>"))
        self.configurationTabWidget.setTabText(self.configurationTabWidget.indexOf(self.simulationWidget), _translate("Form", "Help"))
