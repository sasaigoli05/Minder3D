# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovImportDICOMPanelWidgetnZPssa.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_ImportDICOMPanelWidget(object):
    def setupUi(self, ImportDICOMPanelWidget):
        if not ImportDICOMPanelWidget.objectName():
            ImportDICOMPanelWidget.setObjectName(u"ImportDICOMPanelWidget")
        ImportDICOMPanelWidget.resize(715, 153)
        self.importDICOMInstructionsTextEdit = QTextEdit(ImportDICOMPanelWidget)
        self.importDICOMInstructionsTextEdit.setObjectName(u"importDICOMInstructionsTextEdit")
        self.importDICOMInstructionsTextEdit.setGeometry(QRect(20, 10, 301, 131))
        self.importDICOMInstructionsTextEdit.setReadOnly(True)
        self.importDICOMInputDirectoryLineEdit = QLineEdit(ImportDICOMPanelWidget)
        self.importDICOMInputDirectoryLineEdit.setObjectName(u"importDICOMInputDirectoryLineEdit")
        self.importDICOMInputDirectoryLineEdit.setGeometry(QRect(430, 20, 221, 21))
        self.importDICOMInputDirectoryLabel = QLabel(ImportDICOMPanelWidget)
        self.importDICOMInputDirectoryLabel.setObjectName(u"importDICOMInputDirectoryLabel")
        self.importDICOMInputDirectoryLabel.setGeometry(QRect(330, 20, 81, 16))
        font = QFont()
        font.setPointSize(7)
        self.importDICOMInputDirectoryLabel.setFont(font)
        self.importDICOMInputDirectorySelectButton = QPushButton(ImportDICOMPanelWidget)
        self.importDICOMInputDirectorySelectButton.setObjectName(u"importDICOMInputDirectorySelectButton")
        self.importDICOMInputDirectorySelectButton.setGeometry(QRect(660, 20, 20, 21))
        self.importDICOMInputDirectorySelectButton.setFont(font)
        self.importDICOMOutputDirectorySelectButton = QPushButton(ImportDICOMPanelWidget)
        self.importDICOMOutputDirectorySelectButton.setObjectName(u"importDICOMOutputDirectorySelectButton")
        self.importDICOMOutputDirectorySelectButton.setGeometry(QRect(660, 50, 20, 21))
        self.importDICOMOutputDirectorySelectButton.setFont(font)
        self.importDICOMOutputDirectoryLineEdit = QLineEdit(ImportDICOMPanelWidget)
        self.importDICOMOutputDirectoryLineEdit.setObjectName(u"importDICOMOutputDirectoryLineEdit")
        self.importDICOMOutputDirectoryLineEdit.setGeometry(QRect(430, 50, 221, 21))
        self.importDICOMOutputDirectoryLabel = QLabel(ImportDICOMPanelWidget)
        self.importDICOMOutputDirectoryLabel.setObjectName(u"importDICOMOutputDirectoryLabel")
        self.importDICOMOutputDirectoryLabel.setGeometry(QRect(330, 50, 91, 16))
        self.importDICOMOutputDirectoryLabel.setFont(font)
        self.importDICOMAutoRegisterCheckBox = QCheckBox(ImportDICOMPanelWidget)
        self.importDICOMAutoRegisterCheckBox.setObjectName(u"importDICOMAutoRegisterCheckBox")
        self.importDICOMAutoRegisterCheckBox.setGeometry(QRect(430, 80, 141, 20))
        self.importDICOMAutoRegisterCheckBox.setFont(font)
        self.importDICOMRunButton = QPushButton(ImportDICOMPanelWidget)
        self.importDICOMRunButton.setObjectName(u"importDICOMRunButton")
        self.importDICOMRunButton.setGeometry(QRect(580, 100, 75, 24))
        self.importDICOMRunButton.setFont(font)

        self.retranslateUi(ImportDICOMPanelWidget)

        QMetaObject.connectSlotsByName(ImportDICOMPanelWidget)
    # setupUi

    def retranslateUi(self, ImportDICOMPanelWidget):
        ImportDICOMPanelWidget.setWindowTitle(QCoreApplication.translate("ImportDICOMPanelWidget", u"Form", None))
        self.importDICOMInstructionsTextEdit.setHtml(QCoreApplication.translate("ImportDICOMPanelWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:700;\">Import DICOM</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Select an input directory that contains the DICOM objects. That input directory and its subdirectories will be searched for DICOM objects that can be converted to images.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0;"
                        " text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Select an output directory for storing the converted images. A hierarchy of subdirectories will be automatically created that correspond to the &lt;PatientName&gt;/&lt;StudyID&gt;-&lt;StudyDescription&gt;-&lt;StudyDate&gt;/&lt;Modality&gt;/&lt;SeriesNumber&gt;-&lt;SeriesDescription&gt;-&lt;InstanceNumber&gt;.dcm</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Optionally, the data can be automatically registered with Minder3D and made available for one-click loading via the image browser table.</span></p></body></html>", None))
        self.importDICOMInputDirectoryLabel.setText(QCoreApplication.translate("ImportDICOMPanelWidget", u"Input Directory:", None))
        self.importDICOMInputDirectorySelectButton.setText(QCoreApplication.translate("ImportDICOMPanelWidget", u"...", None))
        self.importDICOMOutputDirectorySelectButton.setText(QCoreApplication.translate("ImportDICOMPanelWidget", u"...", None))
        self.importDICOMOutputDirectoryLabel.setText(QCoreApplication.translate("ImportDICOMPanelWidget", u"Output Directory:", None))
        self.importDICOMAutoRegisterCheckBox.setText(QCoreApplication.translate("ImportDICOMPanelWidget", u"Automatically register", None))
        self.importDICOMRunButton.setText(QCoreApplication.translate("ImportDICOMPanelWidget", u"Run", None))
    # retranslateUi

