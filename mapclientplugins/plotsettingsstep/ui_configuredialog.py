# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt\configuredialog.ui'
#
# Created: Fri Aug 12 13:03:12 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        ConfigureDialog.setObjectName("ConfigureDialog")
        ConfigureDialog.resize(418, 303)
        self.gridLayout = QtGui.QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.configGroupBox = QtGui.QGroupBox(ConfigureDialog)
        self.configGroupBox.setTitle("")
        self.configGroupBox.setObjectName("configGroupBox")
        self.gridLayout_3 = QtGui.QGridLayout(self.configGroupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label0 = QtGui.QLabel(self.configGroupBox)
        self.label0.setObjectName("label0")
        self.gridLayout_3.addWidget(self.label0, 0, 0, 1, 1)
        self.lineEdit0 = QtGui.QLineEdit(self.configGroupBox)
        self.lineEdit0.setObjectName("lineEdit0")
        self.gridLayout_3.addWidget(self.lineEdit0, 0, 1, 1, 1)
        self.pushButtonAdd = QtGui.QPushButton(self.configGroupBox)
        self.pushButtonAdd.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/plotsettingsstep/images/Action-edit-add-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonAdd.setIcon(icon)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.gridLayout_3.addWidget(self.pushButtonAdd, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 2, 1, 1, 1)
        self.groupBoxSettings = QtGui.QGroupBox(self.configGroupBox)
        self.groupBoxSettings.setObjectName("groupBoxSettings")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBoxSettings)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout_3.addWidget(self.groupBoxSettings, 1, 0, 1, 2)
        self.gridLayout.addWidget(self.configGroupBox, 2, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)

        self.retranslateUi(ConfigureDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ConfigureDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ConfigureDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfigureDialog)

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QtGui.QApplication.translate("ConfigureDialog", "Configure Step", None, QtGui.QApplication.UnicodeUTF8))
        self.label0.setText(QtGui.QApplication.translate("ConfigureDialog", "identifier:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxSettings.setTitle(QtGui.QApplication.translate("ConfigureDialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
from . import resources_rc
