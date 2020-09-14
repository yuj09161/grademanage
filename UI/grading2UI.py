# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'grading2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Grading2(object):
    def setupUi(self, Grading2):
        if not Grading2.objectName():
            Grading2.setObjectName(u"Grading2")
        Grading2.resize(358, 218)
        self.centralwidget = QWidget(Grading2)
        self.centralwidget.setObjectName(u"centralwidget")
        self.glMain = QGridLayout(self.centralwidget)
        self.glMain.setObjectName(u"glMain")
        self.lbSubject = QLabel(self.centralwidget)
        self.lbSubject.setObjectName(u"lbSubject")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbSubject.sizePolicy().hasHeightForWidth())
        self.lbSubject.setSizePolicy(sizePolicy)

        self.glMain.addWidget(self.lbSubject, 0, 0, 2, 1)

        self.lb11 = QLabel(self.centralwidget)
        self.lb11.setObjectName(u"lb11")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lb11.sizePolicy().hasHeightForWidth())
        self.lb11.setSizePolicy(sizePolicy1)
        self.lb11.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lb11, 0, 1, 1, 1)

        self.lb12 = QLabel(self.centralwidget)
        self.lb12.setObjectName(u"lb12")
        sizePolicy1.setHeightForWidth(self.lb12.sizePolicy().hasHeightForWidth())
        self.lb12.setSizePolicy(sizePolicy1)
        self.lb12.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lb12, 0, 2, 1, 1)

        self.lb13 = QLabel(self.centralwidget)
        self.lb13.setObjectName(u"lb13")
        sizePolicy1.setHeightForWidth(self.lb13.sizePolicy().hasHeightForWidth())
        self.lb13.setSizePolicy(sizePolicy1)
        self.lb13.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lb13, 0, 3, 1, 1)

        self.lb21 = QLabel(self.centralwidget)
        self.lb21.setObjectName(u"lb21")
        sizePolicy1.setHeightForWidth(self.lb21.sizePolicy().hasHeightForWidth())
        self.lb21.setSizePolicy(sizePolicy1)
        self.lb21.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lb21, 1, 1, 1, 1)

        self.lb22 = QLabel(self.centralwidget)
        self.lb22.setObjectName(u"lb22")
        sizePolicy1.setHeightForWidth(self.lb22.sizePolicy().hasHeightForWidth())
        self.lb22.setSizePolicy(sizePolicy1)
        self.lb22.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lb22, 1, 2, 1, 1)

        self.lb23 = QLabel(self.centralwidget)
        self.lb23.setObjectName(u"lb23")
        sizePolicy1.setHeightForWidth(self.lb23.sizePolicy().hasHeightForWidth())
        self.lb23.setSizePolicy(sizePolicy1)
        self.lb23.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lb23, 1, 3, 1, 1)

        self.lbAns = QLabel(self.centralwidget)
        self.lbAns.setObjectName(u"lbAns")
        sizePolicy.setHeightForWidth(self.lbAns.sizePolicy().hasHeightForWidth())
        self.lbAns.setSizePolicy(sizePolicy)

        self.glMain.addWidget(self.lbAns, 2, 0, 2, 1)

        self.lnAns11 = QLineEdit(self.centralwidget)
        self.lnAns11.setObjectName(u"lnAns11")
        sizePolicy.setHeightForWidth(self.lnAns11.sizePolicy().hasHeightForWidth())
        self.lnAns11.setSizePolicy(sizePolicy)
        self.lnAns11.setMaximumSize(QSize(100, 24))
        self.lnAns11.setStyleSheet(u"padding:16px")
        self.lnAns11.setMaxLength(9)
        self.lnAns11.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnAns11, 2, 1, 1, 1)

        self.lnAns12 = QLineEdit(self.centralwidget)
        self.lnAns12.setObjectName(u"lnAns12")
        sizePolicy.setHeightForWidth(self.lnAns12.sizePolicy().hasHeightForWidth())
        self.lnAns12.setSizePolicy(sizePolicy)
        self.lnAns12.setMaximumSize(QSize(100, 24))
        self.lnAns12.setStyleSheet(u"padding:16px")
        self.lnAns12.setMaxLength(9)
        self.lnAns12.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnAns12, 2, 2, 1, 1)

        self.lnAns13 = QLineEdit(self.centralwidget)
        self.lnAns13.setObjectName(u"lnAns13")
        sizePolicy.setHeightForWidth(self.lnAns13.sizePolicy().hasHeightForWidth())
        self.lnAns13.setSizePolicy(sizePolicy)
        self.lnAns13.setMaximumSize(QSize(100, 24))
        self.lnAns13.setStyleSheet(u"padding:16px")
        self.lnAns13.setMaxLength(9)
        self.lnAns13.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnAns13, 2, 3, 1, 1)

        self.lnAns21 = QLineEdit(self.centralwidget)
        self.lnAns21.setObjectName(u"lnAns21")
        sizePolicy.setHeightForWidth(self.lnAns21.sizePolicy().hasHeightForWidth())
        self.lnAns21.setSizePolicy(sizePolicy)
        self.lnAns21.setMaximumSize(QSize(100, 24))
        self.lnAns21.setStyleSheet(u"padding:16px")
        self.lnAns21.setMaxLength(9)
        self.lnAns21.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnAns21, 3, 1, 1, 1)

        self.lnAns22 = QLineEdit(self.centralwidget)
        self.lnAns22.setObjectName(u"lnAns22")
        sizePolicy.setHeightForWidth(self.lnAns22.sizePolicy().hasHeightForWidth())
        self.lnAns22.setSizePolicy(sizePolicy)
        self.lnAns22.setMaximumSize(QSize(100, 24))
        self.lnAns22.setStyleSheet(u"padding:16px")
        self.lnAns22.setMaxLength(9)
        self.lnAns22.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnAns22, 3, 2, 1, 1)

        self.lnAns23 = QLineEdit(self.centralwidget)
        self.lnAns23.setObjectName(u"lnAns23")
        sizePolicy.setHeightForWidth(self.lnAns23.sizePolicy().hasHeightForWidth())
        self.lnAns23.setSizePolicy(sizePolicy)
        self.lnAns23.setMaximumSize(QSize(100, 24))
        self.lnAns23.setStyleSheet(u"padding:16px")
        self.lnAns23.setMaxLength(9)
        self.lnAns23.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnAns23, 3, 3, 1, 1)

        self.lbCor = QLabel(self.centralwidget)
        self.lbCor.setObjectName(u"lbCor")
        sizePolicy.setHeightForWidth(self.lbCor.sizePolicy().hasHeightForWidth())
        self.lbCor.setSizePolicy(sizePolicy)

        self.glMain.addWidget(self.lbCor, 4, 0, 2, 1)

        self.lnCor11 = QLineEdit(self.centralwidget)
        self.lnCor11.setObjectName(u"lnCor11")
        sizePolicy.setHeightForWidth(self.lnCor11.sizePolicy().hasHeightForWidth())
        self.lnCor11.setSizePolicy(sizePolicy)
        self.lnCor11.setMaximumSize(QSize(100, 24))
        self.lnCor11.setStyleSheet(u"padding:16px")
        self.lnCor11.setMaxLength(9)
        self.lnCor11.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnCor11, 4, 1, 1, 1)

        self.lnCor12 = QLineEdit(self.centralwidget)
        self.lnCor12.setObjectName(u"lnCor12")
        sizePolicy.setHeightForWidth(self.lnCor12.sizePolicy().hasHeightForWidth())
        self.lnCor12.setSizePolicy(sizePolicy)
        self.lnCor12.setMaximumSize(QSize(100, 24))
        self.lnCor12.setStyleSheet(u"padding:16px")
        self.lnCor12.setMaxLength(9)
        self.lnCor12.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnCor12, 4, 2, 1, 1)

        self.lnCor13 = QLineEdit(self.centralwidget)
        self.lnCor13.setObjectName(u"lnCor13")
        sizePolicy.setHeightForWidth(self.lnCor13.sizePolicy().hasHeightForWidth())
        self.lnCor13.setSizePolicy(sizePolicy)
        self.lnCor13.setMaximumSize(QSize(100, 24))
        self.lnCor13.setStyleSheet(u"padding:16px")
        self.lnCor13.setMaxLength(9)
        self.lnCor13.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnCor13, 4, 3, 1, 1)

        self.lnCor21 = QLineEdit(self.centralwidget)
        self.lnCor21.setObjectName(u"lnCor21")
        sizePolicy.setHeightForWidth(self.lnCor21.sizePolicy().hasHeightForWidth())
        self.lnCor21.setSizePolicy(sizePolicy)
        self.lnCor21.setMaximumSize(QSize(100, 24))
        self.lnCor21.setStyleSheet(u"padding:16px")
        self.lnCor21.setMaxLength(9)
        self.lnCor21.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnCor21, 5, 1, 1, 1)

        self.lnCor22 = QLineEdit(self.centralwidget)
        self.lnCor22.setObjectName(u"lnCor22")
        sizePolicy.setHeightForWidth(self.lnCor22.sizePolicy().hasHeightForWidth())
        self.lnCor22.setSizePolicy(sizePolicy)
        self.lnCor22.setMaximumSize(QSize(100, 24))
        self.lnCor22.setStyleSheet(u"padding:16px")
        self.lnCor22.setMaxLength(9)
        self.lnCor22.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnCor22, 5, 2, 1, 1)

        self.lnCor23 = QLineEdit(self.centralwidget)
        self.lnCor23.setObjectName(u"lnCor23")
        sizePolicy.setHeightForWidth(self.lnCor23.sizePolicy().hasHeightForWidth())
        self.lnCor23.setSizePolicy(sizePolicy)
        self.lnCor23.setMaximumSize(QSize(100, 24))
        self.lnCor23.setStyleSheet(u"padding:16px")
        self.lnCor23.setMaxLength(9)
        self.lnCor23.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnCor23, 5, 3, 1, 1)

        self.widBot = QWidget(self.centralwidget)
        self.widBot.setObjectName(u"widBot")
        self.hlBot = QHBoxLayout(self.widBot)
        self.hlBot.setObjectName(u"hlBot")
        self.hlBot.setContentsMargins(0, 0, 0, 0)
        self.btnBack = QPushButton(self.widBot)
        self.btnBack.setObjectName(u"btnBack")
        sizePolicy.setHeightForWidth(self.btnBack.sizePolicy().hasHeightForWidth())
        self.btnBack.setSizePolicy(sizePolicy)

        self.hlBot.addWidget(self.btnBack)

        self.sp1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlBot.addItem(self.sp1)

        self.btnRe = QPushButton(self.widBot)
        self.btnRe.setObjectName(u"btnRe")
        sizePolicy.setHeightForWidth(self.btnRe.sizePolicy().hasHeightForWidth())
        self.btnRe.setSizePolicy(sizePolicy)

        self.hlBot.addWidget(self.btnRe)

        self.sp2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlBot.addItem(self.sp2)

        self.btnNext = QPushButton(self.widBot)
        self.btnNext.setObjectName(u"btnNext")
        sizePolicy.setHeightForWidth(self.btnNext.sizePolicy().hasHeightForWidth())
        self.btnNext.setSizePolicy(sizePolicy)

        self.hlBot.addWidget(self.btnNext)


        self.glMain.addWidget(self.widBot, 6, 0, 1, 4)

        Grading2.setCentralWidget(self.centralwidget)

        self.retranslateUi(Grading2)

        QMetaObject.connectSlotsByName(Grading2)
    # setupUi

    def retranslateUi(self, Grading2):
        Grading2.setWindowTitle(QCoreApplication.translate("Grading2", u"\uac00\ucc44\uc810\uc785\ub825", None))
        self.lbSubject.setText(QCoreApplication.translate("Grading2", u"\uacfc\n\ubaa9", None))
        self.lb11.setText(QCoreApplication.translate("Grading2", u"1~5", None))
        self.lb12.setText(QCoreApplication.translate("Grading2", u"6~10", None))
        self.lb13.setText(QCoreApplication.translate("Grading2", u"11~15", None))
        self.lb21.setText(QCoreApplication.translate("Grading2", u"16~20", None))
        self.lb22.setText(QCoreApplication.translate("Grading2", u"21~25", None))
        self.lb23.setText(QCoreApplication.translate("Grading2", u"26~30", None))
        self.lbAns.setText(QCoreApplication.translate("Grading2", u"\uc751\n\ub2f5", None))
        self.lnAns11.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnAns12.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnAns13.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnAns21.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnAns22.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnAns23.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lbCor.setText(QCoreApplication.translate("Grading2", u"\uc815\n\ub2f5", None))
        self.lnCor11.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnCor12.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnCor13.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnCor21.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnCor22.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnCor23.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.btnBack.setText(QCoreApplication.translate("Grading2", u"\uc774\uc804", None))
        self.btnRe.setText(QCoreApplication.translate("Grading2", u"\ub2e4\uc2dc", None))
        self.btnNext.setText(QCoreApplication.translate("Grading2", u"\ub2e4\uc74c", None))
    # retranslateUi

