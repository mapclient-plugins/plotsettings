import json

from PySide2 import QtGui, QtWidgets
from mapclientplugins.plotsettingsstep.ui_configuredialog import Ui_ConfigureDialog

INVALID_STYLE_SHEET = 'background-color: rgba(239, 0, 0, 50)'
DEFAULT_STYLE_SHEET = ''


class ConfigureDialog(QtWidgets.QDialog):
    """
    Configure dialog to present the user with the options to configure this step.
    """

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)

        self._ui = Ui_ConfigureDialog()
        self._ui.setupUi(self)

        # Keep track of the previous identifier so that we can track changes
        # and know how many occurrences of the current identifier there should
        # be.
        self._previousIdentifier = ''
        # Set a place holder for a callable that will get set from the step.
        # We will use this method to decide whether the identifier is unique.
        self.identifierOccursCount = None
        self._settings = {}

        self._makeConnections()

    def _makeConnections(self):
        self._ui.lineEdit0.textChanged.connect(self.validate)
        self._ui.pushButtonAdd.clicked.connect(self._addClicked)

    def _addClicked(self):
        self._addSetting()

    def _addSetting(self, setting=None, value=None):
        layout = self._ui.groupBoxSettings.layout()

        l, b = createSetting(setting, value, self._ui.groupBoxSettings)
        layout.insertLayout(layout.count() - 1, l)
        b.clicked.connect(self._removeClicked)
        self._settings[b] = l

    def _removeClicked(self):
        b = self.sender()
        if b in self._settings:
            l = self._settings[b]
            while l.count():
                item = l.takeAt(0)
                w = item.widget()
                if w:
                    w.hide()
                    w.deleteLater()

            del self._settings[b]
            l.deleteLater()

    def accept(self):
        """
        Override the accept method so that we can confirm saving an
        invalid configuration.
        """
        result = QtWidgets.QMessageBox.Yes
        if not self.validate():
            result = QtWidgets.QMessageBox.warning(self, 'Invalid Configuration',
                                                   'This configuration is invalid.  Unpredictable behaviour may result if you choose \'Yes\', are you sure you want to save this configuration?)',
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.No)

        if result == QtWidgets.QMessageBox.Yes:
            QtWidgets.QDialog.accept(self)

    def validate(self):
        """
        Validate the configuration dialog fields.  For any field that is not valid
        set the style sheet to the INVALID_STYLE_SHEET.  Return the outcome of the
        overall validity of the configuration.
        """
        # Determine if the current identifier is unique throughout the workflow
        # The identifierOccursCount method is part of the interface to the workflow framework.
        value = self.identifierOccursCount(self._ui.lineEdit0.text())
        valid = (value == 0) or (value == 1 and self._previousIdentifier == self._ui.lineEdit0.text())
        if valid:
            self._ui.lineEdit0.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.lineEdit0.setStyleSheet(INVALID_STYLE_SHEET)

        layout = self._ui.groupBoxSettings.layout()
        kids = layout.children()
        for i, k in enumerate(kids):
            line_edit = k.itemAt(1).widget()
            combo_box = k.itemAt(0).widget()
            line_edit = k.itemAt(1).widget()
            current_text = combo_box.currentText()
            value = line_edit.text()
            if current_text == 'xlim' or current_text == 'ylim':
                try:
                    l = json.loads(value)
                    if type(l) == list:
                        line_edit.setStyleSheet(DEFAULT_STYLE_SHEET)
                    else:
                        valid = False
                        line_edit.setStyleSheet(INVALID_STYLE_SHEET)
                except json.decoder.JSONDecodeError:
                    valid = False
                    line_edit.setStyleSheet(INVALID_STYLE_SHEET)

        return valid

    def getConfig(self):
        '''
        Get the current value of the configuration from the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        '''
        self._previousIdentifier = self._ui.lineEdit0.text()
        config = {}
        config['identifier'] = self._ui.lineEdit0.text()
        layout = self._ui.groupBoxSettings.layout()
        kids = layout.children()
        for i, k in enumerate(kids):
            combo_box = k.itemAt(0).widget()
            line_edit = k.itemAt(1).widget()
            current_text = combo_box.currentText()
            value = line_edit.text()
            if current_text == 'xlim' or current_text == 'ylim':
                try:
                    l = json.loads(value)
                    if type(l) == list:
                        value = l
                except json.decoder.JSONDecodeError:
                    pass

            config[str(i)] = [combo_box.currentText(), value]

        return config

    def setConfig(self, config):
        '''
        Set the current value of the configuration for the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        '''
        self._previousIdentifier = config['identifier']
        self._ui.lineEdit0.setText(config['identifier'])
        settings = []
        for key in config:
            if key != 'identifier':
                values = config[key]
                try:
                    index = int(key)
                    len_settings = len(settings)
                    if index >= len_settings:
                        settings.extend([None] * (index - len_settings + 1))

                    value_1 = values[1]
                    if values[0] == 'xlim' or values[0] == 'ylim':
                        if type(value_1) == list:
                            value_1 = json.dumps(value_1)

                    settings[index] = [values[0], value_1]

                except ValueError as e:
                    pass

        assert (None not in settings)
        for s in settings:
            self._addSetting(s[0], s[1])


def createSetting(setting, value, parent):
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(":/plotsettingsstep/images/red_cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    pushButton = QtWidgets.QPushButton(parent)
    pushButton.setIcon(icon)
    setting_combo = QtWidgets.QComboBox(parent)
    setting_combo.addItems(PLOT_SETTINGS)
    if setting:
        index = setting_combo.findText(setting)
        setting_combo.setCurrentIndex(index)
    lineEdit = QtWidgets.QLineEdit(parent)
    if value:
        lineEdit.setText(value)

    layout = QtWidgets.QHBoxLayout()
    layout.addWidget(setting_combo)
    layout.addWidget(lineEdit)
    layout.addWidget(pushButton)

    return layout, pushButton


PLOT_SETTINGS = [
    'xlabel',
    'ylabel',
    'xlim',
    'ylim',
]
