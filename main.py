from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import requests
import sys
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.retranslateUi(self)

    def get_text(self):
        return self.textEdit.toPlainText()

    def re_curl(self):
        return requests.post(self.get_text())

    def print_text(self):
        self.textBrowser.setText(str(self.re_curl()))
    def setupUi(self, BARK_TOOL):
        BARK_TOOL.setObjectName("BARK_TOOL")
        BARK_TOOL.resize(679, 385)
        self.pushButton = QtWidgets.QPushButton(BARK_TOOL)
        self.pushButton.setGeometry(QtCore.QRect(290, 330, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(BARK_TOOL)
        self.textBrowser.setGeometry(QtCore.QRect(50, 190, 591, 71))
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit = QtWidgets.QTextEdit(BARK_TOOL)
        self.textEdit.setGeometry(QtCore.QRect(50, 70, 591, 64))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(BARK_TOOL)
        self.label.setGeometry(QtCore.QRect(50, 40, 131, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(BARK_TOOL)
        self.label_2.setGeometry(QtCore.QRect(50, 160, 91, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.pushButton.clicked.connect(lambda: self.print_text())

        self.retranslateUi(BARK_TOOL)
        QtCore.QMetaObject.connectSlotsByName(BARK_TOOL)

    def retranslateUi(self, BARK_TOOL):
        _translate = QtCore.QCoreApplication.translate
        BARK_TOOL.setWindowTitle(_translate("BARK_TOOL", "Bark消息推送"))
        self.pushButton.setText(_translate("BARK_TOOL", "发送"))
        self.label.setText(_translate("BARK_TOOL", "推送地址："))
        self.label_2.setText(_translate("BARK_TOOL", "推送结果："))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())

