# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uamodeler/uamodeler_ui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UaModeler(object):
    def setupUi(self, UaModeler):
        UaModeler.setObjectName("UaModeler")
        UaModeler.resize(922, 692)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/object.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UaModeler.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(UaModeler)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.splitterCenter = QtWidgets.QSplitter(self.centralWidget)
        self.splitterCenter.setOrientation(QtCore.Qt.Horizontal)
        self.splitterCenter.setObjectName("splitterCenter")
        self.splitterLeft = QtWidgets.QSplitter(self.splitterCenter)
        self.splitterLeft.setOrientation(QtCore.Qt.Vertical)
        self.splitterLeft.setObjectName("splitterLeft")
        self.namespaceView = QtWidgets.QTreeView(self.splitterLeft)
        self.namespaceView.setObjectName("namespaceView")
        self.treeView = QtWidgets.QTreeView(self.splitterLeft)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.treeView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeView.setDragEnabled(True)
        self.treeView.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.treeView.setObjectName("treeView")
        self.splitterRight = QtWidgets.QSplitter(self.splitterCenter)
        self.splitterRight.setOrientation(QtCore.Qt.Vertical)
        self.splitterRight.setObjectName("splitterRight")
        self.frame = QtWidgets.QFrame(self.splitterRight)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.attrView = QtWidgets.QTreeView(self.frame)
        self.attrView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.attrView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.attrView.setProperty("showDropIndicator", False)
        self.attrView.setTextElideMode(QtCore.Qt.ElideNone)
        self.attrView.setAutoExpandDelay(-1)
        self.attrView.setIndentation(18)
        self.attrView.setSortingEnabled(True)
        self.attrView.setWordWrap(True)
        self.attrView.setObjectName("attrView")
        self.verticalLayout.addWidget(self.attrView)
        self.attrView.raise_()
        self.label.raise_()
        self.frame_2 = QtWidgets.QFrame(self.splitterRight)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.refView = QtWidgets.QTableView(self.frame_2)
        self.refView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.refView.setObjectName("refView")
        self.verticalLayout_2.addWidget(self.refView)
        self.gridLayout.addWidget(self.splitterCenter, 0, 0, 1, 1)
        UaModeler.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(UaModeler)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 922, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuOPC_UA_Client = QtWidgets.QMenu(self.menuBar)
        self.menuOPC_UA_Client.setObjectName("menuOPC_UA_Client")
        UaModeler.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(UaModeler)
        self.statusBar.setObjectName("statusBar")
        UaModeler.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar(UaModeler)
        self.toolBar.setObjectName("toolBar")
        UaModeler.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAddObject = QtWidgets.QAction(UaModeler)
        self.actionAddObject.setObjectName("actionAddObject")
        self.actionAddVariable = QtWidgets.QAction(UaModeler)
        self.actionAddVariable.setObjectName("actionAddVariable")
        self.actionAddObjectType = QtWidgets.QAction(UaModeler)
        self.actionAddObjectType.setObjectName("actionAddObjectType")
        self.actionAddFolder = QtWidgets.QAction(UaModeler)
        self.actionAddFolder.setObjectName("actionAddFolder")
        self.actionAddProperty = QtWidgets.QAction(UaModeler)
        self.actionAddProperty.setObjectName("actionAddProperty")
        self.actionAddDataType = QtWidgets.QAction(UaModeler)
        self.actionAddDataType.setObjectName("actionAddDataType")
        self.actionAddVariableType = QtWidgets.QAction(UaModeler)
        self.actionAddVariableType.setObjectName("actionAddVariableType")
        self.actionAddReferenceType = QtWidgets.QAction(UaModeler)
        self.actionAddReferenceType.setObjectName("actionAddReferenceType")
        self.actionOpen = QtWidgets.QAction(UaModeler)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(UaModeler)
        self.actionSave.setObjectName("actionSave")
        self.actionQuit = QtWidgets.QAction(UaModeler)
        self.actionQuit.setObjectName("actionQuit")
        self.menuOPC_UA_Client.addAction(self.actionOpen)
        self.menuOPC_UA_Client.addAction(self.actionSave)
        self.menuOPC_UA_Client.addAction(self.actionQuit)
        self.menuBar.addAction(self.menuOPC_UA_Client.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAddFolder)
        self.toolBar.addAction(self.actionAddObject)
        self.toolBar.addAction(self.actionAddVariable)
        self.toolBar.addAction(self.actionAddProperty)
        self.toolBar.addAction(self.actionAddObjectType)
        self.toolBar.addAction(self.actionAddDataType)
        self.toolBar.addAction(self.actionAddVariableType)
        self.toolBar.addAction(self.actionAddReferenceType)

        self.retranslateUi(UaModeler)
        QtCore.QMetaObject.connectSlotsByName(UaModeler)

    def retranslateUi(self, UaModeler):
        _translate = QtCore.QCoreApplication.translate
        UaModeler.setWindowTitle(_translate("UaModeler", "FreeOpcUa Modeler"))
        self.label.setText(_translate("UaModeler", "Attributes Editor"))
        self.label_2.setText(_translate("UaModeler", "References Editor"))
        self.menuOPC_UA_Client.setTitle(_translate("UaModeler", "Act&ions"))
        self.toolBar.setWindowTitle(_translate("UaModeler", "toolBar"))
        self.actionAddObject.setText(_translate("UaModeler", "Add Object"))
        self.actionAddObject.setToolTip(_translate("UaModeler", "add child object to current node"))
        self.actionAddVariable.setText(_translate("UaModeler", "Add Variable"))
        self.actionAddObjectType.setText(_translate("UaModeler", "Add Object Type"))
        self.actionAddObjectType.setToolTip(_translate("UaModeler", "add new object type as subtype of current node"))
        self.actionAddFolder.setText(_translate("UaModeler", "Add Folder"))
        self.actionAddProperty.setText(_translate("UaModeler", "Add Property"))
        self.actionAddDataType.setText(_translate("UaModeler", "Add Data Type"))
        self.actionAddVariableType.setText(_translate("UaModeler", "Add Variable Type"))
        self.actionAddReferenceType.setText(_translate("UaModeler", "Add Reference Type"))
        self.actionOpen.setText(_translate("UaModeler", "&Open"))
        self.actionSave.setText(_translate("UaModeler", "&Save"))
        self.actionQuit.setText(_translate("UaModeler", "&Quit"))

