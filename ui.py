# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 611)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 521, 581))
        self.textEdit.setObjectName("textEdit")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(540, 10, 251, 581))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Notes_list = QtWidgets.QListWidget(parent=self.verticalLayoutWidget)
        self.Notes_list.setObjectName("Notes_list")
        self.verticalLayout.addWidget(self.Notes_list)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_create_note = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btn_create_note.setObjectName("btn_create_note")
        self.horizontalLayout.addWidget(self.btn_create_note)
        self.btn_delete_not = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btn_delete_not.setObjectName("btn_delete_not")
        self.horizontalLayout.addWidget(self.btn_delete_not)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.btn_safe_note = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btn_safe_note.setObjectName("btn_safe_note")
        self.verticalLayout.addWidget(self.btn_safe_note)
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.Tags_list = QtWidgets.QListWidget(parent=self.verticalLayoutWidget)
        self.Tags_list.setObjectName("Tags_list")
        self.verticalLayout.addWidget(self.Tags_list)
        self.tag_search = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.tag_search.setObjectName("tag_search")
        self.verticalLayout.addWidget(self.tag_search)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_add_tag = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btn_add_tag.setObjectName("btn_add_tag")
        self.horizontalLayout_2.addWidget(self.btn_add_tag)
        self.btn_delete_tag = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btn_delete_tag.setObjectName("btn_delete_tag")
        self.horizontalLayout_2.addWidget(self.btn_delete_tag)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.btn_search = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btn_search.setObjectName("btn_search")
        self.verticalLayout.addWidget(self.btn_search)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Список Нотаток"))
        self.btn_create_note.setText(_translate("MainWindow", "Створити Нотатку"))
        self.btn_delete_not.setText(_translate("MainWindow", "Видалити Нотатку"))
        self.btn_safe_note.setText(_translate("MainWindow", "Зберегти Нотатку"))
        self.label_2.setText(_translate("MainWindow", "Список тегів"))
        self.tag_search.setPlaceholderText(_translate("MainWindow", "Пошук по тегу"))
        self.btn_add_tag.setText(_translate("MainWindow", "Додати Тег"))
        self.btn_delete_tag.setText(_translate("MainWindow", "Видалити тег"))
        self.btn_search.setText(_translate("MainWindow", "Шукати по Тегу"))
