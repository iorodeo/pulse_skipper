# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pulse_skipper.ui'
#
# Created: Tue Oct  2 16:48:16 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(411, 331)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.deviceGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.deviceGroupBox.setObjectName(_fromUtf8("deviceGroupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.deviceGroupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.deviceGroupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.portLineEdit = QtGui.QLineEdit(self.deviceGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portLineEdit.sizePolicy().hasHeightForWidth())
        self.portLineEdit.setSizePolicy(sizePolicy)
        self.portLineEdit.setObjectName(_fromUtf8("portLineEdit"))
        self.horizontalLayout.addWidget(self.portLineEdit)
        spacerItem = QtGui.QSpacerItem(15, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.connectPushButton = QtGui.QPushButton(self.deviceGroupBox)
        self.connectPushButton.setObjectName(_fromUtf8("connectPushButton"))
        self.horizontalLayout.addWidget(self.connectPushButton)
        spacerItem1 = QtGui.QSpacerItem(189, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.deviceGroupBox)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_3.addWidget(self.line_2)
        self.pulseGroupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pulseGroupBox.sizePolicy().hasHeightForWidth())
        self.pulseGroupBox.setSizePolicy(sizePolicy)
        self.pulseGroupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.pulseGroupBox.setObjectName(_fromUtf8("pulseGroupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.pulseGroupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget_2 = QtGui.QWidget(self.pulseGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.resetPushButton = QtGui.QPushButton(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resetPushButton.sizePolicy().hasHeightForWidth())
        self.resetPushButton.setSizePolicy(sizePolicy)
        self.resetPushButton.setMinimumSize(QtCore.QSize(120, 0))
        self.resetPushButton.setMaximumSize(QtCore.QSize(120, 16777215))
        self.resetPushButton.setObjectName(_fromUtf8("resetPushButton"))
        self.horizontalLayout_3.addWidget(self.resetPushButton)
        spacerItem2 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.skipPushButton = QtGui.QPushButton(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.skipPushButton.sizePolicy().hasHeightForWidth())
        self.skipPushButton.setSizePolicy(sizePolicy)
        self.skipPushButton.setMinimumSize(QtCore.QSize(120, 0))
        self.skipPushButton.setMaximumSize(QtCore.QSize(120, 16777215))
        self.skipPushButton.setObjectName(_fromUtf8("skipPushButton"))
        self.horizontalLayout_3.addWidget(self.skipPushButton)
        spacerItem3 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.skipSpinBox = QtGui.QSpinBox(self.widget_2)
        self.skipSpinBox.setMinimum(1)
        self.skipSpinBox.setMaximum(9)
        self.skipSpinBox.setObjectName(_fromUtf8("skipSpinBox"))
        self.horizontalLayout_3.addWidget(self.skipSpinBox)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout_3.addWidget(self.pulseGroupBox)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        self.displayGroupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.displayGroupBox.sizePolicy().hasHeightForWidth())
        self.displayGroupBox.setSizePolicy(sizePolicy)
        self.displayGroupBox.setMinimumSize(QtCore.QSize(150, 0))
        self.displayGroupBox.setObjectName(_fromUtf8("displayGroupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.displayGroupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.numberRadioButton = QtGui.QRadioButton(self.displayGroupBox)
        self.numberRadioButton.setObjectName(_fromUtf8("numberRadioButton"))
        self.verticalLayout_2.addWidget(self.numberRadioButton)
        self.binaryRadioButton = QtGui.QRadioButton(self.displayGroupBox)
        self.binaryRadioButton.setObjectName(_fromUtf8("binaryRadioButton"))
        self.verticalLayout_2.addWidget(self.binaryRadioButton)
        self.verticalLayout_3.addWidget(self.displayGroupBox)
        spacerItem5 = QtGui.QSpacerItem(20, 54, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 411, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Pulse Skipper", None, QtGui.QApplication.UnicodeUTF8))
        self.deviceGroupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Device", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.connectPushButton.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.pulseGroupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Pulse", None, QtGui.QApplication.UnicodeUTF8))
        self.resetPushButton.setText(QtGui.QApplication.translate("MainWindow", "Reset Counter", None, QtGui.QApplication.UnicodeUTF8))
        self.skipPushButton.setText(QtGui.QApplication.translate("MainWindow", "Skip", None, QtGui.QApplication.UnicodeUTF8))
        self.displayGroupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Display", None, QtGui.QApplication.UnicodeUTF8))
        self.numberRadioButton.setText(QtGui.QApplication.translate("MainWindow", "Number", None, QtGui.QApplication.UnicodeUTF8))
        self.binaryRadioButton.setText(QtGui.QApplication.translate("MainWindow", "Binary", None, QtGui.QApplication.UnicodeUTF8))

