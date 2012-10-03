from __future__ import print_function
import sys
import serial
import functools
from PyQt4 import QtCore
from PyQt4 import QtGui
from pulse_skipper_ui import Ui_MainWindow 
from pulse_skipper_serial import PulseSkipperSerial


class PulseSkipper(QtGui.QMainWindow, Ui_MainWindow):

    DEFAULT_PORT = '/dev/ttyUSB8'

    def __init__(self, parent=None):
        super(PulseSkipper,self).__init__(parent)
        self.setupUi(self)
        self.connectActions()
        self.initialize()

    def main(self):
        self.show()

    def connectActions(self):
        self.connectPushButton.pressed.connect(self.connectPressed)
        self.connectPushButton.clicked.connect(self.connectClicked)
        self.skipPushButton.clicked.connect(self.skipClicked)
        self.resetPushButton.clicked.connect(self.resetClicked)
        numberToggledCallback = functools.partial(self.displayToggled,'number')
        self.numberRadioButton.toggled.connect(numberToggledCallback)
        binaryToggledCallback = functools.partial(self.displayToggled,'binary')
        self.binaryRadioButton.toggled.connect(binaryToggledCallback)

    def initialize(self):
        self.dev = None
        self.port = PulseSkipper.DEFAULT_PORT
        self.portLineEdit.setText(self.port)
        self.setEnabledOnDisconnect()
        self.numberRadioButton.setChecked(True)
        self.binaryRadioButton.setChecked(False)


    def connectPressed(self):
        self.portLineEdit.setEnabled(False)
        self.connectPushButton.setText('Disconnect')

    def connectClicked(self):
        if self.dev is None:
            try:
                self.dev = PulseSkipperSerial(self.port)
                #self.dev = True
            except serial.serialutil.SerialException, e: 
                errMsg = '{0}'.format(str(e)) 
                QtGui.QMessageBox.critical(self,'Error',errMsg) 
                self.portLineEdit.setEnabled(True) 
                self.connectPushButton.setText('Connect')
                self.dev = None
            if self.dev is not None:
                self.setEnabledOnConnect()
                self.setDisplay()

        else: 
            self.portLineEdit.setEnabled(True) 
            self.connectPushButton.setText('Connect') 
            self.setEnabledOnDisconnect()
            self.dev.close() 
            #self.dev = None 


    def skipClicked(self):
        skipValue = self.skipSpinBox.value()
        self.dev.skipPulse(skipValue)

    def resetClicked(self):
        self.dev.resetCount()

    def displayToggled(self, name):
        if self.dev is not None:
            self.setDisplay()

    def setDisplay(self):
        if self.binaryRadioButton.isChecked():
            self.dev.setDisplayBinary()
        else:
            self.dev.setDisplayNumber()

    def setEnabledOnDisconnect(self):
        self.pulseGroupBox.setEnabled(False)
        self.displayGroupBox.setEnabled(False)

    def setEnabledOnConnect(self):
        self.pulseGroupBox.setEnabled(True)
        self.displayGroupBox.setEnabled(True)

def runApp():
    app = QtGui.QApplication(sys.argv)
    win = PulseSkipper()
    win.main()
    app.exec_()


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    runApp()

