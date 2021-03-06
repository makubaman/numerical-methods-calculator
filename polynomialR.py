
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PolynomialResult(object):
    def setupUi(self, PolynomialResult):
        PolynomialResult.setObjectName("PolynomialResult")
        PolynomialResult.resize(800, 600)
        PolynomialResult.setStyleSheet("QMainWindow {background-color: gray}")
        self.centralwidget = QtWidgets.QWidget(PolynomialResult)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 10, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {color:rgb(255, 170, 0)}")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 250, 100, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setText("Show Equation")
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 100, 261, 500))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(12)


        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 280, 441, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 60, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        PolynomialResult.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PolynomialResult)
        self.statusbar.setObjectName("statusbar")
        PolynomialResult.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(PolynomialResult)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 782, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("QMenuBar {color: rgb(0, 0, 0)}")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        PolynomialResult.setMenuBar(self.menubar)
        self.actionFull_Screen = QtWidgets.QAction(PolynomialResult)
        self.actionFull_Screen.setObjectName("actionFull_Screen")
        self.actionMinimize = QtWidgets.QAction(PolynomialResult)
        self.actionMinimize.setObjectName("actionMinimize")
        self.actionMaximize = QtWidgets.QAction(PolynomialResult)
        self.actionMaximize.setObjectName("actionMaximize")
        self.actionNew = QtWidgets.QAction(PolynomialResult)
        self.actionNew.setShortcutVisibleInContextMenu(False)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(PolynomialResult)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(PolynomialResult)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(PolynomialResult)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionClose = QtWidgets.QAction(PolynomialResult)
        self.actionClose.setObjectName("actionClose")
        self.actionExit = QtWidgets.QAction(PolynomialResult)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(PolynomialResult)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(PolynomialResult)
        self.actionHelp.setObjectName("actionHelp")
        self.actionPreferences = QtWidgets.QAction(PolynomialResult)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionMenu = QtWidgets.QAction(PolynomialResult)
        self.actionMenu.setObjectName("actionMenu")
        self.actionUndo = QtWidgets.QAction(PolynomialResult)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(PolynomialResult)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCut = QtWidgets.QAction(PolynomialResult)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(PolynomialResult)
        self.actionPaste.setObjectName("actionPaste")
        self.actionUndo_2 = QtWidgets.QAction(PolynomialResult)
        self.actionUndo_2.setObjectName("actionUndo_2")
        self.actionRedo_2 = QtWidgets.QAction(PolynomialResult)
        self.actionRedo_2.setObjectName("actionRedo_2")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionUndo_2)
        self.menuEdit.addAction(self.actionRedo_2)
        self.menuView.addAction(self.actionMenu)
        self.menuSettings.addAction(self.actionPreferences)
        self.menuWindow.addAction(self.actionFull_Screen)
        self.menuWindow.addAction(self.actionMinimize)
        self.menuWindow.addAction(self.actionMaximize)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(PolynomialResult)
        QtCore.QMetaObject.connectSlotsByName(PolynomialResult)


    def retranslateUi(self, PolynomialResult):
        _translate = QtCore.QCoreApplication.translate
        PolynomialResult.setWindowTitle(_translate("PolynomialResult", "MainWindow"))
        self.label_2.setText(_translate("PolynomialResult", "Numerical Methods Calculator"))

        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("PolynomialResult", "Summation_x1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("PolynomialResult", "Summation_y1"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("PolynomialResult", "Summation_x1^2"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("PolynomialResult", "Summation_x1^3"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("PolynomialResult", "Summation_x1^4"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("PolynomialResult", "Summation_x1y1"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("PolynomialResult", "Summation_x1^2*y1"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("PolynomialResult", "Mean_x1"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("PolynomialResult", "Mean_y1"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("PolynomialResult", "a0"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("PolynomialResult", "a1"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("PolynomialResult", "a2"))
        #

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("PolynomialResult", "Value"))
        self.label.setText(_translate("PolynomialResult", "y = a0 + a1x + a2x^2 + e"))
        self.label_3.setText(_translate("PolynomialResult", "Polynomial  Regression Analysis "))
        self.menuFile.setTitle(_translate("PolynomialResult", "File"))
        self.menuEdit.setTitle(_translate("PolynomialResult", "Edit"))
        self.menuView.setTitle(_translate("PolynomialResult", "View"))
        self.menuSettings.setTitle(_translate("PolynomialResult", "Settings"))
        self.menuWindow.setTitle(_translate("PolynomialResult", "Window "))
        self.menuHelp.setTitle(_translate("PolynomialResult", "Help"))
        self.actionFull_Screen.setText(_translate("PolynomialResult", "Full Screen"))
        self.actionFull_Screen.setShortcut(_translate("PolynomialResult", "F11"))
        self.actionMinimize.setText(_translate("PolynomialResult", "Minimize"))
        self.actionMinimize.setShortcut(_translate("PolynomialResult", "Ctrl+N"))
        self.actionMaximize.setText(_translate("PolynomialResult", "Maximize"))
        self.actionMaximize.setShortcut(_translate("PolynomialResult", "Ctrl+M"))
        self.actionNew.setText(_translate("PolynomialResult", "New"))
        self.actionNew.setStatusTip(_translate("PolynomialResult", "Create a new file"))
        self.actionNew.setShortcut(_translate("PolynomialResult", "Ctrl+N"))
        self.actionOpen.setText(_translate("PolynomialResult", "Open"))
        self.actionOpen.setStatusTip(_translate("PolynomialResult", "Open a file"))
        self.actionSave.setText(_translate("PolynomialResult", "Save"))
        self.actionSave.setStatusTip(_translate("PolynomialResult", "Save a file"))
        self.actionSave.setShortcut(_translate("PolynomialResult", "Ctrl+S"))
        self.actionSave_As.setText(_translate("PolynomialResult", "Save As"))
        self.actionSave_As.setStatusTip(_translate("PolynomialResult", "Save as a new file"))
        self.actionClose.setText(_translate("PolynomialResult", "Close"))
        self.actionExit.setText(_translate("PolynomialResult", "Exit"))
        self.actionAbout.setText(_translate("PolynomialResult", "About"))
        self.actionAbout.setShortcut(_translate("PolynomialResult", "F12"))
        self.actionHelp.setText(_translate("PolynomialResult", "Help"))
        self.actionHelp.setShortcut(_translate("PolynomialResult", "F1"))
        self.actionPreferences.setText(_translate("PolynomialResult", "Preferences"))
        self.actionPreferences.setShortcut(_translate("PolynomialResult", "F10"))
        self.actionMenu.setText(_translate("PolynomialResult", "Menu"))
        self.actionMenu.setShortcut(_translate("PolynomialResult", "Ctrl+M"))
        self.actionUndo.setText(_translate("PolynomialResult", "History"))
        self.actionUndo.setStatusTip(_translate("PolynomialResult", "Check History"))
        self.actionUndo.setShortcut(_translate("PolynomialResult", "Ctrl+H"))
        self.actionRedo.setText(_translate("PolynomialResult", "Copy"))
        self.actionRedo.setShortcut(_translate("PolynomialResult", "Ctrl+C"))
        self.actionCut.setText(_translate("PolynomialResult", "Cut"))
        self.actionCut.setShortcut(_translate("PolynomialResult", "Ctrl+X"))
        self.actionPaste.setText(_translate("PolynomialResult", "Paste"))
        self.actionUndo_2.setText(_translate("PolynomialResult", "Undo"))
        self.actionUndo_2.setShortcut(_translate("PolynomialResult", "Ctrl+Z"))
        self.actionRedo_2.setText(_translate("PolynomialResult", "Redo"))
        self.actionRedo_2.setShortcut(_translate("PolynomialResult", "Ctrl+R"))


    def populate(self, data):
        self.data = data

        self.tableWidget.setItem(-1, 1, QtWidgets.QTableWidgetItem(str(self.data['totalx'])))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(self.data['totaly'])))
        self.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(str(self.data['totalx2'])))
        self.tableWidget.setItem(2, 1, QtWidgets.QTableWidgetItem(str(self.data['totalx3'])))
        self.tableWidget.setItem(3, 1, QtWidgets.QTableWidgetItem(str(self.data['totalx4'])))
        self.tableWidget.setItem(4, 1, QtWidgets.QTableWidgetItem(str(self.data['totalxy'])))
        self.tableWidget.setItem(5, 1, QtWidgets.QTableWidgetItem(str(self.data['totalx2y'])))

        self.tableWidget.setItem(6, 1, QtWidgets.QTableWidgetItem(str(self.data['mean_x'])))
        self.tableWidget.setItem(7, 1, QtWidgets.QTableWidgetItem(str(self.data['mean_y'])))
        self.tableWidget.setItem(8, 1, QtWidgets.QTableWidgetItem(str(self.data['a0'])))
        self.tableWidget.setItem(9, 1, QtWidgets.QTableWidgetItem(str(self.data['a1'])))
        self.tableWidget.setItem(10, 1, QtWidgets.QTableWidgetItem(str(self.data['a2'])))

    def equation_changed(self):
        a0 = self.data['a0']
        a1 = self.data['a1']
        a2 = self.data['a2']
        self.label.setText(f'y = {a0} + {a1}x + {a2}x^2')




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PolynomialResult = QtWidgets.QMainWindow()
    ui = Ui_PolynomialResult()
    ui.setupUi(PolynomialResult)
    PolynomialResult.show()
    sys.exit(app.exec_())
