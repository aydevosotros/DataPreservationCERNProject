# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataPreservationGUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1043, 693)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 381, 441))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.tabWidget = QtGui.QTabWidget(self.groupBox)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 351, 401))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget_2 = QtGui.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 0, 331, 361))
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.layoutWidget_2 = QtGui.QWidget(self.tab_3)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 10, 311, 77))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(self.layoutWidget_2)
        self.label_5.setMinimumSize(QtCore.QSize(55, 0))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.texShortTb = QtGui.QTextEdit(self.layoutWidget_2)
        self.texShortTb.setObjectName(_fromUtf8("texShortTb"))
        self.horizontalLayout_5.addWidget(self.texShortTb)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.searchSingleShortButton = QtGui.QPushButton(self.layoutWidget_2)
        self.searchSingleShortButton.setObjectName(_fromUtf8("searchSingleShortButton"))
        self.verticalLayout_3.addWidget(self.searchSingleShortButton)
        self.parseSingleShortButton = QtGui.QPushButton(self.layoutWidget_2)
        self.parseSingleShortButton.setObjectName(_fromUtf8("parseSingleShortButton"))
        self.verticalLayout_3.addWidget(self.parseSingleShortButton)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.groupBox_2 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 90, 311, 231))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.layoutWidget_3 = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 70, 291, 41))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_7 = QtGui.QLabel(self.layoutWidget_3)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_7.addWidget(self.label_7)
        self.nameShorttb = QtGui.QLineEdit(self.layoutWidget_3)
        self.nameShorttb.setReadOnly(True)
        self.nameShorttb.setObjectName(_fromUtf8("nameShorttb"))
        self.horizontalLayout_7.addWidget(self.nameShorttb)
        self.layoutWidget_4 = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 110, 291, 41))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_8 = QtGui.QLabel(self.layoutWidget_4)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_8.addWidget(self.label_8)
        self.authorShortTb = QtGui.QLineEdit(self.layoutWidget_4)
        self.authorShortTb.setReadOnly(True)
        self.authorShortTb.setObjectName(_fromUtf8("authorShortTb"))
        self.horizontalLayout_8.addWidget(self.authorShortTb)
        self.layoutWidget_5 = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget_5.setGeometry(QtCore.QRect(10, 150, 291, 41))
        self.layoutWidget_5.setObjectName(_fromUtf8("layoutWidget_5"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_9 = QtGui.QLabel(self.layoutWidget_5)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_9.addWidget(self.label_9)
        self.keywordsShortTb = QtGui.QLineEdit(self.layoutWidget_5)
        self.keywordsShortTb.setReadOnly(True)
        self.keywordsShortTb.setObjectName(_fromUtf8("keywordsShortTb"))
        self.horizontalLayout_9.addWidget(self.keywordsShortTb)
        self.layoutWidget = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 291, 41))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        self.idShortTb = QtGui.QLineEdit(self.layoutWidget)
        self.idShortTb.setReadOnly(True)
        self.idShortTb.setObjectName(_fromUtf8("idShortTb"))
        self.horizontalLayout_6.addWidget(self.idShortTb)
        self.tabWidget_2.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.layoutWidget_6 = QtGui.QWidget(self.tab_4)
        self.layoutWidget_6.setGeometry(QtCore.QRect(10, 10, 291, 81))
        self.layoutWidget_6.setObjectName(_fromUtf8("layoutWidget_6"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.searchMultipleShortButton = QtGui.QPushButton(self.layoutWidget_6)
        self.searchMultipleShortButton.setObjectName(_fromUtf8("searchMultipleShortButton"))
        self.horizontalLayout_11.addWidget(self.searchMultipleShortButton)
        self.loadDirectoryMultipleShortButton = QtGui.QPushButton(self.layoutWidget_6)
        self.loadDirectoryMultipleShortButton.setObjectName(_fromUtf8("loadDirectoryMultipleShortButton"))
        self.horizontalLayout_11.addWidget(self.loadDirectoryMultipleShortButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.parseMultipleShortButton = QtGui.QPushButton(self.layoutWidget_6)
        self.parseMultipleShortButton.setObjectName(_fromUtf8("parseMultipleShortButton"))
        self.verticalLayout_4.addWidget(self.parseMultipleShortButton)
        self.horizontalLayout_10.addLayout(self.verticalLayout_4)
        self.loadededFilesShortTextEdit = QtGui.QTextEdit(self.tab_4)
        self.loadededFilesShortTextEdit.setGeometry(QtCore.QRect(10, 120, 301, 201))
        self.loadededFilesShortTextEdit.setReadOnly(True)
        self.loadededFilesShortTextEdit.setObjectName(_fromUtf8("loadededFilesShortTextEdit"))
        self.label_11 = QtGui.QLabel(self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(10, 90, 91, 21))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.tabWidget_2.addTab(self.tab_4, _fromUtf8(""))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayoutWidget = QtGui.QWidget(self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 341, 328))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(80, 0))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.textEdit_3 = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.horizontalLayout_3.addWidget(self.textEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(80, 0))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.textEdit = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(80, 0))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.textEdit_2 = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.horizontalLayout_2.addWidget(self.textEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(80, 0))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.fileEdit = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.fileEdit.setObjectName(_fromUtf8("fileEdit"))
        self.horizontalLayout_4.addWidget(self.fileEdit)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(460, 30, 561, 591))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.processButton = QtGui.QPushButton(self.centralwidget)
        self.processButton.setGeometry(QtCore.QRect(120, 600, 95, 31))
        self.processButton.setObjectName(_fromUtf8("processButton"))
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 460, 331, 124))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.PDFCheckBox = QtGui.QCheckBox(self.layoutWidget1)
        self.PDFCheckBox.setChecked(True)
        self.PDFCheckBox.setObjectName(_fromUtf8("PDFCheckBox"))
        self.verticalLayout_2.addWidget(self.PDFCheckBox)
        self.HTMLCheckBox = QtGui.QCheckBox(self.layoutWidget1)
        self.HTMLCheckBox.setChecked(True)
        self.HTMLCheckBox.setObjectName(_fromUtf8("HTMLCheckBox"))
        self.verticalLayout_2.addWidget(self.HTMLCheckBox)
        self.inyectCheckBox = QtGui.QCheckBox(self.layoutWidget1)
        self.inyectCheckBox.setChecked(True)
        self.inyectCheckBox.setObjectName(_fromUtf8("inyectCheckBox"))
        self.verticalLayout_2.addWidget(self.inyectCheckBox)
        self.persistCheckBox = QtGui.QCheckBox(self.layoutWidget1)
        self.persistCheckBox.setChecked(True)
        self.persistCheckBox.setObjectName(_fromUtf8("persistCheckBox"))
        self.verticalLayout_2.addWidget(self.persistCheckBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1043, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuDatabase = QtGui.QMenu(self.menubar)
        self.menuDatabase.setObjectName(_fromUtf8("menuDatabase"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionCreate_database = QtGui.QAction(MainWindow)
        self.actionCreate_database.setObjectName(_fromUtf8("actionCreate_database"))
        self.menuFile.addAction(self.actionQuit)
        self.menuDatabase.addAction(self.actionCreate_database)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDatabase.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Preservation", None))
        self.groupBox.setTitle(_translate("MainWindow", "Information", None))
        self.label_5.setText(_translate("MainWindow", "Tex File: ", None))
        self.searchSingleShortButton.setText(_translate("MainWindow", "Search", None))
        self.parseSingleShortButton.setText(_translate("MainWindow", "Parse", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Parsed info:", None))
        self.label_7.setText(_translate("MainWindow", "Name:", None))
        self.label_8.setText(_translate("MainWindow", "Author:", None))
        self.label_9.setText(_translate("MainWindow", "Keywords:", None))
        self.label_6.setText(_translate("MainWindow", "Id:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Tab 1", None))
        self.searchMultipleShortButton.setText(_translate("MainWindow", "Search", None))
        self.loadDirectoryMultipleShortButton.setText(_translate("MainWindow", "Load directory", None))
        self.parseMultipleShortButton.setText(_translate("MainWindow", "Parse", None))
        self.label_11.setText(_translate("MainWindow", "Loaded files:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Tab 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.label_3.setText(_translate("MainWindow", "Title:", None))
        self.label.setText(_translate("MainWindow", "Author: ", None))
        self.label_2.setText(_translate("MainWindow", "TextLabel", None))
        self.label_4.setText(_translate("MainWindow", "Tex File: ", None))
        self.pushButton.setText(_translate("MainWindow", "Search", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))
        self.processButton.setText(_translate("MainWindow", "Process", None))
        self.PDFCheckBox.setText(_translate("MainWindow", "Create PDF/A", None))
        self.HTMLCheckBox.setText(_translate("MainWindow", "Create HTML", None))
        self.inyectCheckBox.setText(_translate("MainWindow", "Inyect Short WriteUp Documentation", None))
        self.persistCheckBox.setText(_translate("MainWindow", "Persist in database", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuDatabase.setTitle(_translate("MainWindow", "Database", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionCreate_database.setText(_translate("MainWindow", "Create database", None))

