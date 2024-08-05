# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovIndexedOrgansPanelWidgetDReuHo.ui'
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

class Ui_IndexedOrgansPanelWidget(object):
    def setupUi(self, IndexedOrgansPanelWidget):
        if not IndexedOrgansPanelWidget.objectName():
            IndexedOrgansPanelWidget.setObjectName(u"IndexedOrgansPanelWidget")
        IndexedOrgansPanelWidget.resize(390, 125)
        self.indexedOrgansStep1Button = QPushButton(IndexedOrgansPanelWidget)
        self.indexedOrgansStep1Button.setObjectName(u"indexedOrgansStep1Button")
        self.indexedOrgansStep1Button.setGeometry(QRect(10, 30, 261, 24))
        font = QFont()
        font.setPointSize(7)
        self.indexedOrgansStep1Button.setFont(font)

        self.retranslateUi(IndexedOrgansPanelWidget)

        QMetaObject.connectSlotsByName(IndexedOrgansPanelWidget)
    # setupUi

    def retranslateUi(self, IndexedOrgansPanelWidget):
        IndexedOrgansPanelWidget.setWindowTitle(QCoreApplication.translate("IndexedOrgansPanelWidget", u"Form", None))
        self.indexedOrgansStep1Button.setText(QCoreApplication.translate("IndexedOrgansPanelWidget", u"Run Total Segmentator", None))
    # retranslateUi

