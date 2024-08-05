# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovNewTaskPanelWidgetoIIuYf.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

class Ui_NewTaskPanelWidget(object):
    def setupUi(self, NewTaskPanelWidget):
        if not NewTaskPanelWidget.objectName():
            NewTaskPanelWidget.setObjectName(u"NewTaskPanelWidget")
        NewTaskPanelWidget.resize(599, 223)
        self.newTaskOtsuButton = QPushButton(NewTaskPanelWidget)
        self.newTaskOtsuButton.setObjectName(u"newTaskOtsuButton")
        self.newTaskOtsuButton.setGeometry(QRect(380, 50, 151, 24))
        font = QFont()
        font.setPointSize(7)
        self.newTaskOtsuButton.setFont(font)
        self.newTaskImageProcessButton = QPushButton(NewTaskPanelWidget)
        self.newTaskImageProcessButton.setObjectName(u"newTaskImageProcessButton")
        self.newTaskImageProcessButton.setGeometry(QRect(380, 20, 151, 24))
        self.newTaskImageProcessButton.setFont(font)
        self.newTaskIndexedOrgansButton = QPushButton(NewTaskPanelWidget)
        self.newTaskIndexedOrgansButton.setObjectName(u"newTaskIndexedOrgansButton")
        self.newTaskIndexedOrgansButton.setGeometry(QRect(20, 50, 171, 24))
        self.newTaskIndexedOrgansButton.setFont(font)
        self.newTaskTotalSegmentatorButton = QPushButton(NewTaskPanelWidget)
        self.newTaskTotalSegmentatorButton.setObjectName(u"newTaskTotalSegmentatorButton")
        self.newTaskTotalSegmentatorButton.setGeometry(QRect(20, 20, 171, 24))
        self.newTaskTotalSegmentatorButton.setFont(font)

        self.retranslateUi(NewTaskPanelWidget)

        QMetaObject.connectSlotsByName(NewTaskPanelWidget)
    # setupUi

    def retranslateUi(self, NewTaskPanelWidget):
        NewTaskPanelWidget.setWindowTitle(QCoreApplication.translate("NewTaskPanelWidget", u"Form", None))
        self.newTaskOtsuButton.setText(QCoreApplication.translate("NewTaskPanelWidget", u"Otsu Threshold", None))
        self.newTaskImageProcessButton.setText(QCoreApplication.translate("NewTaskPanelWidget", u"Image Preprocessing", None))
        self.newTaskIndexedOrgansButton.setText(QCoreApplication.translate("NewTaskPanelWidget", u"Indexed Organ Statistics", None))
        self.newTaskTotalSegmentatorButton.setText(QCoreApplication.translate("NewTaskPanelWidget", u"Total Segmentator", None))
    # retranslateUi

