# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'importconfig.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_import_Form(object):
    def setupUi(self, import_Form):
        if not import_Form.objectName():
            import_Form.setObjectName(u"import_Form")
        import_Form.resize(306, 270)
        self.gridLayout = QGridLayout(import_Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(import_Form)
        self.label_5.setObjectName(u"label_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 2)

        self.date_map_lineEdit = QLineEdit(import_Form)
        self.date_map_lineEdit.setObjectName(u"date_map_lineEdit")

        self.gridLayout.addWidget(self.date_map_lineEdit, 1, 0, 1, 1)

        self.label = QLabel(import_Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.depts_map_lineEdit = QLineEdit(import_Form)
        self.depts_map_lineEdit.setObjectName(u"depts_map_lineEdit")

        self.gridLayout.addWidget(self.depts_map_lineEdit, 2, 0, 1, 1)

        self.label_2 = QLabel(import_Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)

        self.employees_map_lineEdit = QLineEdit(import_Form)
        self.employees_map_lineEdit.setObjectName(u"employees_map_lineEdit")

        self.gridLayout.addWidget(self.employees_map_lineEdit, 3, 0, 1, 1)

        self.label_4 = QLabel(import_Form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)

        self.goods_map_lineEdit = QLineEdit(import_Form)
        self.goods_map_lineEdit.setObjectName(u"goods_map_lineEdit")

        self.gridLayout.addWidget(self.goods_map_lineEdit, 4, 0, 1, 1)

        self.label_3 = QLabel(import_Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)

        self.sales_map_lineEdit = QLineEdit(import_Form)
        self.sales_map_lineEdit.setObjectName(u"sales_map_lineEdit")

        self.gridLayout.addWidget(self.sales_map_lineEdit, 5, 0, 1, 1)

        self.label_6 = QLabel(import_Form)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 1, 1, 1)


        self.retranslateUi(import_Form)

        QMetaObject.connectSlotsByName(import_Form)
    # setupUi

    def retranslateUi(self, import_Form):
        import_Form.setWindowTitle(QCoreApplication.translate("import_Form", u"\u6570\u636e\u6587\u4ef6\u5bfc\u5165\u914d\u7f6e", None))
        self.label_5.setText(QCoreApplication.translate("import_Form", u"\u5b57\u6bb5\u5bf9\u7167\u8bbe\u7f6e(\u5bfc\u5165\u6587\u4ef6\u4e0e\u7cfb\u7edf\u5b57\u6bb5\u540d\u4e00\u81f4\u65e0\u9700\u586b\u5199)", None))
        self.label.setText(QCoreApplication.translate("import_Form", u"==>> \u5165\u8d26\u65e5\u671f", None))
        self.label_2.setText(QCoreApplication.translate("import_Form", u"==>> \u90e8\u95e8\u540d\u79f0", None))
        self.label_4.setText(QCoreApplication.translate("import_Form", u"==>> \u8425\u4e1a\u5458\u540d\u79f0", None))
        self.label_3.setText(QCoreApplication.translate("import_Form", u"==>> \u5546\u54c1\u540d\u79f0", None))
        self.label_6.setText(QCoreApplication.translate("import_Form", u"==>> \u9500\u552e\u6536\u5165", None))
    # retranslateUi

