# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filterwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListView,
    QPushButton, QSizePolicy, QTableView, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(712, 726)
        self.verticalLayout_3 = QVBoxLayout(widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.quick_date_comboBox = QComboBox(widget)
        self.quick_date_comboBox.addItem("")
        self.quick_date_comboBox.addItem("")
        self.quick_date_comboBox.addItem("")
        self.quick_date_comboBox.addItem("")
        self.quick_date_comboBox.addItem("")
        self.quick_date_comboBox.addItem("")
        self.quick_date_comboBox.addItem("")
        self.quick_date_comboBox.addItem("")
        self.quick_date_comboBox.addItem("")
        self.quick_date_comboBox.addItem("")
        self.quick_date_comboBox.addItem("")
        self.quick_date_comboBox.setObjectName(u"quick_date_comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quick_date_comboBox.sizePolicy().hasHeightForWidth())
        self.quick_date_comboBox.setSizePolicy(sizePolicy)
        self.quick_date_comboBox.setMinimumSize(QSize(75, 0))

        self.horizontalLayout.addWidget(self.quick_date_comboBox)

        self.label_2 = QLabel(widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.start_dateEdit = QDateEdit(widget)
        self.start_dateEdit.setObjectName(u"start_dateEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.start_dateEdit.sizePolicy().hasHeightForWidth())
        self.start_dateEdit.setSizePolicy(sizePolicy1)
        self.start_dateEdit.setDateTime(QDateTime(QDate(2015, 9, 10), QTime(8, 0, 0)))
        self.start_dateEdit.setDate(QDate(2015, 9, 10))

        self.horizontalLayout.addWidget(self.start_dateEdit)

        self.label_4 = QLabel(widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.end_dateEdit = QDateEdit(widget)
        self.end_dateEdit.setObjectName(u"end_dateEdit")
        sizePolicy1.setHeightForWidth(self.end_dateEdit.sizePolicy().hasHeightForWidth())
        self.end_dateEdit.setSizePolicy(sizePolicy1)
        self.end_dateEdit.setDateTime(QDateTime(QDate(2015, 9, 30), QTime(8, 0, 0)))
        self.end_dateEdit.setDate(QDate(2015, 9, 30))

        self.horizontalLayout.addWidget(self.end_dateEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.dept_comparison_comboBox = QComboBox(widget)
        self.dept_comparison_comboBox.addItem("")
        self.dept_comparison_comboBox.addItem("")
        self.dept_comparison_comboBox.addItem("")
        self.dept_comparison_comboBox.addItem("")
        self.dept_comparison_comboBox.setObjectName(u"dept_comparison_comboBox")

        self.horizontalLayout_2.addWidget(self.dept_comparison_comboBox)

        self.dept_lineEdit = QLineEdit(widget)
        self.dept_lineEdit.setObjectName(u"dept_lineEdit")

        self.horizontalLayout_2.addWidget(self.dept_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.employee_comparsion_comboBox = QComboBox(widget)
        self.employee_comparsion_comboBox.addItem("")
        self.employee_comparsion_comboBox.addItem("")
        self.employee_comparsion_comboBox.addItem("")
        self.employee_comparsion_comboBox.setObjectName(u"employee_comparsion_comboBox")

        self.horizontalLayout_3.addWidget(self.employee_comparsion_comboBox)

        self.employee_lineEdit = QLineEdit(widget)
        self.employee_lineEdit.setObjectName(u"employee_lineEdit")

        self.horizontalLayout_3.addWidget(self.employee_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(widget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.goods_comparison_comboBox = QComboBox(widget)
        self.goods_comparison_comboBox.addItem("")
        self.goods_comparison_comboBox.addItem("")
        self.goods_comparison_comboBox.addItem("")
        self.goods_comparison_comboBox.addItem("")
        self.goods_comparison_comboBox.setObjectName(u"goods_comparison_comboBox")

        self.horizontalLayout_4.addWidget(self.goods_comparison_comboBox)

        self.goods_lineEdit = QLineEdit(widget)
        self.goods_lineEdit.setObjectName(u"goods_lineEdit")

        self.horizontalLayout_4.addWidget(self.goods_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.filtered_conditions_textEdit = QTextEdit(widget)
        self.filtered_conditions_textEdit.setObjectName(u"filtered_conditions_textEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.filtered_conditions_textEdit.sizePolicy().hasHeightForWidth())
        self.filtered_conditions_textEdit.setSizePolicy(sizePolicy2)
        self.filtered_conditions_textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.filtered_conditions_textEdit)


        self.horizontalLayout_6.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.filtered_data_listView = QListView(widget)
        self.filtered_data_listView.setObjectName(u"filtered_data_listView")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.filtered_data_listView.sizePolicy().hasHeightForWidth())
        self.filtered_data_listView.setSizePolicy(sizePolicy3)
        self.filtered_data_listView.setMaximumSize(QSize(180, 16777215))

        self.verticalLayout_2.addWidget(self.filtered_data_listView)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.filter_ok_btn = QPushButton(widget)
        self.filter_ok_btn.setObjectName(u"filter_ok_btn")

        self.horizontalLayout_7.addWidget(self.filter_ok_btn)

        self.filter_cancel_btn = QPushButton(widget)
        self.filter_cancel_btn.setObjectName(u"filter_cancel_btn")

        self.horizontalLayout_7.addWidget(self.filter_cancel_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_6.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.database_tableView = QTableView(widget)
        self.database_tableView.setObjectName(u"database_tableView")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.database_tableView.sizePolicy().hasHeightForWidth())
        self.database_tableView.setSizePolicy(sizePolicy4)

        self.verticalLayout_3.addWidget(self.database_tableView)


        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"\u6570\u636e\u7b5b\u9009", None))
        self.quick_date_comboBox.setItemText(0, QCoreApplication.translate("widget", u"\u5feb\u6377\u65e5\u671f", None))
        self.quick_date_comboBox.setItemText(1, QCoreApplication.translate("widget", u"\u4eca\u5929", None))
        self.quick_date_comboBox.setItemText(2, QCoreApplication.translate("widget", u"\u6628\u5929", None))
        self.quick_date_comboBox.setItemText(3, QCoreApplication.translate("widget", u"\u4e0a\u5468", None))
        self.quick_date_comboBox.setItemText(4, QCoreApplication.translate("widget", u"\u4e0a\u6708", None))
        self.quick_date_comboBox.setItemText(5, QCoreApplication.translate("widget", u"\u4e0a\u5b63\u5ea6", None))
        self.quick_date_comboBox.setItemText(6, QCoreApplication.translate("widget", u"\u4e0a\u5e74", None))
        self.quick_date_comboBox.setItemText(7, QCoreApplication.translate("widget", u"\u672c\u5468", None))
        self.quick_date_comboBox.setItemText(8, QCoreApplication.translate("widget", u"\u672c\u6708", None))
        self.quick_date_comboBox.setItemText(9, QCoreApplication.translate("widget", u"\u672c\u5b63\u5ea6", None))
        self.quick_date_comboBox.setItemText(10, QCoreApplication.translate("widget", u"\u672c\u5e74", None))

        self.label_2.setText(QCoreApplication.translate("widget", u"\u8d77\u59cb\u65e5\u671f", None))
        self.label_4.setText(QCoreApplication.translate("widget", u"\u7ed3\u675f\u65e5\u671f", None))
        self.label.setText(QCoreApplication.translate("widget", u"\u90e8\u95e8\u540d\u79f0", None))
        self.dept_comparison_comboBox.setItemText(0, QCoreApplication.translate("widget", u"\u5305\u542b", None))
        self.dept_comparison_comboBox.setItemText(1, QCoreApplication.translate("widget", u"\u5de6\u7b49\u4e8e", None))
        self.dept_comparison_comboBox.setItemText(2, QCoreApplication.translate("widget", u"\u53f3\u7b49\u4e8e", None))
        self.dept_comparison_comboBox.setItemText(3, "")

        self.dept_lineEdit.setPlaceholderText(QCoreApplication.translate("widget", u"\u591a\u4e2a\u6761\u4ef6\u7528\u82f1\u6587\u9017\u53f7\u9694\u5f00", None))
        self.label_3.setText(QCoreApplication.translate("widget", u"\u8425\u4e1a\u5458   ", None))
        self.employee_comparsion_comboBox.setItemText(0, QCoreApplication.translate("widget", u"\u5305\u542b", None))
        self.employee_comparsion_comboBox.setItemText(1, QCoreApplication.translate("widget", u"\u5de6\u7b49\u4e8e", None))
        self.employee_comparsion_comboBox.setItemText(2, QCoreApplication.translate("widget", u"\u53f3\u7b49\u4e8e", None))

        self.employee_lineEdit.setPlaceholderText(QCoreApplication.translate("widget", u"\u591a\u4e2a\u6761\u4ef6\u7528\u82f1\u6587\u9017\u53f7\u9694\u5f00", None))
        self.label_5.setText(QCoreApplication.translate("widget", u"\u5546\u54c1\u540d\u79f0", None))
        self.goods_comparison_comboBox.setItemText(0, QCoreApplication.translate("widget", u"\u5305\u542b", None))
        self.goods_comparison_comboBox.setItemText(1, QCoreApplication.translate("widget", u"\u5de6\u7b49\u4e8e", None))
        self.goods_comparison_comboBox.setItemText(2, QCoreApplication.translate("widget", u"\u53f3\u7b49\u4e8e", None))
        self.goods_comparison_comboBox.setItemText(3, "")

        self.goods_lineEdit.setPlaceholderText(QCoreApplication.translate("widget", u"\u591a\u4e2a\u6761\u4ef6\u7528\u82f1\u6587\u9017\u53f7\u9694\u5f00", None))
        self.filter_ok_btn.setText(QCoreApplication.translate("widget", u"\u786e\u5b9a", None))
        self.filter_cancel_btn.setText(QCoreApplication.translate("widget", u"\u53d6\u6d88", None))
    # retranslateUi

