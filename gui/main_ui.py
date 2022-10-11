# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 400))
        MainWindow.setMaximumSize(QtCore.QSize(800, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_main = QtWidgets.QVBoxLayout()
        self.verticalLayout_main.setObjectName("verticalLayout_main")
        self.groupBox_physicalControllers = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_physicalControllers.setObjectName("groupBox_physicalControllers")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_physicalControllers)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableView_physicalControllerList = QtWidgets.QTableView(self.groupBox_physicalControllers)
        self.tableView_physicalControllerList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView_physicalControllerList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView_physicalControllerList.setObjectName("tableView_physicalControllerList")
        self.tableView_physicalControllerList.horizontalHeader().setStretchLastSection(True)
        self.tableView_physicalControllerList.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tableView_physicalControllerList)
        self.horizontalLayout_physicalControllerActions = QtWidgets.QHBoxLayout()
        self.horizontalLayout_physicalControllerActions.setObjectName("horizontalLayout_physicalControllerActions")
        self.pushButton_physicalControllerRefresh = QtWidgets.QPushButton(self.groupBox_physicalControllers)
        self.pushButton_physicalControllerRefresh.setObjectName("pushButton_physicalControllerRefresh")
        self.horizontalLayout_physicalControllerActions.addWidget(self.pushButton_physicalControllerRefresh)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_physicalControllerActions.addItem(spacerItem)
        self.pushButton_physicalControllerConfig = QtWidgets.QPushButton(self.groupBox_physicalControllers)
        self.pushButton_physicalControllerConfig.setObjectName("pushButton_physicalControllerConfig")
        self.horizontalLayout_physicalControllerActions.addWidget(self.pushButton_physicalControllerConfig)
        self.verticalLayout_2.addLayout(self.horizontalLayout_physicalControllerActions)
        self.verticalLayout_main.addWidget(self.groupBox_physicalControllers)
        self.groupBox_emulatedController = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_emulatedController.setObjectName("groupBox_emulatedController")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_emulatedController)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_emulatedControllerModel = QtWidgets.QLabel(self.groupBox_emulatedController)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_emulatedControllerModel.sizePolicy().hasHeightForWidth())
        self.label_emulatedControllerModel.setSizePolicy(sizePolicy)
        self.label_emulatedControllerModel.setObjectName("label_emulatedControllerModel")
        self.horizontalLayout.addWidget(self.label_emulatedControllerModel)
        self.comboBox_emulatedControllerModel = QtWidgets.QComboBox(self.groupBox_emulatedController)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_emulatedControllerModel.sizePolicy().hasHeightForWidth())
        self.comboBox_emulatedControllerModel.setSizePolicy(sizePolicy)
        self.comboBox_emulatedControllerModel.setObjectName("comboBox_emulatedControllerModel")
        self.comboBox_emulatedControllerModel.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_emulatedControllerModel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_emulatedControllerStart = QtWidgets.QPushButton(self.groupBox_emulatedController)
        self.pushButton_emulatedControllerStart.setObjectName("pushButton_emulatedControllerStart")
        self.horizontalLayout.addWidget(self.pushButton_emulatedControllerStart)
        self.verticalLayout_main.addWidget(self.groupBox_emulatedController)
        self.gridLayout.addLayout(self.verticalLayout_main, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Densha de GO! Controller Converter"))
        self.groupBox_physicalControllers.setTitle(_translate("MainWindow", "Physical controllers"))
        self.pushButton_physicalControllerRefresh.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_physicalControllerConfig.setText(_translate("MainWindow", "Configuration"))
        self.groupBox_emulatedController.setTitle(_translate("MainWindow", "Emulated controller"))
        self.label_emulatedControllerModel.setText(_translate("MainWindow", "Model"))
        self.comboBox_emulatedControllerModel.setItemText(0, _translate("MainWindow", "Two-handle controller for PC (DGOC-44U)"))
        self.pushButton_emulatedControllerStart.setText(_translate("MainWindow", "Start"))
