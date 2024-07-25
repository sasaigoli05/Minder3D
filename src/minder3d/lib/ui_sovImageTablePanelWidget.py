# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovImageTablePanelWidgetQPMrUq.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_ImageTablePanelWidget(object):
    def setupUi(self, ImageTablePanelWidget):
        if not ImageTablePanelWidget.objectName():
            ImageTablePanelWidget.setObjectName(u"ImageTablePanelWidget")
        ImageTablePanelWidget.resize(448, 336)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ImageTablePanelWidget.sizePolicy().hasHeightForWidth())
        ImageTablePanelWidget.setSizePolicy(sizePolicy)
        ImageTablePanelWidget.setMinimumSize(QSize(190, 0))
        self.horizontalLayout = QHBoxLayout(ImageTablePanelWidget)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.imageTableWidget = QTableWidget(ImageTablePanelWidget)
        self.imageTableWidget.setObjectName(u"imageTableWidget")
        self.imageTableWidget.setAlternatingRowColors(True)
        self.imageTableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.imageTableWidget.horizontalHeader().setVisible(True)
        self.imageTableWidget.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.imageTableWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.imageTableLoadButton = QPushButton(ImageTablePanelWidget)
        self.imageTableLoadButton.setObjectName(u"imageTableLoadButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.imageTableLoadButton.sizePolicy().hasHeightForWidth())
        self.imageTableLoadButton.setSizePolicy(sizePolicy1)
        self.imageTableLoadButton.setMinimumSize(QSize(50, 0))
        font = QFont()
        font.setPointSize(7)
        self.imageTableLoadButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.imageTableLoadButton)

        self.imageTableUnloadButton = QPushButton(ImageTablePanelWidget)
        self.imageTableUnloadButton.setObjectName(u"imageTableUnloadButton")
        sizePolicy1.setHeightForWidth(self.imageTableUnloadButton.sizePolicy().hasHeightForWidth())
        self.imageTableUnloadButton.setSizePolicy(sizePolicy1)
        self.imageTableUnloadButton.setMinimumSize(QSize(50, 0))
        self.imageTableUnloadButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.imageTableUnloadButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.imageTableRenameButton = QPushButton(ImageTablePanelWidget)
        self.imageTableRenameButton.setObjectName(u"imageTableRenameButton")
        sizePolicy1.setHeightForWidth(self.imageTableRenameButton.sizePolicy().hasHeightForWidth())
        self.imageTableRenameButton.setSizePolicy(sizePolicy1)
        self.imageTableRenameButton.setMinimumSize(QSize(50, 0))
        self.imageTableRenameButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.imageTableRenameButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.imageTableRemoveButton = QPushButton(ImageTablePanelWidget)
        self.imageTableRemoveButton.setObjectName(u"imageTableRemoveButton")
        sizePolicy1.setHeightForWidth(self.imageTableRemoveButton.sizePolicy().hasHeightForWidth())
        self.imageTableRemoveButton.setSizePolicy(sizePolicy1)
        self.imageTableRemoveButton.setMinimumSize(QSize(50, 0))
        self.imageTableRemoveButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.imageTableRemoveButton)

        self.imageTableRemoveAllButton = QPushButton(ImageTablePanelWidget)
        self.imageTableRemoveAllButton.setObjectName(u"imageTableRemoveAllButton")
        sizePolicy1.setHeightForWidth(self.imageTableRemoveAllButton.sizePolicy().hasHeightForWidth())
        self.imageTableRemoveAllButton.setSizePolicy(sizePolicy1)
        self.imageTableRemoveAllButton.setMinimumSize(QSize(50, 0))
        self.imageTableRemoveAllButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.imageTableRemoveAllButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.imageTableExpandButton = QPushButton(ImageTablePanelWidget)
        self.imageTableExpandButton.setObjectName(u"imageTableExpandButton")
        sizePolicy1.setHeightForWidth(self.imageTableExpandButton.sizePolicy().hasHeightForWidth())
        self.imageTableExpandButton.setSizePolicy(sizePolicy1)
        self.imageTableExpandButton.setMinimumSize(QSize(23, 23))
        self.imageTableExpandButton.setMaximumSize(QSize(23, 23))
        font1 = QFont()
        font1.setPointSize(7)
        font1.setBold(True)
        self.imageTableExpandButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.imageTableExpandButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(ImageTablePanelWidget)

        QMetaObject.connectSlotsByName(ImageTablePanelWidget)
    # setupUi

    def retranslateUi(self, ImageTablePanelWidget):
        ImageTablePanelWidget.setWindowTitle(QCoreApplication.translate("ImageTablePanelWidget", u"Form", None))
        self.imageTableLoadButton.setText(QCoreApplication.translate("ImageTablePanelWidget", u"Load", None))
        self.imageTableUnloadButton.setText(QCoreApplication.translate("ImageTablePanelWidget", u"Unload", None))
        self.imageTableRenameButton.setText(QCoreApplication.translate("ImageTablePanelWidget", u"Rename", None))
        self.imageTableRemoveButton.setText(QCoreApplication.translate("ImageTablePanelWidget", u"Remove", None))
        self.imageTableRemoveAllButton.setText(QCoreApplication.translate("ImageTablePanelWidget", u"Remove All", None))
        self.imageTableExpandButton.setText(QCoreApplication.translate("ImageTablePanelWidget", u". . .", None))
    # retranslateUi

