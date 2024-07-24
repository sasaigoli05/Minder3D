# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovBrainSegmentationPanelWidgetwrLjMf.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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

class Ui_BrainSegmentationPanelWidget(object):
    def setupUi(self, BrainSegmentationPanelWidget):
        if not BrainSegmentationPanelWidget.objectName():
            BrainSegmentationPanelWidget.setObjectName(u"BrainSegmentationPanelWidget")
        BrainSegmentationPanelWidget.resize(390, 125)
        self.BrainStep1Button = QPushButton(BrainSegmentationPanelWidget)
        self.BrainStep1Button.setObjectName(u"BrainStep1Button")
        self.BrainStep1Button.setGeometry(QRect(70, 50, 261, 24))

        self.retranslateUi(BrainSegmentationPanelWidget)

        QMetaObject.connectSlotsByName(BrainSegmentationPanelWidget)
    # setupUi

    def retranslateUi(self, BrainSegmentationPanelWidget):
        BrainSegmentationPanelWidget.setWindowTitle(QCoreApplication.translate("BrainSegmentationPanelWidget", u"Form", None))
        self.BrainStep1Button.setText(QCoreApplication.translate("BrainSegmentationPanelWidget", u"Brain Segmentation", None))
    # retranslateUi

