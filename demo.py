# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(447, 527)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 70, 391, 391))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.price = QtWidgets.QLabel(self.formLayoutWidget)
        self.price.setStyleSheet("font: 22pt \"Sans Serif\";")
        self.price.setObjectName("price")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.price)
        self.tax_rate_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.tax_rate_label.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.tax_rate_label.setObjectName("tax_rate_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.tax_rate_label)
        self.tax_rate = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.tax_rate.setProperty("value", 20)
        self.tax_rate.setObjectName("tax_rate")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.tax_rate)
        self.pricebox = QtWidgets.QTextEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pricebox.sizePolicy().hasHeightForWidth())
        self.pricebox.setSizePolicy(sizePolicy)
        self.pricebox.setMinimumSize(QtCore.QSize(115, 0))
        self.pricebox.setObjectName("pricebox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pricebox)
        self.calc_tax_button = QtWidgets.QPushButton(self.centralwidget)
        self.calc_tax_button.setGeometry(QtCore.QRect(170, 170, 115, 27))
        self.calc_tax_button.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.calc_tax_button.setObjectName("calc_tax_button")
        self.results_window = QtWidgets.QTextEdit(self.centralwidget)
        self.results_window.setGeometry(QtCore.QRect(80, 230, 302, 192))
        self.results_window.setObjectName("results_window")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 20, 322, 38))
        self.label.setStyleSheet("font: 24pt \"Sans Serif\";")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 447, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.calc_tax_button.clicked.connect(self.CalcTax)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.price.setText(_translate("MainWindow", "Price"))
        self.tax_rate_label.setText(_translate("MainWindow", "Tax Rate"))
        self.calc_tax_button.setText(_translate("MainWindow", "Calculate Tax"))
        self.label.setText(_translate("MainWindow", "Sales Tax Calculator"))

    def CalcTax(self):
        price = int(self.pricebox.toPlainText())
        tax = (self.tax_rate.value())
        total_price = price + ((tax/100)*price)
        total_price_string = "The total price with tax is :" + str(total_price)
        self.results_window.setText(total_price_string)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
