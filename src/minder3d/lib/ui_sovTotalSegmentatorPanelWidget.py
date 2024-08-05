# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovTotalSegmentatorPanelWidgetTstZto.ui'
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

class Ui_TotalSegmentatorPanelWidget(object):
    def setupUi(self, TotalSegmentatorPanelWidget):
        if not TotalSegmentatorPanelWidget.objectName():
            TotalSegmentatorPanelWidget.setObjectName(u"TotalSegmentatorPanelWidget")
        TotalSegmentatorPanelWidget.resize(390, 125)
        self.totalSegmentatorStep1Button = QPushButton(TotalSegmentatorPanelWidget)
        self.totalSegmentatorStep1Button.setObjectName(u"totalSegmentatorStep1Button")
        self.totalSegmentatorStep1Button.setGeometry(QRect(10, 30, 261, 24))
        font = QFont()
        font.setPointSize(7)
        self.totalSegmentatorStep1Button.setFont(font)

        self.retranslateUi(TotalSegmentatorPanelWidget)

        QMetaObject.connectSlotsByName(TotalSegmentatorPanelWidget)
    # setupUi

    def retranslateUi(self, TotalSegmentatorPanelWidget):
        TotalSegmentatorPanelWidget.setWindowTitle(QCoreApplication.translate("TotalSegmentatorPanelWidget", u"Form", None))
        self.totalSegmentatorStep1Button.setText(QCoreApplication.translate("TotalSegmentatorPanelWidget", u"Run Total Segmentator", None))
    # retranslateUi

