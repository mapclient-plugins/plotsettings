# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from  . import resources_rc
from  . import resources_rc

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        if not ConfigureDialog.objectName():
            ConfigureDialog.setObjectName(u"ConfigureDialog")
        ConfigureDialog.resize(418, 303)
        self.gridLayout = QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.configGroupBox = QGroupBox(ConfigureDialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.gridLayout_3 = QGridLayout(self.configGroupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label0 = QLabel(self.configGroupBox)
        self.label0.setObjectName(u"label0")

        self.gridLayout_3.addWidget(self.label0, 0, 0, 1, 1)

        self.lineEdit0 = QLineEdit(self.configGroupBox)
        self.lineEdit0.setObjectName(u"lineEdit0")

        self.gridLayout_3.addWidget(self.lineEdit0, 0, 1, 1, 1)

        self.pushButtonAdd = QPushButton(self.configGroupBox)
        self.pushButtonAdd.setObjectName(u"pushButtonAdd")
        icon = QIcon()
        icon.addFile(u":/plotsettingsstep/images/Action-edit-add-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonAdd.setIcon(icon)

        self.gridLayout_3.addWidget(self.pushButtonAdd, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.groupBoxSettings = QGroupBox(self.configGroupBox)
        self.groupBoxSettings.setObjectName(u"groupBoxSettings")
        self.verticalLayout = QVBoxLayout(self.groupBoxSettings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_3.addWidget(self.groupBoxSettings, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.configGroupBox, 2, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)


        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        self.buttonBox.rejected.connect(ConfigureDialog.reject)

        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"Configure Step", None))
        self.configGroupBox.setTitle("")
        self.label0.setText(QCoreApplication.translate("ConfigureDialog", u"identifier:  ", None))
        self.pushButtonAdd.setText("")
        self.groupBoxSettings.setTitle(QCoreApplication.translate("ConfigureDialog", u"Settings", None))
    # retranslateUi

