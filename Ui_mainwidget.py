# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwidget.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QHBoxLayout, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(895, 695)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.update_title_lineEdit = QLineEdit(Form)
        self.update_title_lineEdit.setObjectName(u"update_title_lineEdit")

        self.gridLayout.addWidget(self.update_title_lineEdit, 1, 0, 1, 1)

        self.show_widget = QWidget(Form)
        self.show_widget.setObjectName(u"show_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.show_widget.sizePolicy().hasHeightForWidth())
        self.show_widget.setSizePolicy(sizePolicy)
        self.show_widget.setStyleSheet(u"background-color: rgb(195, 195, 195);")
        self.formLayout = QFormLayout(self.show_widget)
        self.formLayout.setObjectName(u"formLayout")
        self.show_plot_webEngineView = QWebEngineView(self.show_widget)
        self.show_plot_webEngineView.setObjectName(u"show_plot_webEngineView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.show_plot_webEngineView.sizePolicy().hasHeightForWidth())
        self.show_plot_webEngineView.setSizePolicy(sizePolicy1)
        self.show_plot_webEngineView.setUrl(QUrl(u"about:blank"))

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.show_plot_webEngineView)


        self.gridLayout.addWidget(self.show_widget, 2, 0, 1, 1)

        self.options_widget = QWidget(Form)
        self.options_widget.setObjectName(u"options_widget")
        sizePolicy1.setHeightForWidth(self.options_widget.sizePolicy().hasHeightForWidth())
        self.options_widget.setSizePolicy(sizePolicy1)
        self.options_widget.setMinimumSize(QSize(0, 30))
        self.horizontalLayout = QHBoxLayout(self.options_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.import_config_btn = QPushButton(self.options_widget)
        self.import_config_btn.setObjectName(u"import_config_btn")

        self.horizontalLayout.addWidget(self.import_config_btn)

        self.datasource_btn = QPushButton(self.options_widget)
        self.datasource_btn.setObjectName(u"datasource_btn")

        self.horizontalLayout.addWidget(self.datasource_btn)

        self.filter_btn = QPushButton(self.options_widget)
        self.filter_btn.setObjectName(u"filter_btn")

        self.horizontalLayout.addWidget(self.filter_btn)

        self.select_type_comboBox = QComboBox(self.options_widget)
        self.select_type_comboBox.addItem("")
        self.select_type_comboBox.addItem("")
        self.select_type_comboBox.addItem("")
        self.select_type_comboBox.addItem("")
        self.select_type_comboBox.setObjectName(u"select_type_comboBox")

        self.horizontalLayout.addWidget(self.select_type_comboBox)

        self.sort_comboBox = QComboBox(self.options_widget)
        self.sort_comboBox.addItem("")
        self.sort_comboBox.addItem("")
        self.sort_comboBox.addItem("")
        self.sort_comboBox.setObjectName(u"sort_comboBox")

        self.horizontalLayout.addWidget(self.sort_comboBox)

        self.chart_type_comboBox = QComboBox(self.options_widget)
        self.chart_type_comboBox.addItem("")
        self.chart_type_comboBox.addItem("")
        self.chart_type_comboBox.addItem("")
        self.chart_type_comboBox.addItem("")
        self.chart_type_comboBox.addItem("")
        self.chart_type_comboBox.addItem("")
        self.chart_type_comboBox.setObjectName(u"chart_type_comboBox")

        self.horizontalLayout.addWidget(self.chart_type_comboBox)

        self.draw_chart_btn = QPushButton(self.options_widget)
        self.draw_chart_btn.setObjectName(u"draw_chart_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.draw_chart_btn.sizePolicy().hasHeightForWidth())
        self.draw_chart_btn.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.draw_chart_btn)

        self.save_chart_btn = QPushButton(self.options_widget)
        self.save_chart_btn.setObjectName(u"save_chart_btn")
        sizePolicy2.setHeightForWidth(self.save_chart_btn.sizePolicy().hasHeightForWidth())
        self.save_chart_btn.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.save_chart_btn)


        self.gridLayout.addWidget(self.options_widget, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5546\u4e1aBI\u5de5\u5177", None))
        self.update_title_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u6b64\u5904\u53ef\u4fee\u6539\u6807\u9898", None))
        self.import_config_btn.setText(QCoreApplication.translate("Form", u"\u5bfc\u5165\u914d\u7f6e", None))
        self.datasource_btn.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u6e90>>", None))
        self.filter_btn.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u7b5b\u9009", None))
        self.select_type_comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u9009\u62e9\u62a5\u8868\u7c7b\u578b", None))
        self.select_type_comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u95e8\u5e97\u9500\u552e\u6c47\u603b", None))
        self.select_type_comboBox.setItemText(2, QCoreApplication.translate("Form", u"\u8425\u4e1a\u5458\u9500\u552e\u6c47\u603b", None))
        self.select_type_comboBox.setItemText(3, QCoreApplication.translate("Form", u"\u95e8\u5e97\u9500\u552e\u8d70\u52bf", None))

        self.sort_comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u9ed8\u8ba4\u6392\u5e8f", None))
        self.sort_comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u6c47\u603b\u5347\u5e8f", None))
        self.sort_comboBox.setItemText(2, QCoreApplication.translate("Form", u"\u6c47\u603b\u964d\u5e8f", None))

        self.chart_type_comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u9ed8\u8ba4\u67f1\u5f62\u56fe", None))
        self.chart_type_comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u997c\u72b6\u56fe", None))
        self.chart_type_comboBox.setItemText(2, QCoreApplication.translate("Form", u"\u6298\u7ebf\u56fe", None))
        self.chart_type_comboBox.setItemText(3, QCoreApplication.translate("Form", u"\u76f4\u65b9\u56fe", None))
        self.chart_type_comboBox.setItemText(4, QCoreApplication.translate("Form", u"\u6761\u5f62\u56fe", None))
        self.chart_type_comboBox.setItemText(5, QCoreApplication.translate("Form", u"\u6563\u70b9\u56fe", None))

        self.draw_chart_btn.setText(QCoreApplication.translate("Form", u"\u751f\u6210\u56fe\u8868", None))
        self.save_chart_btn.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58\u56fe\u8868", None))
    # retranslateUi

