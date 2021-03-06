
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from input_table_lr import Ui_InputDataLR


class Ui_LinearRegressionAnalysis(object):
    def setupUi(self, LinearRegressionAnalysis):
        LinearRegressionAnalysis.setObjectName("LinearRegressionAnalysis")
        LinearRegressionAnalysis.resize(800, 600)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        LinearRegressionAnalysis.setFont(font)
        LinearRegressionAnalysis.setStyleSheet("QMainWindow{\n"
"    background-color: gray;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(LinearRegressionAnalysis)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 130, 211, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 60, 300, 60))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("QLabel {\n"
"    color:rgb(255, 170, 0)}")
        self.label.setMidLineWidth(0)
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 370, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QWidget {\n"
"    background-color: rgb(255, 170, 0)\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 140, 401, 131))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QWidget {\n"
"    color: rgb(255, 255, 255)\n"
"}")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(360, 310, 90, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    border-color:red\n"
"}")
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit.setObjectName("lineEdit")
        LinearRegressionAnalysis.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LinearRegressionAnalysis)
        self.statusbar.setObjectName("statusbar")
        LinearRegressionAnalysis.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(LinearRegressionAnalysis)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 781, 21))
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
        LinearRegressionAnalysis.setMenuBar(self.menubar)
        self.actionFull_Screen = QtWidgets.QAction(LinearRegressionAnalysis)
        self.actionFull_Screen.setObjectName("actionFull_Screen")
        self.actionMinimize = QtWidgets.QAction(LinearRegressionAnalysis)
        self.actionMinimize.setObjectName("actionMinimize")
        self.actionMaximize = QtWidgets.QAction(LinearRegressionAnalysis)
        self.actionMaximize.setObjectName("actionMaximize")
        self.actionNew = QtWidgets.QAction(LinearRegressionAnalysis)
        self.actionNew.setShortcutVisibleInContextMenu(False)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(LinearRegressionAnalysis)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(LinearRegressionAnalysis)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(LinearRegressionAnalysis)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionClose = QtWidgets.QAction(LinearRegressionAnalysis)
        self.actionClose.setObjectName("actionClose")
        self.actionExit = QtWidgets.QAction(LinearRegressionAnalysis)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(LinearRegressionAnalysis)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(LinearRegressionAnalysis)
        self.actionHelp.setObjectName("actionHelp")
        self.actionPreferences = QtWidgets.QAction(LinearRegressionAnalysis)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionMenu = QtWidgets.QAction(LinearRegressionAnalysis)
        self.actionMenu.setObjectName("actionMenu")
        self.actionUndo = QtWidgets.QAction(LinearRegressionAnalysis)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(LinearRegressionAnalysis)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCut = QtWidgets.QAction(LinearRegressionAnalysis)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(LinearRegressionAnalysis)
        self.actionPaste.setObjectName("actionPaste")
        self.actionUndo_2 = QtWidgets.QAction(LinearRegressionAnalysis)
        self.actionUndo_2.setObjectName("actionUndo_2")
        self.actionRedo_2 = QtWidgets.QAction(LinearRegressionAnalysis)
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

        self.retranslateUi(LinearRegressionAnalysis)
        QtCore.QMetaObject.connectSlotsByName(LinearRegressionAnalysis)
        
        self.pushButton_3.clicked.connect(self.switch_to_lr)

    def retranslateUi(self, LinearRegressionAnalysis):
        _translate = QtCore.QCoreApplication.translate
        LinearRegressionAnalysis.setWindowTitle(_translate("LinearRegressionAnalysis", "Linear Regression"))
        self.pushButton.setText(_translate("LinearRegressionAnalysis", "Linear Regression Analysis"))
        self.label.setText(_translate("LinearRegressionAnalysis", "  Curve Fitting"))
        self.pushButton_3.setText(_translate("LinearRegressionAnalysis", "Generate "))
        self.label_2.setText(_translate("LinearRegressionAnalysis", "Enter the number of pairs of data"))
        self.menuFile.setTitle(_translate("LinearRegressionAnalysis", "File"))
        self.menuEdit.setTitle(_translate("LinearRegressionAnalysis", "Edit"))
        self.menuView.setTitle(_translate("LinearRegressionAnalysis", "View"))
        self.menuSettings.setTitle(_translate("LinearRegressionAnalysis", "Settings"))
        self.menuWindow.setTitle(_translate("LinearRegressionAnalysis", "Window "))
        self.menuHelp.setTitle(_translate("LinearRegressionAnalysis", "Help"))
        self.actionFull_Screen.setText(_translate("LinearRegressionAnalysis", "Full Screen"))
        self.actionFull_Screen.setShortcut(_translate("LinearRegressionAnalysis", "F11"))
        self.actionMinimize.setText(_translate("LinearRegressionAnalysis", "Minimize"))
        self.actionMinimize.setShortcut(_translate("LinearRegressionAnalysis", "Ctrl+N"))
        self.actionMaximize.setText(_translate("LinearRegressionAnalysis", "Maximize"))
        self.actionMaximize.setShortcut(_translate("LinearRegressionAnalysis", "Ctrl+M"))
        self.actionNew.setText(_translate("LinearRegressionAnalysis", "New"))
        self.actionNew.setStatusTip(_translate("LinearRegressionAnalysis", "Create a new file"))
        self.actionNew.setShortcut(_translate("LinearRegressionAnalysis", "Ctrl+N"))
        self.actionOpen.setText(_translate("LinearRegressionAnalysis", "Open"))
        self.actionOpen.setStatusTip(_translate("LinearRegressionAnalysis", "Open a file"))
        self.actionSave.setText(_translate("LinearRegressionAnalysis", "Save"))
        self.actionSave.setStatusTip(_translate("LinearRegressionAnalysis", "Save a file"))
        self.actionSave.setShortcut(_translate("LinearRegressionAnalysis", "Ctrl+S"))
        self.actionSave_As.setText(_translate("LinearRegressionAnalysis", "Save As"))
        self.actionSave_As.setStatusTip(_translate("LinearRegressionAnalysis", "Save as a new file"))
        self.actionClose.setText(_translate("LinearRegressionAnalysis", "Close"))
        self.actionExit.setText(_translate("LinearRegressionAnalysis", "Exit"))
        self.actionAbout.setText(_translate("LinearRegressionAnalysis", "About"))
        self.actionAbout.setShortcut(_translate("LinearRegressionAnalysis", "F12"))
        self.actionHelp.setText(_translate("LinearRegressionAnalysis", "Help"))
        self.actionHelp.setShortcut(_translate("LinearRegressionAnalysis", "F1"))
        self.actionPreferences.setText(_translate("LinearRegressionAnalysis", "Preferences"))
        self.actionPreferences.setShortcut(_translate("LinearRegressionAnalysis", "F10"))
        self.actionMenu.setText(_translate("LinearRegressionAnalysis", "Menu"))
        self.actionMenu.setShortcut(_translate("LinearRegressionAnalysis", "Ctrl+M"))
        self.actionUndo.setText(_translate("LinearRegressionAnalysis", "History"))
        self.actionUndo.setStatusTip(_translate("LinearRegressionAnalysis", "Check History"))
        self.actionUndo.setShortcut(_translate("LinearRegressionAnalysis", "Ctrl+H"))
        self.actionRedo.setText(_translate("LinearRegressionAnalysis", "Copy"))
        self.actionRedo.setShortcut(_translate("LinearRegressionAnalysis", "Ctrl+C"))
        self.actionCut.setText(_translate("LinearRegressionAnalysis", "Cut"))
        self.actionCut.setShortcut(_translate("LinearRegressionAnalysis", "Ctrl+X"))
        self.actionPaste.setText(_translate("LinearRegressionAnalysis", "Paste"))
        self.actionUndo_2.setText(_translate("LinearRegressionAnalysis", "Undo"))
        self.actionUndo_2.setShortcut(_translate("LinearRegressionAnalysis", "Ctrl+Z"))
        self.actionRedo_2.setText(_translate("LinearRegressionAnalysis", "Redo"))
        self.actionRedo_2.setShortcut(_translate("LinearRegressionAnalysis", "Ctrl+R"))


    def switch_to_lr(self):
        try:
            cc = (self.lineEdit.text())
            column_count = int(round(float(cc)))
            self.window = QtWidgets.QWidget()
            self.ui = Ui_InputDataLR()
            self.ui.setupUi(self.window)
            self.window.show()
            self.ui.tableWidget.setColumnCount(column_count)
        except ValueError:
            cc = (self.lineEdit.setText(""))
            self.error_messageBox()
            print("Please enter an integer!")

    def error_messageBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Input Error")
        msg.setText("Please input an Integer")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Retry)
        x = msg.exec_()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LinearRegressionAnalysis = QtWidgets.QMainWindow()
    ui = Ui_LinearRegressionAnalysis()
    ui.setupUi(LinearRegressionAnalysis)
    LinearRegressionAnalysis.show()
    sys.exit(app.exec_())
