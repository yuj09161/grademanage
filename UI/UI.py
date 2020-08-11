# -*- coding: utf-8 -*-

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_CutCalc(object):
    def setupUi(self, CutCalc):
        if not CutCalc.objectName():
            CutCalc.setObjectName(u"CutCalc")
        CutCalc.resize(208, 319)
        self.centralwidget = QWidget(CutCalc)
        self.centralwidget.setObjectName(u"centralwidget")
        self.glMain = QGridLayout(self.centralwidget)
        self.glMain.setObjectName(u"glMain")
        self.lbTitleCount = QLabel(self.centralwidget)
        self.lbTitleCount.setObjectName(u"lbTitleCount")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbTitleCount.sizePolicy().hasHeightForWidth())
        self.lbTitleCount.setSizePolicy(sizePolicy)
        self.lbTitleCount.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbTitleCount, 0, 0, 1, 1)

        self.lnPerson = QLineEdit(self.centralwidget)
        self.lnPerson.setObjectName(u"lnPerson")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lnPerson.sizePolicy().hasHeightForWidth())
        self.lnPerson.setSizePolicy(sizePolicy1)
        self.lnPerson.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnPerson, 0, 1, 1, 2)

        self.lbTitleGrade = QLabel(self.centralwidget)
        self.lbTitleGrade.setObjectName(u"lbTitleGrade")
        sizePolicy.setHeightForWidth(self.lbTitleGrade.sizePolicy().hasHeightForWidth())
        self.lbTitleGrade.setSizePolicy(sizePolicy)
        self.lbTitleGrade.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbTitleGrade, 1, 0, 1, 1)

        self.lbTitleRatio = QLabel(self.centralwidget)
        self.lbTitleRatio.setObjectName(u"lbTitleRatio")
        sizePolicy.setHeightForWidth(self.lbTitleRatio.sizePolicy().hasHeightForWidth())
        self.lbTitleRatio.setSizePolicy(sizePolicy)
        self.lbTitleRatio.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbTitleRatio, 1, 1, 1, 1)

        self.lbCut_2 = QLabel(self.centralwidget)
        self.lbCut_2.setObjectName(u"lbCut_2")
        sizePolicy.setHeightForWidth(self.lbCut_2.sizePolicy().hasHeightForWidth())
        self.lbCut_2.setSizePolicy(sizePolicy)
        self.lbCut_2.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbCut_2, 1, 2, 1, 1)

        self.lbGrade1 = QLabel(self.centralwidget)
        self.lbGrade1.setObjectName(u"lbGrade1")
        sizePolicy.setHeightForWidth(self.lbGrade1.sizePolicy().hasHeightForWidth())
        self.lbGrade1.setSizePolicy(sizePolicy)
        self.lbGrade1.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbGrade1, 2, 0, 1, 1)

        self.lbRatio1 = QLabel(self.centralwidget)
        self.lbRatio1.setObjectName(u"lbRatio1")
        sizePolicy.setHeightForWidth(self.lbRatio1.sizePolicy().hasHeightForWidth())
        self.lbRatio1.setSizePolicy(sizePolicy)
        self.lbRatio1.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbRatio1, 2, 1, 1, 1)

        self.lbCut1 = QLabel(self.centralwidget)
        self.lbCut1.setObjectName(u"lbCut1")
        sizePolicy.setHeightForWidth(self.lbCut1.sizePolicy().hasHeightForWidth())
        self.lbCut1.setSizePolicy(sizePolicy)
        self.lbCut1.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbCut1, 2, 2, 1, 1)

        self.lbGrade2 = QLabel(self.centralwidget)
        self.lbGrade2.setObjectName(u"lbGrade2")
        sizePolicy.setHeightForWidth(self.lbGrade2.sizePolicy().hasHeightForWidth())
        self.lbGrade2.setSizePolicy(sizePolicy)
        self.lbGrade2.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbGrade2, 3, 0, 1, 1)

        self.lbRatio2 = QLabel(self.centralwidget)
        self.lbRatio2.setObjectName(u"lbRatio2")
        sizePolicy.setHeightForWidth(self.lbRatio2.sizePolicy().hasHeightForWidth())
        self.lbRatio2.setSizePolicy(sizePolicy)
        self.lbRatio2.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbRatio2, 3, 1, 1, 1)

        self.lbCut2 = QLabel(self.centralwidget)
        self.lbCut2.setObjectName(u"lbCut2")
        sizePolicy.setHeightForWidth(self.lbCut2.sizePolicy().hasHeightForWidth())
        self.lbCut2.setSizePolicy(sizePolicy)
        self.lbCut2.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbCut2, 3, 2, 1, 1)

        self.lbGrade3 = QLabel(self.centralwidget)
        self.lbGrade3.setObjectName(u"lbGrade3")
        sizePolicy.setHeightForWidth(self.lbGrade3.sizePolicy().hasHeightForWidth())
        self.lbGrade3.setSizePolicy(sizePolicy)
        self.lbGrade3.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbGrade3, 4, 0, 1, 1)

        self.lbRatio3 = QLabel(self.centralwidget)
        self.lbRatio3.setObjectName(u"lbRatio3")
        sizePolicy.setHeightForWidth(self.lbRatio3.sizePolicy().hasHeightForWidth())
        self.lbRatio3.setSizePolicy(sizePolicy)
        self.lbRatio3.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbRatio3, 4, 1, 1, 1)

        self.lbCut3 = QLabel(self.centralwidget)
        self.lbCut3.setObjectName(u"lbCut3")
        sizePolicy.setHeightForWidth(self.lbCut3.sizePolicy().hasHeightForWidth())
        self.lbCut3.setSizePolicy(sizePolicy)
        self.lbCut3.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbCut3, 4, 2, 1, 1)

        self.lbGrade4 = QLabel(self.centralwidget)
        self.lbGrade4.setObjectName(u"lbGrade4")
        sizePolicy.setHeightForWidth(self.lbGrade4.sizePolicy().hasHeightForWidth())
        self.lbGrade4.setSizePolicy(sizePolicy)
        self.lbGrade4.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbGrade4, 5, 0, 1, 1)

        self.lbRatio4 = QLabel(self.centralwidget)
        self.lbRatio4.setObjectName(u"lbRatio4")
        sizePolicy.setHeightForWidth(self.lbRatio4.sizePolicy().hasHeightForWidth())
        self.lbRatio4.setSizePolicy(sizePolicy)
        self.lbRatio4.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbRatio4, 5, 1, 1, 1)

        self.lbCut4 = QLabel(self.centralwidget)
        self.lbCut4.setObjectName(u"lbCut4")
        sizePolicy.setHeightForWidth(self.lbCut4.sizePolicy().hasHeightForWidth())
        self.lbCut4.setSizePolicy(sizePolicy)
        self.lbCut4.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbCut4, 5, 2, 1, 1)

        self.lbGrade5 = QLabel(self.centralwidget)
        self.lbGrade5.setObjectName(u"lbGrade5")
        sizePolicy.setHeightForWidth(self.lbGrade5.sizePolicy().hasHeightForWidth())
        self.lbGrade5.setSizePolicy(sizePolicy)
        self.lbGrade5.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbGrade5, 6, 0, 1, 1)

        self.lbRatio5 = QLabel(self.centralwidget)
        self.lbRatio5.setObjectName(u"lbRatio5")
        sizePolicy.setHeightForWidth(self.lbRatio5.sizePolicy().hasHeightForWidth())
        self.lbRatio5.setSizePolicy(sizePolicy)
        self.lbRatio5.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbRatio5, 6, 1, 1, 1)

        self.lbCut5 = QLabel(self.centralwidget)
        self.lbCut5.setObjectName(u"lbCut5")
        sizePolicy.setHeightForWidth(self.lbCut5.sizePolicy().hasHeightForWidth())
        self.lbCut5.setSizePolicy(sizePolicy)
        self.lbCut5.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbCut5, 6, 2, 1, 1)

        self.lbGrade6 = QLabel(self.centralwidget)
        self.lbGrade6.setObjectName(u"lbGrade6")
        sizePolicy.setHeightForWidth(self.lbGrade6.sizePolicy().hasHeightForWidth())
        self.lbGrade6.setSizePolicy(sizePolicy)
        self.lbGrade6.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbGrade6, 7, 0, 1, 1)

        self.lbRatio6 = QLabel(self.centralwidget)
        self.lbRatio6.setObjectName(u"lbRatio6")
        sizePolicy.setHeightForWidth(self.lbRatio6.sizePolicy().hasHeightForWidth())
        self.lbRatio6.setSizePolicy(sizePolicy)
        self.lbRatio6.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbRatio6, 7, 1, 1, 1)

        self.lbCut6 = QLabel(self.centralwidget)
        self.lbCut6.setObjectName(u"lbCut6")
        sizePolicy.setHeightForWidth(self.lbCut6.sizePolicy().hasHeightForWidth())
        self.lbCut6.setSizePolicy(sizePolicy)
        self.lbCut6.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbCut6, 7, 2, 1, 1)

        self.lbGrade7 = QLabel(self.centralwidget)
        self.lbGrade7.setObjectName(u"lbGrade7")
        sizePolicy.setHeightForWidth(self.lbGrade7.sizePolicy().hasHeightForWidth())
        self.lbGrade7.setSizePolicy(sizePolicy)
        self.lbGrade7.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbGrade7, 8, 0, 1, 1)

        self.lbRatio7 = QLabel(self.centralwidget)
        self.lbRatio7.setObjectName(u"lbRatio7")
        sizePolicy.setHeightForWidth(self.lbRatio7.sizePolicy().hasHeightForWidth())
        self.lbRatio7.setSizePolicy(sizePolicy)
        self.lbRatio7.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbRatio7, 8, 1, 1, 1)

        self.lbCut7 = QLabel(self.centralwidget)
        self.lbCut7.setObjectName(u"lbCut7")
        sizePolicy.setHeightForWidth(self.lbCut7.sizePolicy().hasHeightForWidth())
        self.lbCut7.setSizePolicy(sizePolicy)
        self.lbCut7.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbCut7, 8, 2, 1, 1)

        self.lbGrade8 = QLabel(self.centralwidget)
        self.lbGrade8.setObjectName(u"lbGrade8")
        sizePolicy.setHeightForWidth(self.lbGrade8.sizePolicy().hasHeightForWidth())
        self.lbGrade8.setSizePolicy(sizePolicy)
        self.lbGrade8.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbGrade8, 9, 0, 1, 1)

        self.lbRatio8 = QLabel(self.centralwidget)
        self.lbRatio8.setObjectName(u"lbRatio8")
        sizePolicy.setHeightForWidth(self.lbRatio8.sizePolicy().hasHeightForWidth())
        self.lbRatio8.setSizePolicy(sizePolicy)
        self.lbRatio8.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbRatio8, 9, 1, 1, 1)

        self.lbCut8 = QLabel(self.centralwidget)
        self.lbCut8.setObjectName(u"lbCut8")
        sizePolicy.setHeightForWidth(self.lbCut8.sizePolicy().hasHeightForWidth())
        self.lbCut8.setSizePolicy(sizePolicy)
        self.lbCut8.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbCut8, 9, 2, 1, 1)

        self.lbGrade9 = QLabel(self.centralwidget)
        self.lbGrade9.setObjectName(u"lbGrade9")
        sizePolicy.setHeightForWidth(self.lbGrade9.sizePolicy().hasHeightForWidth())
        self.lbGrade9.setSizePolicy(sizePolicy)
        self.lbGrade9.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbGrade9, 10, 0, 1, 1)

        self.lbRatio9 = QLabel(self.centralwidget)
        self.lbRatio9.setObjectName(u"lbRatio9")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lbRatio9.sizePolicy().hasHeightForWidth())
        self.lbRatio9.setSizePolicy(sizePolicy2)
        self.lbRatio9.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbRatio9, 10, 1, 1, 1)

        self.lbCut9 = QLabel(self.centralwidget)
        self.lbCut9.setObjectName(u"lbCut9")
        sizePolicy.setHeightForWidth(self.lbCut9.sizePolicy().hasHeightForWidth())
        self.lbCut9.setSizePolicy(sizePolicy)
        self.lbCut9.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbCut9, 10, 2, 1, 1)

        self.widBot = QWidget(self.centralwidget)
        self.widBot.setObjectName(u"widBot")
        self.hlBot = QHBoxLayout(self.widBot)
        self.hlBot.setSpacing(0)
        self.hlBot.setObjectName(u"hlBot")
        self.hlBot.setContentsMargins(0, 0, 0, 0)
        self.btnClose = QPushButton(self.widBot)
        self.btnClose.setObjectName(u"btnClose")

        self.hlBot.addWidget(self.btnClose)

        self.sp = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlBot.addItem(self.sp)

        self.btnCalc = QPushButton(self.widBot)
        self.btnCalc.setObjectName(u"btnCalc")

        self.hlBot.addWidget(self.btnCalc)


        self.glMain.addWidget(self.widBot, 11, 0, 1, 3)

        CutCalc.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.lnPerson, self.btnClose)
        QWidget.setTabOrder(self.btnClose, self.btnCalc)

        self.retranslateUi(CutCalc)

        QMetaObject.connectSlotsByName(CutCalc)
    # setupUi

    def retranslateUi(self, CutCalc):
        CutCalc.setWindowTitle(QCoreApplication.translate("CutCalc", u"\ub4f1\uae09\ucef7 \uacc4\uc0b0", None))
        self.lbTitleCount.setText(QCoreApplication.translate("CutCalc", u"\uc778\uc6d0", None))
        self.lnPerson.setInputMask(QCoreApplication.translate("CutCalc", u"Ddd", None))
        self.lbTitleGrade.setText(QCoreApplication.translate("CutCalc", u"\ub4f1\uae09", None))
        self.lbTitleRatio.setText(QCoreApplication.translate("CutCalc", u"\ube44\uc728", None))
        self.lbCut_2.setText(QCoreApplication.translate("CutCalc", u"\uc778\uc6d0\uc218", None))
        self.lbGrade1.setText(QCoreApplication.translate("CutCalc", u"1", None))
        self.lbRatio1.setText("")
        self.lbGrade2.setText(QCoreApplication.translate("CutCalc", u"2", None))
        self.lbGrade3.setText(QCoreApplication.translate("CutCalc", u"3", None))
        self.lbGrade4.setText(QCoreApplication.translate("CutCalc", u"4", None))
        self.lbGrade5.setText(QCoreApplication.translate("CutCalc", u"5", None))
        self.lbGrade6.setText(QCoreApplication.translate("CutCalc", u"6", None))
        self.lbGrade7.setText(QCoreApplication.translate("CutCalc", u"7", None))
        self.lbGrade8.setText(QCoreApplication.translate("CutCalc", u"8", None))
        self.lbGrade9.setText(QCoreApplication.translate("CutCalc", u"9", None))
        self.lbRatio9.setText(QCoreApplication.translate("CutCalc", u"100%", None))
        self.btnClose.setText(QCoreApplication.translate("CutCalc", u"\ub2eb\uae30", None))
        self.btnCalc.setText(QCoreApplication.translate("CutCalc", u"\uacc4\uc0b0", None))
    # retranslateUi

class Ui_ExamInput(object):
    def setupUi(self, ExamInput):
        if not ExamInput.objectName():
            ExamInput.setObjectName(u"ExamInput")
        ExamInput.resize(389, 107)
        self.centralwidget = QWidget(ExamInput)
        self.centralwidget.setObjectName(u"centralwidget")
        self.glMain = QGridLayout(self.centralwidget)
        self.glMain.setObjectName(u"glMain")
        self.lbTitleSubject = QLabel(self.centralwidget)
        self.lbTitleSubject.setObjectName(u"lbTitleSubject")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbTitleSubject.sizePolicy().hasHeightForWidth())
        self.lbTitleSubject.setSizePolicy(sizePolicy)
        self.lbTitleSubject.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbTitleSubject, 0, 0, 1, 1)

        self.lnScore = QLineEdit(self.centralwidget)
        self.lnScore.setObjectName(u"lnScore")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lnScore.sizePolicy().hasHeightForWidth())
        self.lnScore.setSizePolicy(sizePolicy1)
        self.lnScore.setMaximumSize(QSize(60, 16777215))
        self.lnScore.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnScore, 1, 2, 1, 1)

        self.lbGrade = QLabel(self.centralwidget)
        self.lbGrade.setObjectName(u"lbGrade")
        sizePolicy.setHeightForWidth(self.lbGrade.sizePolicy().hasHeightForWidth())
        self.lbGrade.setSizePolicy(sizePolicy)
        self.lbGrade.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbGrade, 1, 1, 1, 1)

        self.lbTitleScore = QLabel(self.centralwidget)
        self.lbTitleScore.setObjectName(u"lbTitleScore")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lbTitleScore.sizePolicy().hasHeightForWidth())
        self.lbTitleScore.setSizePolicy(sizePolicy2)
        self.lbTitleScore.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbTitleScore, 0, 2, 1, 1, Qt.AlignHCenter)

        self.lbSubject = QLabel(self.centralwidget)
        self.lbSubject.setObjectName(u"lbSubject")
        sizePolicy.setHeightForWidth(self.lbSubject.sizePolicy().hasHeightForWidth())
        self.lbSubject.setSizePolicy(sizePolicy)
        self.lbSubject.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbSubject, 1, 0, 1, 1)

        self.lnRank = QLineEdit(self.centralwidget)
        self.lnRank.setObjectName(u"lnRank")
        sizePolicy1.setHeightForWidth(self.lnRank.sizePolicy().hasHeightForWidth())
        self.lnRank.setSizePolicy(sizePolicy1)
        self.lnRank.setMaximumSize(QSize(60, 16777215))
        self.lnRank.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnRank, 1, 3, 1, 1)

        self.lnPerson = QLineEdit(self.centralwidget)
        self.lnPerson.setObjectName(u"lnPerson")
        sizePolicy1.setHeightForWidth(self.lnPerson.sizePolicy().hasHeightForWidth())
        self.lnPerson.setSizePolicy(sizePolicy1)
        self.lnPerson.setMaximumSize(QSize(60, 16777215))
        self.lnPerson.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnPerson, 1, 4, 1, 1)

        self.lbTitleNum = QLabel(self.centralwidget)
        self.lbTitleNum.setObjectName(u"lbTitleNum")
        sizePolicy.setHeightForWidth(self.lbTitleNum.sizePolicy().hasHeightForWidth())
        self.lbTitleNum.setSizePolicy(sizePolicy)
        self.lbTitleNum.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbTitleNum, 0, 1, 1, 1)

        self.lbTitlePerson = QLabel(self.centralwidget)
        self.lbTitlePerson.setObjectName(u"lbTitlePerson")
        sizePolicy2.setHeightForWidth(self.lbTitlePerson.sizePolicy().hasHeightForWidth())
        self.lbTitlePerson.setSizePolicy(sizePolicy2)
        self.lbTitlePerson.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbTitlePerson, 0, 4, 1, 1, Qt.AlignHCenter)

        self.lbTitleRank = QLabel(self.centralwidget)
        self.lbTitleRank.setObjectName(u"lbTitleRank")
        sizePolicy2.setHeightForWidth(self.lbTitleRank.sizePolicy().hasHeightForWidth())
        self.lbTitleRank.setSizePolicy(sizePolicy2)
        self.lbTitleRank.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbTitleRank, 0, 3, 1, 1, Qt.AlignHCenter)

        self.btnDel = QPushButton(self.centralwidget)
        self.btnDel.setObjectName(u"btnDel")
        sizePolicy1.setHeightForWidth(self.btnDel.sizePolicy().hasHeightForWidth())
        self.btnDel.setSizePolicy(sizePolicy1)
        self.btnDel.setMaximumSize(QSize(28, 16777215))

        self.glMain.addWidget(self.btnDel, 1, 5, 1, 1, Qt.AlignHCenter)

        self.lbTitleDel = QLabel(self.centralwidget)
        self.lbTitleDel.setObjectName(u"lbTitleDel")
        sizePolicy2.setHeightForWidth(self.lbTitleDel.sizePolicy().hasHeightForWidth())
        self.lbTitleDel.setSizePolicy(sizePolicy2)
        self.lbTitleDel.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbTitleDel, 0, 5, 1, 1)

        self.widBot = QWidget(self.centralwidget)
        self.widBot.setObjectName(u"widBot")
        self.horizontalLayout = QHBoxLayout(self.widBot)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnAdd = QPushButton(self.widBot)
        self.btnAdd.setObjectName(u"btnAdd")
        sizePolicy1.setHeightForWidth(self.btnAdd.sizePolicy().hasHeightForWidth())
        self.btnAdd.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.btnAdd)

        self.spH = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.spH)

        self.btnCancel = QPushButton(self.widBot)
        self.btnCancel.setObjectName(u"btnCancel")
        sizePolicy1.setHeightForWidth(self.btnCancel.sizePolicy().hasHeightForWidth())
        self.btnCancel.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.btnCancel)

        self.btnSet = QPushButton(self.widBot)
        self.btnSet.setObjectName(u"btnSet")
        sizePolicy1.setHeightForWidth(self.btnSet.sizePolicy().hasHeightForWidth())
        self.btnSet.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.btnSet)


        self.glMain.addWidget(self.widBot, 2, 0, 1, 6)

        ExamInput.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.lnScore, self.lnRank)
        QWidget.setTabOrder(self.lnRank, self.lnPerson)
        QWidget.setTabOrder(self.lnPerson, self.btnDel)
        QWidget.setTabOrder(self.btnDel, self.btnAdd)
        QWidget.setTabOrder(self.btnAdd, self.btnCancel)
        QWidget.setTabOrder(self.btnCancel, self.btnSet)

        self.retranslateUi(ExamInput)

        QMetaObject.connectSlotsByName(ExamInput)
    # setupUi

    def retranslateUi(self, ExamInput):
        ExamInput.setWindowTitle(QCoreApplication.translate("ExamInput", u"(\ucd5c\uc885)\uc131\uc801\uc785\ub825", None))
        self.lbTitleSubject.setText(QCoreApplication.translate("ExamInput", u"\uacfc\ubaa9\uba85", None))
        self.lnScore.setInputMask(QCoreApplication.translate("ExamInput", u"Ddd", None))
        self.lbGrade.setText(QCoreApplication.translate("ExamInput", u"1", None))
        self.lbTitleScore.setText(QCoreApplication.translate("ExamInput", u"\uc6d0\uc810\uc218", None))
        self.lbSubject.setText(QCoreApplication.translate("ExamInput", u"\uac00\ub098\ub2e4", None))
        self.lnRank.setInputMask(QCoreApplication.translate("ExamInput", u"Ddd", None))
        self.lnPerson.setInputMask(QCoreApplication.translate("ExamInput", u"Ddd", None))
        self.lbTitleNum.setText(QCoreApplication.translate("ExamInput", u"\ub2e8\uc704\uc218", None))
        self.lbTitlePerson.setText(QCoreApplication.translate("ExamInput", u"\uc218\uac15\uc778\uc6d0", None))
        self.lbTitleRank.setText(QCoreApplication.translate("ExamInput", u"\uc11d\ucc28", None))
        self.btnDel.setText(QCoreApplication.translate("ExamInput", u"X", None))
        self.lbTitleDel.setText(QCoreApplication.translate("ExamInput", u"\uc0ad\uc81c", None))
        self.btnAdd.setText(QCoreApplication.translate("ExamInput", u"\ucd08\uae30\ud654", None))
        self.btnCancel.setText(QCoreApplication.translate("ExamInput", u"\ucde8\uc18c", None))
        self.btnSet.setText(QCoreApplication.translate("ExamInput", u"\uc785\ub825", None))
    # retranslateUi

class Ui_ExamResult(object):
    def setupUi(self, ExamResult):
        if not ExamResult.objectName():
            ExamResult.setObjectName(u"ExamResult")
        ExamResult.resize(252, 72)
        self.centralwidget = QWidget(ExamResult)
        self.centralwidget.setObjectName(u"centralwidget")
        self.glMain = QGridLayout(self.centralwidget)
        self.glMain.setObjectName(u"glMain")
        self.lbTitleNum = QLabel(self.centralwidget)
        self.lbTitleNum.setObjectName(u"lbTitleNum")

        self.glMain.addWidget(self.lbTitleNum, 0, 1, 1, 1)

        self.lbTitleGrade = QLabel(self.centralwidget)
        self.lbTitleGrade.setObjectName(u"lbTitleGrade")

        self.glMain.addWidget(self.lbTitleGrade, 0, 4, 1, 1)

        self.lbTitleScore = QLabel(self.centralwidget)
        self.lbTitleScore.setObjectName(u"lbTitleScore")

        self.glMain.addWidget(self.lbTitleScore, 0, 2, 1, 1)

        self.lbTitleRank = QLabel(self.centralwidget)
        self.lbTitleRank.setObjectName(u"lbTitleRank")

        self.glMain.addWidget(self.lbTitleRank, 0, 3, 1, 1)

        self.lbTitleSubject = QLabel(self.centralwidget)
        self.lbTitleSubject.setObjectName(u"lbTitleSubject")

        self.glMain.addWidget(self.lbTitleSubject, 0, 0, 1, 1)

        self.lbTitlePercent = QLabel(self.centralwidget)
        self.lbTitlePercent.setObjectName(u"lbTitlePercent")

        self.glMain.addWidget(self.lbTitlePercent, 0, 5, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.hlBot = QHBoxLayout(self.widget)
        self.hlBot.setObjectName(u"hlBot")
        self.hlBot.setContentsMargins(0, 0, 0, 0)
        self.sp = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlBot.addItem(self.sp)

        self.btnClose = QPushButton(self.widget)
        self.btnClose.setObjectName(u"btnClose")

        self.hlBot.addWidget(self.btnClose)


        self.glMain.addWidget(self.widget, 1, 0, 1, 6)

        ExamResult.setCentralWidget(self.centralwidget)

        self.retranslateUi(ExamResult)

        QMetaObject.connectSlotsByName(ExamResult)
    # setupUi

    def retranslateUi(self, ExamResult):
        ExamResult.setWindowTitle(QCoreApplication.translate("ExamResult", u"\uc2dc\ud5d8\uacb0\uacfc", None))
        self.lbTitleNum.setText(QCoreApplication.translate("ExamResult", u"\uc2dc\uc218", None))
        self.lbTitleGrade.setText(QCoreApplication.translate("ExamResult", u"\ub4f1\uae09", None))
        self.lbTitleScore.setText(QCoreApplication.translate("ExamResult", u"\uc810\uc218", None))
        self.lbTitleRank.setText(QCoreApplication.translate("ExamResult", u"\uc11d\ucc28", None))
        self.lbTitleSubject.setText(QCoreApplication.translate("ExamResult", u"\uacfc\ubaa9", None))
        self.lbTitlePercent.setText(QCoreApplication.translate("ExamResult", u"\ubc31\ubd84\uc704", None))
        self.btnClose.setText(QCoreApplication.translate("ExamResult", u"\ub2eb\uae30", None))
    # retranslateUi

class Ui_GradeCalc(object):
    def setupUi(self, GradeCalc):
        if not GradeCalc.objectName():
            GradeCalc.setObjectName(u"GradeCalc")
        GradeCalc.resize(333, 103)
        self.centralwidget = QWidget(GradeCalc)
        self.centralwidget.setObjectName(u"centralwidget")
        self.glMain = QGridLayout(self.centralwidget)
        self.glMain.setObjectName(u"glMain")
        self.lnGrade2 = QLineEdit(self.centralwidget)
        self.lnGrade2.setObjectName(u"lnGrade2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnGrade2.sizePolicy().hasHeightForWidth())
        self.lnGrade2.setSizePolicy(sizePolicy)
        self.lnGrade2.setMaximumSize(QSize(100, 16777215))
        self.lnGrade2.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnGrade2, 1, 3, 1, 1)

        self.lbTitleGrade1 = QLabel(self.centralwidget)
        self.lbTitleGrade1.setObjectName(u"lbTitleGrade1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbTitleGrade1.sizePolicy().hasHeightForWidth())
        self.lbTitleGrade1.setSizePolicy(sizePolicy1)
        self.lbTitleGrade1.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbTitleGrade1, 0, 2, 1, 1, Qt.AlignHCenter)

        self.lnGrade1 = QLineEdit(self.centralwidget)
        self.lnGrade1.setObjectName(u"lnGrade1")
        sizePolicy.setHeightForWidth(self.lnGrade1.sizePolicy().hasHeightForWidth())
        self.lnGrade1.setSizePolicy(sizePolicy)
        self.lnGrade1.setMaximumSize(QSize(100, 16777215))
        self.lnGrade1.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnGrade1, 1, 2, 1, 1)

        self.lbSubject = QLabel(self.centralwidget)
        self.lbSubject.setObjectName(u"lbSubject")
        sizePolicy1.setHeightForWidth(self.lbSubject.sizePolicy().hasHeightForWidth())
        self.lbSubject.setSizePolicy(sizePolicy1)
        self.lbSubject.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbSubject, 1, 0, 1, 1)

        self.lbTitleSubject = QLabel(self.centralwidget)
        self.lbTitleSubject.setObjectName(u"lbTitleSubject")
        sizePolicy1.setHeightForWidth(self.lbTitleSubject.sizePolicy().hasHeightForWidth())
        self.lbTitleSubject.setSizePolicy(sizePolicy1)
        self.lbTitleSubject.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbTitleSubject, 0, 0, 1, 1)

        self.lbTitleGrade2 = QLabel(self.centralwidget)
        self.lbTitleGrade2.setObjectName(u"lbTitleGrade2")
        sizePolicy1.setHeightForWidth(self.lbTitleGrade2.sizePolicy().hasHeightForWidth())
        self.lbTitleGrade2.setSizePolicy(sizePolicy1)
        self.lbTitleGrade2.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbTitleGrade2, 0, 3, 1, 1, Qt.AlignHCenter)

        self.widBot = QWidget(self.centralwidget)
        self.widBot.setObjectName(u"widBot")
        self.hlBot = QHBoxLayout(self.widBot)
        self.hlBot.setSpacing(0)
        self.hlBot.setObjectName(u"hlBot")
        self.hlBot.setContentsMargins(0, 0, 0, 0)
        self.btnAdd = QPushButton(self.widBot)
        self.btnAdd.setObjectName(u"btnAdd")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnAdd.sizePolicy().hasHeightForWidth())
        self.btnAdd.setSizePolicy(sizePolicy2)

        self.hlBot.addWidget(self.btnAdd)

        self.spH = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlBot.addItem(self.spH)

        self.btnCancel = QPushButton(self.widBot)
        self.btnCancel.setObjectName(u"btnCancel")
        sizePolicy2.setHeightForWidth(self.btnCancel.sizePolicy().hasHeightForWidth())
        self.btnCancel.setSizePolicy(sizePolicy2)

        self.hlBot.addWidget(self.btnCancel)

        self.btnSet = QPushButton(self.widBot)
        self.btnSet.setObjectName(u"btnSet")
        sizePolicy2.setHeightForWidth(self.btnSet.sizePolicy().hasHeightForWidth())
        self.btnSet.setSizePolicy(sizePolicy2)

        self.hlBot.addWidget(self.btnSet)


        self.glMain.addWidget(self.widBot, 2, 0, 1, 4)

        self.lbNum = QLabel(self.centralwidget)
        self.lbNum.setObjectName(u"lbNum")
        sizePolicy3 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lbNum.sizePolicy().hasHeightForWidth())
        self.lbNum.setSizePolicy(sizePolicy3)
        self.lbNum.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbNum, 1, 1, 1, 1)

        self.lbTitleNum = QLabel(self.centralwidget)
        self.lbTitleNum.setObjectName(u"lbTitleNum")
        sizePolicy1.setHeightForWidth(self.lbTitleNum.sizePolicy().hasHeightForWidth())
        self.lbTitleNum.setSizePolicy(sizePolicy1)
        self.lbTitleNum.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbTitleNum, 0, 1, 1, 1)

        GradeCalc.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.lnGrade1, self.lnGrade2)
        QWidget.setTabOrder(self.lnGrade2, self.btnAdd)
        QWidget.setTabOrder(self.btnAdd, self.btnCancel)
        QWidget.setTabOrder(self.btnCancel, self.btnSet)

        self.retranslateUi(GradeCalc)

        QMetaObject.connectSlotsByName(GradeCalc)
    # setupUi

    def retranslateUi(self, GradeCalc):
        GradeCalc.setWindowTitle(QCoreApplication.translate("GradeCalc", u"\uc608\uc0c1\ub4f1\uae09\uacc4\uc0b0", None))
        self.lnGrade2.setInputMask(QCoreApplication.translate("GradeCalc", u"d", None))
        self.lbTitleGrade1.setText(QCoreApplication.translate("GradeCalc", u"\ub4f1\uae091", None))
        self.lnGrade1.setInputMask(QCoreApplication.translate("GradeCalc", u"D", None))
        self.lbSubject.setText(QCoreApplication.translate("GradeCalc", u"\uac00\ub098\ub2e4", None))
        self.lbTitleSubject.setText(QCoreApplication.translate("GradeCalc", u"\uacfc\ubaa9\uba85", None))
        self.lbTitleGrade2.setText(QCoreApplication.translate("GradeCalc", u"\ub4f1\uae092", None))
        self.btnAdd.setText(QCoreApplication.translate("GradeCalc", u"\uc778\uc6d0\uacc4\uc0b0", None))
        self.btnCancel.setText(QCoreApplication.translate("GradeCalc", u"\ucd08\uae30\ud654", None))
        self.btnSet.setText(QCoreApplication.translate("GradeCalc", u"\ub2eb\uae30", None))
        self.lbNum.setText(QCoreApplication.translate("GradeCalc", u"1", None))
        self.lbTitleNum.setText(QCoreApplication.translate("GradeCalc", u"\ub2e8\uc704\uc218", None))
    # retranslateUi

class Ui_GradDetail(object):
    def setupUi(self, GradDetail):
        if not GradDetail.objectName():
            GradDetail.setObjectName(u"GradDetail")
        GradDetail.resize(207, 274)
        self.centralwidget = QWidget(GradDetail)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widSupply = QWidget(self.centralwidget)
        self.widSupply.setObjectName(u"widSupply")
        self.gridLayout = QGridLayout(self.widSupply)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbTitle2Get = QLabel(self.widSupply)
        self.lbTitle2Get.setObjectName(u"lbTitle2Get")
        self.lbTitle2Get.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbTitle2Get, 0, 2, 1, 1)

        self.lbTitle2Num = QLabel(self.widSupply)
        self.lbTitle2Num.setObjectName(u"lbTitle2Num")
        self.lbTitle2Num.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbTitle2Num, 0, 1, 1, 1)

        self.lbTitle2Score = QLabel(self.widSupply)
        self.lbTitle2Score.setObjectName(u"lbTitle2Score")
        self.lbTitle2Score.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbTitle2Score, 0, 3, 1, 1)

        self.lbTitleSupply = QLabel(self.widSupply)
        self.lbTitleSupply.setObjectName(u"lbTitleSupply")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbTitleSupply.sizePolicy().hasHeightForWidth())
        self.lbTitleSupply.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.lbTitleSupply, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widSupply, 1, 1, 1, 2)

        self.widSel = QWidget(self.centralwidget)
        self.widSel.setObjectName(u"widSel")
        self.gridLayout_2 = QGridLayout(self.widSel)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbTitle1Num = QLabel(self.widSel)
        self.lbTitle1Num.setObjectName(u"lbTitle1Num")
        self.lbTitle1Num.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lbTitle1Num, 0, 1, 1, 1)

        self.lbTitle1Ans = QLabel(self.widSel)
        self.lbTitle1Ans.setObjectName(u"lbTitle1Ans")
        self.lbTitle1Ans.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lbTitle1Ans, 0, 2, 1, 1)

        self.lbTitle1Cor = QLabel(self.widSel)
        self.lbTitle1Cor.setObjectName(u"lbTitle1Cor")
        self.lbTitle1Cor.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lbTitle1Cor, 0, 3, 1, 1)

        self.lbTitle1Score = QLabel(self.widSel)
        self.lbTitle1Score.setObjectName(u"lbTitle1Score")
        self.lbTitle1Score.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lbTitle1Score, 0, 4, 1, 1)

        self.lbTitle1Sel = QLabel(self.widSel)
        self.lbTitle1Sel.setObjectName(u"lbTitle1Sel")
        sizePolicy.setHeightForWidth(self.lbTitle1Sel.sizePolicy().hasHeightForWidth())
        self.lbTitle1Sel.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.lbTitle1Sel, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widSel, 0, 1, 1, 2)

        self.btnClose = QPushButton(self.centralwidget)
        self.btnClose.setObjectName(u"btnClose")
        sizePolicy.setHeightForWidth(self.btnClose.sizePolicy().hasHeightForWidth())
        self.btnClose.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.btnClose, 2, 2, 1, 1)

        GradDetail.setCentralWidget(self.centralwidget)

        self.retranslateUi(GradDetail)

        QMetaObject.connectSlotsByName(GradDetail)
    # setupUi

    def retranslateUi(self, GradDetail):
        GradDetail.setWindowTitle(QCoreApplication.translate("GradDetail", u"\uc0c1\uc138", None))
        self.lbTitle2Get.setText(QCoreApplication.translate("GradDetail", u"\ub4dd\uc810", None))
        self.lbTitle2Num.setText(QCoreApplication.translate("GradDetail", u"\ubc88\ud638", None))
        self.lbTitle2Score.setText(QCoreApplication.translate("GradDetail", u"\ubc30\uc810", None))
        self.lbTitleSupply.setText(QCoreApplication.translate("GradDetail", u"\uc11c\n"
"\ub2f5\n"
"\ud615\n"
"\uc624\n"
"\ub2f5", None))
        self.lbTitle1Num.setText(QCoreApplication.translate("GradDetail", u"\ubc88\ud638", None))
        self.lbTitle1Ans.setText(QCoreApplication.translate("GradDetail", u"\uc751\ub2f5", None))
        self.lbTitle1Cor.setText(QCoreApplication.translate("GradDetail", u"\uc815\ub2f5", None))
        self.lbTitle1Score.setText(QCoreApplication.translate("GradDetail", u"\ubc30\uc810", None))
        self.lbTitle1Sel.setText(QCoreApplication.translate("GradDetail", u"\uc120\n"
"\ud0dd\n"
"\ud615\n"
"\uc624\n"
"\ub2f5", None))
        self.btnClose.setText(QCoreApplication.translate("GradDetail", u"\ub2eb\uae30", None))
    # retranslateUi

class Ui_GradRes(object):
    def setupUi(self, GradRes):
        if not GradRes.objectName():
            GradRes.setObjectName(u"GradRes")
        GradRes.resize(218, 107)
        self.centralwidget = QWidget(GradRes)
        self.centralwidget.setObjectName(u"centralwidget")
        self.glMain = QGridLayout(self.centralwidget)
        self.glMain.setObjectName(u"glMain")
        self.btnDetail = QPushButton(self.centralwidget)
        self.btnDetail.setObjectName(u"btnDetail")
        self.btnDetail.setMaximumSize(QSize(50, 16777215))

        self.glMain.addWidget(self.btnDetail, 1, 3, 1, 1)

        self.lbTitleDetail = QLabel(self.centralwidget)
        self.lbTitleDetail.setObjectName(u"lbTitleDetail")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbTitleDetail.sizePolicy().hasHeightForWidth())
        self.lbTitleDetail.setSizePolicy(sizePolicy)
        self.lbTitleDetail.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbTitleDetail, 0, 3, 1, 1)

        self.lbWrong = QLabel(self.centralwidget)
        self.lbWrong.setObjectName(u"lbWrong")
        sizePolicy.setHeightForWidth(self.lbWrong.sizePolicy().hasHeightForWidth())
        self.lbWrong.setSizePolicy(sizePolicy)
        self.lbWrong.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbWrong, 1, 1, 1, 1)

        self.lbScore = QLabel(self.centralwidget)
        self.lbScore.setObjectName(u"lbScore")
        sizePolicy.setHeightForWidth(self.lbScore.sizePolicy().hasHeightForWidth())
        self.lbScore.setSizePolicy(sizePolicy)
        self.lbScore.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbScore, 1, 2, 1, 1)

        self.lbSubject = QLabel(self.centralwidget)
        self.lbSubject.setObjectName(u"lbSubject")
        sizePolicy.setHeightForWidth(self.lbSubject.sizePolicy().hasHeightForWidth())
        self.lbSubject.setSizePolicy(sizePolicy)
        self.lbSubject.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbSubject, 1, 0, 1, 1)

        self.lbTitleSubject = QLabel(self.centralwidget)
        self.lbTitleSubject.setObjectName(u"lbTitleSubject")
        sizePolicy.setHeightForWidth(self.lbTitleSubject.sizePolicy().hasHeightForWidth())
        self.lbTitleSubject.setSizePolicy(sizePolicy)
        self.lbTitleSubject.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbTitleSubject, 0, 0, 1, 1)

        self.lbTitleGrade = QLabel(self.centralwidget)
        self.lbTitleGrade.setObjectName(u"lbTitleGrade")
        sizePolicy.setHeightForWidth(self.lbTitleGrade.sizePolicy().hasHeightForWidth())
        self.lbTitleGrade.setSizePolicy(sizePolicy)
        self.lbTitleGrade.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbTitleGrade, 0, 2, 1, 1)

        self.lbTitleWrong = QLabel(self.centralwidget)
        self.lbTitleWrong.setObjectName(u"lbTitleWrong")
        sizePolicy.setHeightForWidth(self.lbTitleWrong.sizePolicy().hasHeightForWidth())
        self.lbTitleWrong.setSizePolicy(sizePolicy)
        self.lbTitleWrong.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbTitleWrong, 0, 1, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.hlBot = QHBoxLayout(self.widget)
        self.hlBot.setObjectName(u"hlBot")
        self.hlBot.setContentsMargins(0, 0, 0, 0)
        self.sp = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlBot.addItem(self.sp)

        self.btnClose = QPushButton(self.widget)
        self.btnClose.setObjectName(u"btnClose")

        self.hlBot.addWidget(self.btnClose)


        self.glMain.addWidget(self.widget, 2, 0, 1, 4)

        GradRes.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btnDetail, self.btnClose)

        self.retranslateUi(GradRes)

        QMetaObject.connectSlotsByName(GradRes)
    # setupUi

    def retranslateUi(self, GradRes):
        GradRes.setWindowTitle(QCoreApplication.translate("GradRes", u"\uac00\ucc44\uc810\uacb0\uacfc", None))
        self.btnDetail.setText(QCoreApplication.translate("GradRes", u"\ubcf4\uae30", None))
        self.lbTitleDetail.setText(QCoreApplication.translate("GradRes", u"\uc0c1\uc138", None))
        self.lbWrong.setText(QCoreApplication.translate("GradRes", u"\uc624\ub2f5 \uc218", None))
        self.lbScore.setText(QCoreApplication.translate("GradRes", u"35", None))
        self.lbSubject.setText(QCoreApplication.translate("GradRes", u"\uacfc\ubaa9\uba85", None))
        self.lbTitleSubject.setText(QCoreApplication.translate("GradRes", u"\uacfc\ubaa9\uba85", None))
        self.lbTitleGrade.setText(QCoreApplication.translate("GradRes", u"\uc810\uc218", None))
        self.lbTitleWrong.setText(QCoreApplication.translate("GradRes", u"\uc624\ub2f5 \uc218", None))
        self.btnClose.setText(QCoreApplication.translate("GradRes", u"\ub2eb\uae30", None))
    # retranslateUi

class Ui_Grading1(object):
    def setupUi(self, Grading1):
        if not Grading1.objectName():
            Grading1.setObjectName(u"Grading1")
        Grading1.resize(220, 80)
        self.centralwidget = QWidget(Grading1)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnNext = QPushButton(self.centralwidget)
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setGeometry(QRect(113, 43, 93, 28))
        self.lbSubject = QLabel(self.centralwidget)
        self.lbSubject.setObjectName(u"lbSubject")
        self.lbSubject.setGeometry(QRect(10, 15, 35, 16))
        self.comboSubject = QComboBox(self.centralwidget)
        self.comboSubject.setObjectName(u"comboSubject")
        self.comboSubject.setGeometry(QRect(56, 15, 151, 21))
        self.btnBack = QPushButton(self.centralwidget)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setGeometry(QRect(10, 43, 93, 28))
        Grading1.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.comboSubject, self.btnBack)
        QWidget.setTabOrder(self.btnBack, self.btnNext)

        self.retranslateUi(Grading1)

        QMetaObject.connectSlotsByName(Grading1)
    # setupUi

    def retranslateUi(self, Grading1):
        Grading1.setWindowTitle(QCoreApplication.translate("Grading1", u"\uacfc\ubaa9\uc120\ud0dd", None))
        self.btnNext.setText(QCoreApplication.translate("Grading1", u"\ub2e4\uc74c", None))
        self.lbSubject.setText(QCoreApplication.translate("Grading1", u"\uacfc\ubaa9:", None))
        self.btnBack.setText(QCoreApplication.translate("Grading1", u"\ucde8\uc18c", None))
    # retranslateUi

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

        self.lb15 = QLabel(self.centralwidget)
        self.lb15.setObjectName(u"lb15")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lb15.sizePolicy().hasHeightForWidth())
        self.lb15.setSizePolicy(sizePolicy1)
        self.lb15.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lb15, 0, 1, 1, 1)

        self.lb610 = QLabel(self.centralwidget)
        self.lb610.setObjectName(u"lb610")
        sizePolicy1.setHeightForWidth(self.lb610.sizePolicy().hasHeightForWidth())
        self.lb610.setSizePolicy(sizePolicy1)
        self.lb610.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lb610, 0, 2, 1, 1)

        self.lb1115 = QLabel(self.centralwidget)
        self.lb1115.setObjectName(u"lb1115")
        sizePolicy1.setHeightForWidth(self.lb1115.sizePolicy().hasHeightForWidth())
        self.lb1115.setSizePolicy(sizePolicy1)
        self.lb1115.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lb1115, 0, 3, 1, 1)

        self.lb1620 = QLabel(self.centralwidget)
        self.lb1620.setObjectName(u"lb1620")
        sizePolicy1.setHeightForWidth(self.lb1620.sizePolicy().hasHeightForWidth())
        self.lb1620.setSizePolicy(sizePolicy1)
        self.lb1620.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lb1620, 1, 1, 1, 1)

        self.lb2125 = QLabel(self.centralwidget)
        self.lb2125.setObjectName(u"lb2125")
        sizePolicy1.setHeightForWidth(self.lb2125.sizePolicy().hasHeightForWidth())
        self.lb2125.setSizePolicy(sizePolicy1)
        self.lb2125.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lb2125, 1, 2, 1, 1)

        self.lb2630 = QLabel(self.centralwidget)
        self.lb2630.setObjectName(u"lb2630")
        sizePolicy1.setHeightForWidth(self.lb2630.sizePolicy().hasHeightForWidth())
        self.lb2630.setSizePolicy(sizePolicy1)
        self.lb2630.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lb2630, 1, 3, 1, 1)

        self.lbAns = QLabel(self.centralwidget)
        self.lbAns.setObjectName(u"lbAns")
        sizePolicy.setHeightForWidth(self.lbAns.sizePolicy().hasHeightForWidth())
        self.lbAns.setSizePolicy(sizePolicy)

        self.glMain.addWidget(self.lbAns, 2, 0, 2, 1)

        self.lnAns15 = QLineEdit(self.centralwidget)
        self.lnAns15.setObjectName(u"lnAns15")
        sizePolicy.setHeightForWidth(self.lnAns15.sizePolicy().hasHeightForWidth())
        self.lnAns15.setSizePolicy(sizePolicy)
        self.lnAns15.setMaximumSize(QSize(100, 24))
        self.lnAns15.setStyleSheet(u"padding:16px")
        self.lnAns15.setMaxLength(9)
        self.lnAns15.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnAns15, 2, 1, 1, 1)

        self.lnAns610 = QLineEdit(self.centralwidget)
        self.lnAns610.setObjectName(u"lnAns610")
        sizePolicy.setHeightForWidth(self.lnAns610.sizePolicy().hasHeightForWidth())
        self.lnAns610.setSizePolicy(sizePolicy)
        self.lnAns610.setMaximumSize(QSize(100, 24))
        self.lnAns610.setStyleSheet(u"padding:16px")
        self.lnAns610.setMaxLength(9)
        self.lnAns610.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnAns610, 2, 2, 1, 1)

        self.lnAns1115 = QLineEdit(self.centralwidget)
        self.lnAns1115.setObjectName(u"lnAns1115")
        sizePolicy.setHeightForWidth(self.lnAns1115.sizePolicy().hasHeightForWidth())
        self.lnAns1115.setSizePolicy(sizePolicy)
        self.lnAns1115.setMaximumSize(QSize(100, 24))
        self.lnAns1115.setStyleSheet(u"padding:16px")
        self.lnAns1115.setMaxLength(9)
        self.lnAns1115.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnAns1115, 2, 3, 1, 1)

        self.lnAns1620 = QLineEdit(self.centralwidget)
        self.lnAns1620.setObjectName(u"lnAns1620")
        sizePolicy.setHeightForWidth(self.lnAns1620.sizePolicy().hasHeightForWidth())
        self.lnAns1620.setSizePolicy(sizePolicy)
        self.lnAns1620.setMaximumSize(QSize(100, 24))
        self.lnAns1620.setStyleSheet(u"padding:16px")
        self.lnAns1620.setMaxLength(9)
        self.lnAns1620.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnAns1620, 3, 1, 1, 1)

        self.lnAns2125 = QLineEdit(self.centralwidget)
        self.lnAns2125.setObjectName(u"lnAns2125")
        sizePolicy.setHeightForWidth(self.lnAns2125.sizePolicy().hasHeightForWidth())
        self.lnAns2125.setSizePolicy(sizePolicy)
        self.lnAns2125.setMaximumSize(QSize(100, 24))
        self.lnAns2125.setStyleSheet(u"padding:16px")
        self.lnAns2125.setMaxLength(9)
        self.lnAns2125.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnAns2125, 3, 2, 1, 1)

        self.lnAns2630 = QLineEdit(self.centralwidget)
        self.lnAns2630.setObjectName(u"lnAns2630")
        sizePolicy.setHeightForWidth(self.lnAns2630.sizePolicy().hasHeightForWidth())
        self.lnAns2630.setSizePolicy(sizePolicy)
        self.lnAns2630.setMaximumSize(QSize(100, 24))
        self.lnAns2630.setStyleSheet(u"padding:16px")
        self.lnAns2630.setMaxLength(9)
        self.lnAns2630.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnAns2630, 3, 3, 1, 1)

        self.lbCor = QLabel(self.centralwidget)
        self.lbCor.setObjectName(u"lbCor")
        sizePolicy.setHeightForWidth(self.lbCor.sizePolicy().hasHeightForWidth())
        self.lbCor.setSizePolicy(sizePolicy)

        self.glMain.addWidget(self.lbCor, 4, 0, 2, 1)

        self.lnCor15 = QLineEdit(self.centralwidget)
        self.lnCor15.setObjectName(u"lnCor15")
        sizePolicy.setHeightForWidth(self.lnCor15.sizePolicy().hasHeightForWidth())
        self.lnCor15.setSizePolicy(sizePolicy)
        self.lnCor15.setMaximumSize(QSize(100, 24))
        self.lnCor15.setStyleSheet(u"padding:16px")
        self.lnCor15.setMaxLength(9)
        self.lnCor15.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnCor15, 4, 1, 1, 1)

        self.lnCor610 = QLineEdit(self.centralwidget)
        self.lnCor610.setObjectName(u"lnCor610")
        sizePolicy.setHeightForWidth(self.lnCor610.sizePolicy().hasHeightForWidth())
        self.lnCor610.setSizePolicy(sizePolicy)
        self.lnCor610.setMaximumSize(QSize(100, 24))
        self.lnCor610.setStyleSheet(u"padding:16px")
        self.lnCor610.setMaxLength(9)
        self.lnCor610.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnCor610, 4, 2, 1, 1)

        self.lnCor1115 = QLineEdit(self.centralwidget)
        self.lnCor1115.setObjectName(u"lnCor1115")
        sizePolicy.setHeightForWidth(self.lnCor1115.sizePolicy().hasHeightForWidth())
        self.lnCor1115.setSizePolicy(sizePolicy)
        self.lnCor1115.setMaximumSize(QSize(100, 24))
        self.lnCor1115.setStyleSheet(u"padding:16px")
        self.lnCor1115.setMaxLength(9)
        self.lnCor1115.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnCor1115, 4, 3, 1, 1)

        self.lnCor1620 = QLineEdit(self.centralwidget)
        self.lnCor1620.setObjectName(u"lnCor1620")
        sizePolicy.setHeightForWidth(self.lnCor1620.sizePolicy().hasHeightForWidth())
        self.lnCor1620.setSizePolicy(sizePolicy)
        self.lnCor1620.setMaximumSize(QSize(100, 24))
        self.lnCor1620.setStyleSheet(u"padding:16px")
        self.lnCor1620.setMaxLength(9)
        self.lnCor1620.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnCor1620, 5, 1, 1, 1)

        self.lnCor2125 = QLineEdit(self.centralwidget)
        self.lnCor2125.setObjectName(u"lnCor2125")
        sizePolicy.setHeightForWidth(self.lnCor2125.sizePolicy().hasHeightForWidth())
        self.lnCor2125.setSizePolicy(sizePolicy)
        self.lnCor2125.setMaximumSize(QSize(100, 24))
        self.lnCor2125.setStyleSheet(u"padding:16px")
        self.lnCor2125.setMaxLength(9)
        self.lnCor2125.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnCor2125, 5, 2, 1, 1)

        self.lnCor2630 = QLineEdit(self.centralwidget)
        self.lnCor2630.setObjectName(u"lnCor2630")
        sizePolicy.setHeightForWidth(self.lnCor2630.sizePolicy().hasHeightForWidth())
        self.lnCor2630.setSizePolicy(sizePolicy)
        self.lnCor2630.setMaximumSize(QSize(100, 24))
        self.lnCor2630.setStyleSheet(u"padding:16px")
        self.lnCor2630.setMaxLength(9)
        self.lnCor2630.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnCor2630, 5, 3, 1, 1)

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
        self.lbSubject.setText(QCoreApplication.translate("Grading2", u"\uacfc\n"
"\ubaa9", None))
        self.lb15.setText(QCoreApplication.translate("Grading2", u"1~5", None))
        self.lb610.setText(QCoreApplication.translate("Grading2", u"6~10", None))
        self.lb1115.setText(QCoreApplication.translate("Grading2", u"11~15", None))
        self.lb1620.setText(QCoreApplication.translate("Grading2", u"16~20", None))
        self.lb2125.setText(QCoreApplication.translate("Grading2", u"21~25", None))
        self.lb2630.setText(QCoreApplication.translate("Grading2", u"26~30", None))
        self.lbAns.setText(QCoreApplication.translate("Grading2", u"\uc751\n"
"\ub2f5", None))
        self.lnAns15.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnAns610.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnAns1115.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnAns1620.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnAns2125.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnAns2630.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lbCor.setText(QCoreApplication.translate("Grading2", u"\uc815\n"
"\ub2f5", None))
        self.lnCor15.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnCor610.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnCor1115.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnCor1620.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnCor2125.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnCor2630.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.btnBack.setText(QCoreApplication.translate("Grading2", u"\uc774\uc804", None))
        self.btnRe.setText(QCoreApplication.translate("Grading2", u"\ub2e4\uc2dc", None))
        self.btnNext.setText(QCoreApplication.translate("Grading2", u"\ub2e4\uc74c", None))
    # retranslateUi

class Ui_Grading31(object):
    def setupUi(self, Grading31):
        if not Grading31.objectName():
            Grading31.setObjectName(u"Grading31")
        Grading31.resize(215, 103)
        self.centralwidget = QWidget(Grading31)
        self.centralwidget.setObjectName(u"centralwidget")
        self.glMain = QGridLayout(self.centralwidget)
        self.glMain.setObjectName(u"glMain")
        self.lbNum = QLabel(self.centralwidget)
        self.lbNum.setObjectName(u"lbNum")
        self.lbNum.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbNum, 0, 0, 1, 1)

        self.lbPoint = QLabel(self.centralwidget)
        self.lbPoint.setObjectName(u"lbPoint")
        self.lbPoint.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbPoint, 0, 1, 1, 1)

        self.lbNo = QLabel(self.centralwidget)
        self.lbNo.setObjectName(u"lbNo")
        self.lbNo.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbNo, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.glMain.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.widBot = QWidget(self.centralwidget)
        self.widBot.setObjectName(u"widBot")
        self.hlBot = QHBoxLayout(self.widBot)
        self.hlBot.setSpacing(0)
        self.hlBot.setObjectName(u"hlBot")
        self.hlBot.setContentsMargins(0, 0, 0, 0)
        self.btnBack = QPushButton(self.widBot)
        self.btnBack.setObjectName(u"btnBack")

        self.hlBot.addWidget(self.btnBack)

        self.spH = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlBot.addItem(self.spH)

        self.btnNext = QPushButton(self.widBot)
        self.btnNext.setObjectName(u"btnNext")

        self.hlBot.addWidget(self.btnNext)


        self.glMain.addWidget(self.widBot, 2, 0, 1, 2)

        Grading31.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.lineEdit, self.btnBack)
        QWidget.setTabOrder(self.btnBack, self.btnNext)

        self.retranslateUi(Grading31)

        QMetaObject.connectSlotsByName(Grading31)
    # setupUi

    def retranslateUi(self, Grading31):
        Grading31.setWindowTitle(QCoreApplication.translate("Grading31", u"\uc120\ud0dd\ud615 \ubc30\uc810", None))
        self.lbNum.setText(QCoreApplication.translate("Grading31", u"\ubc88\ud638", None))
        self.lbPoint.setText(QCoreApplication.translate("Grading31", u"\ubc30\uc810", None))
        self.lbNo.setText(QCoreApplication.translate("Grading31", u"111", None))
        self.lineEdit.setInputMask(QCoreApplication.translate("Grading31", u"D.d", None))
        self.btnBack.setText(QCoreApplication.translate("Grading31", u"\uc774\uc804", None))
        self.btnNext.setText(QCoreApplication.translate("Grading31", u"\ub2e4\uc74c", None))
    # retranslateUi

class Ui_Grading32(object):
    def setupUi(self, Grading32):
        if not Grading32.objectName():
            Grading32.setObjectName(u"Grading32")
        Grading32.resize(260, 104)
        self.centralwidget = QWidget(Grading32)
        self.centralwidget.setObjectName(u"centralwidget")
        self.glMain = QGridLayout(self.centralwidget)
        self.glMain.setObjectName(u"glMain")
        self.lbTitleNo = QLabel(self.centralwidget)
        self.lbTitleNo.setObjectName(u"lbTitleNo")
        self.lbTitleNo.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbTitleNo, 0, 0, 1, 1)

        self.lbTitlePoint = QLabel(self.centralwidget)
        self.lbTitlePoint.setObjectName(u"lbTitlePoint")
        self.lbTitlePoint.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbTitlePoint, 0, 1, 1, 1)

        self.lbTitleGet = QLabel(self.centralwidget)
        self.lbTitleGet.setObjectName(u"lbTitleGet")
        self.lbTitleGet.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbTitleGet, 0, 2, 1, 1)

        self.lbNo = QLabel(self.centralwidget)
        self.lbNo.setObjectName(u"lbNo")
        self.lbNo.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbNo, 1, 0, 1, 1)

        self.lnPoint = QLineEdit(self.centralwidget)
        self.lnPoint.setObjectName(u"lnPoint")
        self.lnPoint.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.glMain.addWidget(self.lnPoint, 1, 1, 1, 1)

        self.lnGet = QLineEdit(self.centralwidget)
        self.lnGet.setObjectName(u"lnGet")
        self.lnGet.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.glMain.addWidget(self.lnGet, 1, 2, 1, 1)

        self.widBot = QWidget(self.centralwidget)
        self.widBot.setObjectName(u"widBot")
        self.hlBot = QHBoxLayout(self.widBot)
        self.hlBot.setSpacing(0)
        self.hlBot.setObjectName(u"hlBot")
        self.hlBot.setContentsMargins(0, 0, 0, 0)
        self.btnBack = QPushButton(self.widBot)
        self.btnBack.setObjectName(u"btnBack")

        self.hlBot.addWidget(self.btnBack)

        self.spH = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlBot.addItem(self.spH)

        self.btnNext = QPushButton(self.widBot)
        self.btnNext.setObjectName(u"btnNext")

        self.hlBot.addWidget(self.btnNext)


        self.glMain.addWidget(self.widBot, 2, 0, 1, 3)

        Grading32.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.lnPoint, self.lnGet)
        QWidget.setTabOrder(self.lnGet, self.btnBack)
        QWidget.setTabOrder(self.btnBack, self.btnNext)

        self.retranslateUi(Grading32)

        QMetaObject.connectSlotsByName(Grading32)
    # setupUi

    def retranslateUi(self, Grading32):
        Grading32.setWindowTitle(QCoreApplication.translate("Grading32", u"\uc11c\ub2f5\ud615 \ubc30\uc810", None))
        self.lbTitleNo.setText(QCoreApplication.translate("Grading32", u"\ubc88\ud638", None))
        self.lbTitlePoint.setText(QCoreApplication.translate("Grading32", u"\ubc30\uc810", None))
        self.lbTitleGet.setText(QCoreApplication.translate("Grading32", u"\ubc30\uc810", None))
        self.lbNo.setText(QCoreApplication.translate("Grading32", u"99", None))
        self.lnPoint.setInputMask(QCoreApplication.translate("Grading32", u"D.d", None))
        self.lnGet.setInputMask(QCoreApplication.translate("Grading32", u"D.d", None))
        self.btnBack.setText(QCoreApplication.translate("Grading32", u"\uc774\uc804", None))
        self.btnNext.setText(QCoreApplication.translate("Grading32", u"\ub2e4\uc74c", None))
    # retranslateUi

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(442, 300)
        self.save = QAction(Main)
        self.save.setObjectName(u"save")
        self.exit = QAction(Main)
        self.exit.setObjectName(u"exit")
        self.actiontest = QAction(Main)
        self.actiontest.setObjectName(u"actiontest")
        self.load = QAction(Main)
        self.load.setObjectName(u"load")
        self.cut_calc = QAction(Main)
        self.cut_calc.setObjectName(u"cut_calc")
        self.license = QAction(Main)
        self.license.setObjectName(u"license")
        self.about = QAction(Main)
        self.about.setObjectName(u"about")
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.glMain = QGridLayout(self.centralwidget)
        self.glMain.setObjectName(u"glMain")
        self.widManage = QGroupBox(self.centralwidget)
        self.widManage.setObjectName(u"widManage")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widManage.sizePolicy().hasHeightForWidth())
        self.widManage.setSizePolicy(sizePolicy)
        self.vlManage = QVBoxLayout(self.widManage)
        self.vlManage.setObjectName(u"vlManage")
        self.btnCalc = QPushButton(self.widManage)
        self.btnCalc.setObjectName(u"btnCalc")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnCalc.sizePolicy().hasHeightForWidth())
        self.btnCalc.setSizePolicy(sizePolicy1)

        self.vlManage.addWidget(self.btnCalc)

        self.btnInput = QPushButton(self.widManage)
        self.btnInput.setObjectName(u"btnInput")
        sizePolicy1.setHeightForWidth(self.btnInput.sizePolicy().hasHeightForWidth())
        self.btnInput.setSizePolicy(sizePolicy1)

        self.vlManage.addWidget(self.btnInput)

        self.btnRes = QPushButton(self.widManage)
        self.btnRes.setObjectName(u"btnRes")
        sizePolicy1.setHeightForWidth(self.btnRes.sizePolicy().hasHeightForWidth())
        self.btnRes.setSizePolicy(sizePolicy1)

        self.vlManage.addWidget(self.btnRes)

        self.btnManage = QPushButton(self.widManage)
        self.btnManage.setObjectName(u"btnManage")
        sizePolicy1.setHeightForWidth(self.btnManage.sizePolicy().hasHeightForWidth())
        self.btnManage.setSizePolicy(sizePolicy1)

        self.vlManage.addWidget(self.btnManage)


        self.glMain.addWidget(self.widManage, 1, 1, 1, 1)

        self.widGrade = QGroupBox(self.centralwidget)
        self.widGrade.setObjectName(u"widGrade")
        sizePolicy.setHeightForWidth(self.widGrade.sizePolicy().hasHeightForWidth())
        self.widGrade.setSizePolicy(sizePolicy)
        self.vlGrade = QVBoxLayout(self.widGrade)
        self.vlGrade.setObjectName(u"vlGrade")
        self.btnSubject = QPushButton(self.widGrade)
        self.btnSubject.setObjectName(u"btnSubject")
        sizePolicy1.setHeightForWidth(self.btnSubject.sizePolicy().hasHeightForWidth())
        self.btnSubject.setSizePolicy(sizePolicy1)

        self.vlGrade.addWidget(self.btnSubject)

        self.btnGrading = QPushButton(self.widGrade)
        self.btnGrading.setObjectName(u"btnGrading")
        sizePolicy1.setHeightForWidth(self.btnGrading.sizePolicy().hasHeightForWidth())
        self.btnGrading.setSizePolicy(sizePolicy1)

        self.vlGrade.addWidget(self.btnGrading)

        self.btnGradingRes = QPushButton(self.widGrade)
        self.btnGradingRes.setObjectName(u"btnGradingRes")
        sizePolicy1.setHeightForWidth(self.btnGradingRes.sizePolicy().hasHeightForWidth())
        self.btnGradingRes.setSizePolicy(sizePolicy1)

        self.vlGrade.addWidget(self.btnGradingRes)


        self.glMain.addWidget(self.widGrade, 1, 0, 1, 1)

        self.widYear = QGroupBox(self.centralwidget)
        self.widYear.setObjectName(u"widYear")
        self.hlYear = QHBoxLayout(self.widYear)
        self.hlYear.setObjectName(u"hlYear")
        self.comboYear = QComboBox(self.widYear)
        self.comboYear.setObjectName(u"comboYear")

        self.hlYear.addWidget(self.comboYear)

        self.comboSemester = QComboBox(self.widYear)
        self.comboSemester.setObjectName(u"comboSemester")

        self.hlYear.addWidget(self.comboSemester)

        self.comboExam = QComboBox(self.widYear)
        self.comboExam.setObjectName(u"comboExam")

        self.hlYear.addWidget(self.comboExam)

        self.btnSet = QPushButton(self.widYear)
        self.btnSet.setObjectName(u"btnSet")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnSet.sizePolicy().hasHeightForWidth())
        self.btnSet.setSizePolicy(sizePolicy2)

        self.hlYear.addWidget(self.btnSet)


        self.glMain.addWidget(self.widYear, 0, 0, 1, 2)

        Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 442, 26))
        self.file = QMenu(self.menubar)
        self.file.setObjectName(u"file")
        self.tools = QMenu(self.menubar)
        self.tools.setObjectName(u"tools")
        self.info = QMenu(self.menubar)
        self.info.setObjectName(u"info")
        Main.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.comboYear, self.comboSemester)
        QWidget.setTabOrder(self.comboSemester, self.comboExam)
        QWidget.setTabOrder(self.comboExam, self.btnSet)
        QWidget.setTabOrder(self.btnSet, self.btnSubject)
        QWidget.setTabOrder(self.btnSubject, self.btnGrading)
        QWidget.setTabOrder(self.btnGrading, self.btnGradingRes)
        QWidget.setTabOrder(self.btnGradingRes, self.btnCalc)
        QWidget.setTabOrder(self.btnCalc, self.btnInput)
        QWidget.setTabOrder(self.btnInput, self.btnRes)
        QWidget.setTabOrder(self.btnRes, self.btnManage)

        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.tools.menuAction())
        self.menubar.addAction(self.info.menuAction())
        self.file.addAction(self.load)
        self.file.addAction(self.save)
        self.file.addSeparator()
        self.file.addAction(self.exit)
        self.tools.addAction(self.cut_calc)
        self.info.addAction(self.license)
        self.info.addSeparator()
        self.info.addAction(self.about)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"\uc131\uc801\uad00\ub9ac", None))
        self.save.setText(QCoreApplication.translate("Main", u"\uc800\uc7a5", None))
        self.exit.setText(QCoreApplication.translate("Main", u"\uc885\ub8cc", None))
        self.actiontest.setText(QCoreApplication.translate("Main", u"test", None))
        self.load.setText(QCoreApplication.translate("Main", u"\ubd88\ub7ec\uc624\uae30", None))
        self.cut_calc.setText(QCoreApplication.translate("Main", u"\ub4f1\uae09\uc778\uc6d0\uacc4\uc0b0", None))
        self.license.setText(QCoreApplication.translate("Main", u"License", None))
        self.about.setText(QCoreApplication.translate("Main", u"\uc815\ubcf4", None))
        self.widManage.setTitle(QCoreApplication.translate("Main", u"\uc131\uc801\uad00\ub9ac", None))
        self.btnCalc.setText(QCoreApplication.translate("Main", u"\ub4f1\uae09\uacc4\uc0b0", None))
        self.btnInput.setText(QCoreApplication.translate("Main", u"\uc131\uc801\uc785\ub825", None))
        self.btnRes.setText(QCoreApplication.translate("Main", u"\uc2dc\ud5d8\uacb0\uacfc", None))
        self.btnManage.setText(QCoreApplication.translate("Main", u"\uc131\uc801\ucd94\uc774", None))
        self.widGrade.setTitle(QCoreApplication.translate("Main", u"\uac00\ucc44\uc810", None))
        self.btnSubject.setText(QCoreApplication.translate("Main", u"\uacfc\ubaa9 \uc785\ub825", None))
        self.btnGrading.setText(QCoreApplication.translate("Main", u"\uac00\ucc44\uc810 \uc785\ub825", None))
        self.btnGradingRes.setText(QCoreApplication.translate("Main", u"\uac00\ucc44\uc810 \uacb0\uacfc", None))
        self.widYear.setTitle(QCoreApplication.translate("Main", u"\ud559\ub144\ub3c4", None))
        self.btnSet.setText(QCoreApplication.translate("Main", u"\uc124\uc815", None))
        self.file.setTitle(QCoreApplication.translate("Main", u"\ud30c\uc77c", None))
        self.tools.setTitle(QCoreApplication.translate("Main", u"\ub3c4\uad6c", None))
        self.info.setTitle(QCoreApplication.translate("Main", u"\uc815\ubcf4", None))
    # retranslateUi

class Ui_SubjectIn(object):
    def setupUi(self, SubjectIn):
        if not SubjectIn.objectName():
            SubjectIn.setObjectName(u"SubjectIn")
        SubjectIn.resize(345, 110)
        self.centralwidget = QWidget(SubjectIn)
        self.centralwidget.setObjectName(u"centralwidget")
        self.glMain = QGridLayout(self.centralwidget)
        self.glMain.setObjectName(u"glMain")
        self.lbTitleSubject = QLabel(self.centralwidget)
        self.lbTitleSubject.setObjectName(u"lbTitleSubject")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbTitleSubject.sizePolicy().hasHeightForWidth())
        self.lbTitleSubject.setSizePolicy(sizePolicy)
        self.lbTitleSubject.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbTitleSubject, 0, 0, 1, 1)

        self.lbTitleNum = QLabel(self.centralwidget)
        self.lbTitleNum.setObjectName(u"lbTitleNum")
        sizePolicy.setHeightForWidth(self.lbTitleNum.sizePolicy().hasHeightForWidth())
        self.lbTitleNum.setSizePolicy(sizePolicy)
        self.lbTitleNum.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbTitleNum, 0, 1, 1, 1)

        self.lbTitleMid = QLabel(self.centralwidget)
        self.lbTitleMid.setObjectName(u"lbTitleMid")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbTitleMid.sizePolicy().hasHeightForWidth())
        self.lbTitleMid.setSizePolicy(sizePolicy1)
        self.lbTitleMid.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbTitleMid, 0, 2, 1, 1)

        self.lbTitleEnd = QLabel(self.centralwidget)
        self.lbTitleEnd.setObjectName(u"lbTitleEnd")
        sizePolicy1.setHeightForWidth(self.lbTitleEnd.sizePolicy().hasHeightForWidth())
        self.lbTitleEnd.setSizePolicy(sizePolicy1)
        self.lbTitleEnd.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbTitleEnd, 0, 3, 1, 1)

        self.lbTitleDel = QLabel(self.centralwidget)
        self.lbTitleDel.setObjectName(u"lbTitleDel")
        sizePolicy1.setHeightForWidth(self.lbTitleDel.sizePolicy().hasHeightForWidth())
        self.lbTitleDel.setSizePolicy(sizePolicy1)
        self.lbTitleDel.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lbTitleDel, 0, 4, 1, 1)

        self.lnSubject = QLineEdit(self.centralwidget)
        self.lnSubject.setObjectName(u"lnSubject")
        self.lnSubject.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnSubject, 1, 0, 1, 1)

        self.lnNum = QLineEdit(self.centralwidget)
        self.lnNum.setObjectName(u"lnNum")
        self.lnNum.setMaximumSize(QSize(45, 16777215))
        self.lnNum.setAlignment(Qt.AlignCenter)

        self.glMain.addWidget(self.lnNum, 1, 1, 1, 1)

        self.btnDel = QPushButton(self.centralwidget)
        self.btnDel.setObjectName(u"btnDel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnDel.sizePolicy().hasHeightForWidth())
        self.btnDel.setSizePolicy(sizePolicy2)

        self.glMain.addWidget(self.btnDel, 1, 4, 1, 1)

        self.widBot = QWidget(self.centralwidget)
        self.widBot.setObjectName(u"widBot")
        self.hlBot = QHBoxLayout(self.widBot)
        self.hlBot.setSpacing(0)
        self.hlBot.setObjectName(u"hlBot")
        self.hlBot.setContentsMargins(0, 0, 0, 0)
        self.btnAdd = QPushButton(self.widBot)
        self.btnAdd.setObjectName(u"btnAdd")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btnAdd.sizePolicy().hasHeightForWidth())
        self.btnAdd.setSizePolicy(sizePolicy3)

        self.hlBot.addWidget(self.btnAdd)

        self.sp = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlBot.addItem(self.sp)

        self.btnCancel = QPushButton(self.widBot)
        self.btnCancel.setObjectName(u"btnCancel")
        sizePolicy3.setHeightForWidth(self.btnCancel.sizePolicy().hasHeightForWidth())
        self.btnCancel.setSizePolicy(sizePolicy3)

        self.hlBot.addWidget(self.btnCancel)

        self.btnSet = QPushButton(self.widBot)
        self.btnSet.setObjectName(u"btnSet")
        sizePolicy3.setHeightForWidth(self.btnSet.sizePolicy().hasHeightForWidth())
        self.btnSet.setSizePolicy(sizePolicy3)

        self.hlBot.addWidget(self.btnSet)


        self.glMain.addWidget(self.widBot, 2, 0, 1, 5)

        self.chkMid = QCheckBox(self.centralwidget)
        self.chkMid.setObjectName(u"chkMid")

        self.glMain.addWidget(self.chkMid, 1, 2, 1, 1, Qt.AlignHCenter)

        self.chkEnd = QCheckBox(self.centralwidget)
        self.chkEnd.setObjectName(u"chkEnd")

        self.glMain.addWidget(self.chkEnd, 1, 3, 1, 1, Qt.AlignHCenter)

        SubjectIn.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.lnSubject, self.lnNum)
        QWidget.setTabOrder(self.lnNum, self.chkMid)
        QWidget.setTabOrder(self.chkMid, self.chkEnd)
        QWidget.setTabOrder(self.chkEnd, self.btnDel)
        QWidget.setTabOrder(self.btnDel, self.btnAdd)
        QWidget.setTabOrder(self.btnAdd, self.btnCancel)
        QWidget.setTabOrder(self.btnCancel, self.btnSet)

        self.retranslateUi(SubjectIn)

        QMetaObject.connectSlotsByName(SubjectIn)
    # setupUi

    def retranslateUi(self, SubjectIn):
        SubjectIn.setWindowTitle(QCoreApplication.translate("SubjectIn", u"\uacfc\ubaa9\uc785\ub825", None))
        self.lbTitleSubject.setText(QCoreApplication.translate("SubjectIn", u"\uacfc\ubaa9\uba85", None))
        self.lbTitleNum.setText(QCoreApplication.translate("SubjectIn", u"\ub2e8\uc704\uc218", None))
        self.lbTitleMid.setText(QCoreApplication.translate("SubjectIn", u"\uc911\uac04", None))
        self.lbTitleEnd.setText(QCoreApplication.translate("SubjectIn", u"\uae30\ub9d0", None))
        self.lbTitleDel.setText(QCoreApplication.translate("SubjectIn", u"\uc0ad\uc81c", None))
        self.lnNum.setInputMask(QCoreApplication.translate("SubjectIn", u"D", None))
        self.btnDel.setText(QCoreApplication.translate("SubjectIn", u"X", None))
        self.btnAdd.setText(QCoreApplication.translate("SubjectIn", u"\ucd94\uac00", None))
        self.btnCancel.setText(QCoreApplication.translate("SubjectIn", u"\ucde8\uc18c", None))
        self.btnSet.setText(QCoreApplication.translate("SubjectIn", u"\uc785\ub825", None))
        self.chkMid.setText("")
        self.chkEnd.setText("")
    # retranslateUi

