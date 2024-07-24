# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovNewTaskPanelWidgetiqWHRy.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QPushButton, QSizePolicy,
    QWidget)

class Ui_NewTaskPanelWidget(object):
    def setupUi(self, NewTaskPanelWidget):
        if not NewTaskPanelWidget.objectName():
            NewTaskPanelWidget.setObjectName(u"NewTaskPanelWidget")
        NewTaskPanelWidget.resize(599, 223)
        self.newTaskOtsuButton = QPushButton(NewTaskPanelWidget)
        self.newTaskOtsuButton.setObjectName(u"newTaskOtsuButton")
        self.newTaskOtsuButton.setGeometry(QRect(230, 60, 151, 24))
        self.newTaskImageProcessButton = QPushButton(NewTaskPanelWidget)
        self.newTaskImageProcessButton.setObjectName(u"newTaskImageProcessButton")
        self.newTaskImageProcessButton.setGeometry(QRect(230, 10, 151, 24))
        self.frame = QFrame(NewTaskPanelWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 191, 171))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.newTaskLungCTAButton = QPushButton(self.frame)
        self.newTaskLungCTAButton.setObjectName(u"newTaskLungCTAButton")
        self.newTaskLungCTAButton.setGeometry(QRect(10, 10, 171, 24))
        self.newTaskBrainCTAMRAButton = QPushButton(self.frame)
        self.newTaskBrainCTAMRAButton.setObjectName(u"newTaskBrainCTAMRAButton")
        self.newTaskBrainCTAMRAButton.setGeometry(QRect(10, 40, 171, 24))
        self.newTaskBrainCTPButton = QPushButton(self.frame)
        self.newTaskBrainCTPButton.setObjectName(u"newTaskBrainCTPButton")
        self.newTaskBrainCTPButton.setGeometry(QRect(10, 70, 171, 24))
        self.newTaskUltrasoundVesselsButton = QPushButton(self.frame)
        self.newTaskUltrasoundVesselsButton.setObjectName(u"newTaskUltrasoundVesselsButton")
        self.newTaskUltrasoundVesselsButton.setGeometry(QRect(10, 100, 171, 24))
        self.newTaskBrainSegmentationButton = QPushButton(self.frame)
        self.newTaskBrainSegmentationButton.setObjectName(u"newTaskBrainSegmentationButton")
        self.newTaskBrainSegmentationButton.setGeometry(QRect(10, 130, 171, 25))

        self.retranslateUi(NewTaskPanelWidget)

        QMetaObject.connectSlotsByName(NewTaskPanelWidget)
    # setupUi

    def retranslateUi(self, NewTaskPanelWidget):
        NewTaskPanelWidget.setWindowTitle(QCoreApplication.translate("NewTaskPanelWidget", u"Form", None))
        self.newTaskOtsuButton.setText(QCoreApplication.translate("NewTaskPanelWidget", u"Demo: Otsu Threshold", None))
        self.newTaskImageProcessButton.setText(QCoreApplication.translate("NewTaskPanelWidget", u"Image Preprocessing", None))
        self.newTaskLungCTAButton.setText(QCoreApplication.translate("NewTaskPanelWidget", u"Lung CTA: Vessels + Airways", None))
        self.newTaskBrainCTAMRAButton.setText(QCoreApplication.translate("NewTaskPanelWidget", u"Brain CTA / MRA: Vessels", None))
        self.newTaskBrainCTPButton.setText(QCoreApplication.translate("NewTaskPanelWidget", u"Brain CT Perfusion", None))
        self.newTaskUltrasoundVesselsButton.setText(QCoreApplication.translate("NewTaskPanelWidget", u"Ultrasound Angio: Vessels", None))
        self.newTaskBrainSegmentationButton.setText(QCoreApplication.translate("NewTaskPanelWidget", u"Brain Segmentation", None))
    # retranslateUi

