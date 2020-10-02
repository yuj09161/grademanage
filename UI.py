# -*- coding: utf-8 -*-

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


#Size Policies
sizePolicy_MF = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
sizePolicy_MF.setHorizontalStretch(0)
sizePolicy_MF.setVerticalStretch(0)

sizePolicy_FP = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
sizePolicy_FP.setHorizontalStretch(0)
sizePolicy_FP.setVerticalStretch(0)

sizePolicy_PF = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
sizePolicy_PF.setHorizontalStretch(0)
sizePolicy_PF.setVerticalStretch(0)

sizePolicy_FF = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
sizePolicy_FF.setHorizontalStretch(0)
sizePolicy_FF.setVerticalStretch(0)

sizePolicy_IP = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
sizePolicy_IP.setHorizontalStretch(0)
sizePolicy_IP.setVerticalStretch(0)

sizePolicy_IF = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
sizePolicy_IF.setHorizontalStretch(0)
sizePolicy_IF.setVerticalStretch(0)

sizePolicy_EE = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
sizePolicy_EE.setHorizontalStretch(0)
sizePolicy_EE.setVerticalStretch(0)

sizePolicy_EP = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
sizePolicy_EP.setHorizontalStretch(0)
sizePolicy_EP.setVerticalStretch(0)

CUTS=(4,11,23,40,60,77,89,96,100)

VALIDATOR_SCORE_IN=QRegExpValidator(QRegExp(r'[1-9][0-9]?\.[0-9]'))
VALIDATOR_NUM_1   =QRegExpValidator(QRegExp(r'[0-9]'))


class Ui_CutCalc(object):
    def setupUI(self, CutCalc):
        if not CutCalc.objectName():
            CutCalc.setObjectName(u"CutCalc")
        CutCalc.resize(208, 319)
        
        self.centralwidget = QWidget(CutCalc)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.glMain = QGridLayout(self.centralwidget)
        self.glMain.setObjectName(u"glMain")
        
        self.lbTitleCount = QLabel(self.centralwidget)
        self.lbTitleCount.setObjectName(u"lbTitleCount")
        self.lbTitleCount.setSizePolicy(sizePolicy_IP)
        self.lbTitleCount.setAlignment(Qt.AlignCenter)
        sizePolicy_IP.setHeightForWidth(self.lbTitleCount.sizePolicy().hasHeightForWidth())
        self.glMain.addWidget(self.lbTitleCount, 0, 0, 1, 1)

        self.lnPersonCount = QLineEdit(self.centralwidget)
        self.lnPersonCount.setObjectName(u"lnPersonCount")
        sizePolicy_IF.setHeightForWidth(self.lnPersonCount.sizePolicy().hasHeightForWidth())
        self.lnPersonCount.setSizePolicy(sizePolicy_IF)
        self.lnPersonCount.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lnPersonCount, 0, 1, 1, 2)

        self.lbTitleGrade = QLabel(self.centralwidget)
        self.lbTitleGrade.setObjectName(u"lbTitleGrade")
        sizePolicy_IP.setHeightForWidth(self.lbTitleGrade.sizePolicy().hasHeightForWidth())
        self.lbTitleGrade.setSizePolicy(sizePolicy_IP)
        self.lbTitleGrade.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbTitleGrade, 1, 0, 1, 1)

        self.lbTitleRatio = QLabel(self.centralwidget)
        self.lbTitleRatio.setObjectName(u"lbTitleRatio")
        sizePolicy_IP.setHeightForWidth(self.lbTitleRatio.sizePolicy().hasHeightForWidth())
        self.lbTitleRatio.setSizePolicy(sizePolicy_IP)
        self.lbTitleRatio.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbTitleRatio, 1, 1, 1, 1)

        self.lbCut = QLabel(self.centralwidget)
        self.lbCut.setObjectName(u"lbCut")
        sizePolicy_IP.setHeightForWidth(self.lbCut.sizePolicy().hasHeightForWidth())
        self.lbCut.setSizePolicy(sizePolicy_IP)
        self.lbCut.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbCut, 1, 2, 1, 1)

        self.lbGrade1 = QLabel(self.centralwidget)
        self.lbGrade1.setObjectName(u"lbGrade1")
        sizePolicy_IP.setHeightForWidth(self.lbGrade1.sizePolicy().hasHeightForWidth())
        self.lbGrade1.setSizePolicy(sizePolicy_IP)
        self.lbGrade1.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbGrade1, 2, 0, 1, 1)

        self.lbRatio1 = QLabel(self.centralwidget)
        self.lbRatio1.setObjectName(u"lbRatio1")
        sizePolicy_IP.setHeightForWidth(self.lbRatio1.sizePolicy().hasHeightForWidth())
        self.lbRatio1.setSizePolicy(sizePolicy_IP)
        self.lbRatio1.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbRatio1, 2, 1, 1, 1)

        self.lbCut1 = QLabel(self.centralwidget)
        self.lbCut1.setObjectName(u"lbCut1")
        sizePolicy_IP.setHeightForWidth(self.lbCut1.sizePolicy().hasHeightForWidth())
        self.lbCut1.setSizePolicy(sizePolicy_IP)
        self.lbCut1.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbCut1, 2, 2, 1, 1)

        self.lbGrade2 = QLabel(self.centralwidget)
        self.lbGrade2.setObjectName(u"lbGrade2")
        sizePolicy_IP.setHeightForWidth(self.lbGrade2.sizePolicy().hasHeightForWidth())
        self.lbGrade2.setSizePolicy(sizePolicy_IP)
        self.lbGrade2.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbGrade2, 3, 0, 1, 1)

        self.lbRatio2 = QLabel(self.centralwidget)
        self.lbRatio2.setObjectName(u"lbRatio2")
        sizePolicy_IP.setHeightForWidth(self.lbRatio2.sizePolicy().hasHeightForWidth())
        self.lbRatio2.setSizePolicy(sizePolicy_IP)
        self.lbRatio2.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbRatio2, 3, 1, 1, 1)

        self.lbCut2 = QLabel(self.centralwidget)
        self.lbCut2.setObjectName(u"lbCut2")
        sizePolicy_IP.setHeightForWidth(self.lbCut2.sizePolicy().hasHeightForWidth())
        self.lbCut2.setSizePolicy(sizePolicy_IP)
        self.lbCut2.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbCut2, 3, 2, 1, 1)

        self.lbGrade3 = QLabel(self.centralwidget)
        self.lbGrade3.setObjectName(u"lbGrade3")
        sizePolicy_IP.setHeightForWidth(self.lbGrade3.sizePolicy().hasHeightForWidth())
        self.lbGrade3.setSizePolicy(sizePolicy_IP)
        self.lbGrade3.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbGrade3, 4, 0, 1, 1)

        self.lbRatio3 = QLabel(self.centralwidget)
        self.lbRatio3.setObjectName(u"lbRatio3")
        sizePolicy_IP.setHeightForWidth(self.lbRatio3.sizePolicy().hasHeightForWidth())
        self.lbRatio3.setSizePolicy(sizePolicy_IP)
        self.lbRatio3.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbRatio3, 4, 1, 1, 1)

        self.lbCut3 = QLabel(self.centralwidget)
        self.lbCut3.setObjectName(u"lbCut3")
        sizePolicy_IP.setHeightForWidth(self.lbCut3.sizePolicy().hasHeightForWidth())
        self.lbCut3.setSizePolicy(sizePolicy_IP)
        self.lbCut3.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbCut3, 4, 2, 1, 1)

        self.lbGrade4 = QLabel(self.centralwidget)
        self.lbGrade4.setObjectName(u"lbGrade4")
        sizePolicy_IP.setHeightForWidth(self.lbGrade4.sizePolicy().hasHeightForWidth())
        self.lbGrade4.setSizePolicy(sizePolicy_IP)
        self.lbGrade4.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbGrade4, 5, 0, 1, 1)

        self.lbRatio4 = QLabel(self.centralwidget)
        self.lbRatio4.setObjectName(u"lbRatio4")
        sizePolicy_IP.setHeightForWidth(self.lbRatio4.sizePolicy().hasHeightForWidth())
        self.lbRatio4.setSizePolicy(sizePolicy_IP)
        self.lbRatio4.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbRatio4, 5, 1, 1, 1)

        self.lbCut4 = QLabel(self.centralwidget)
        self.lbCut4.setObjectName(u"lbCut4")
        sizePolicy_IP.setHeightForWidth(self.lbCut4.sizePolicy().hasHeightForWidth())
        self.lbCut4.setSizePolicy(sizePolicy_IP)
        self.lbCut4.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbCut4, 5, 2, 1, 1)

        self.lbGrade5 = QLabel(self.centralwidget)
        self.lbGrade5.setObjectName(u"lbGrade5")
        sizePolicy_IP.setHeightForWidth(self.lbGrade5.sizePolicy().hasHeightForWidth())
        self.lbGrade5.setSizePolicy(sizePolicy_IP)
        self.lbGrade5.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbGrade5, 6, 0, 1, 1)

        self.lbRatio5 = QLabel(self.centralwidget)
        self.lbRatio5.setObjectName(u"lbRatio5")
        sizePolicy_IP.setHeightForWidth(self.lbRatio5.sizePolicy().hasHeightForWidth())
        self.lbRatio5.setSizePolicy(sizePolicy_IP)
        self.lbRatio5.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbRatio5, 6, 1, 1, 1)

        self.lbCut5 = QLabel(self.centralwidget)
        self.lbCut5.setObjectName(u"lbCut5")
        sizePolicy_IP.setHeightForWidth(self.lbCut5.sizePolicy().hasHeightForWidth())
        self.lbCut5.setSizePolicy(sizePolicy_IP)
        self.lbCut5.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbCut5, 6, 2, 1, 1)

        self.lbGrade6 = QLabel(self.centralwidget)
        self.lbGrade6.setObjectName(u"lbGrade6")
        sizePolicy_IP.setHeightForWidth(self.lbGrade6.sizePolicy().hasHeightForWidth())
        self.lbGrade6.setSizePolicy(sizePolicy_IP)
        self.lbGrade6.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbGrade6, 7, 0, 1, 1)

        self.lbRatio6 = QLabel(self.centralwidget)
        self.lbRatio6.setObjectName(u"lbRatio6")
        sizePolicy_IP.setHeightForWidth(self.lbRatio6.sizePolicy().hasHeightForWidth())
        self.lbRatio6.setSizePolicy(sizePolicy_IP)
        self.lbRatio6.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbRatio6, 7, 1, 1, 1)

        self.lbCut6 = QLabel(self.centralwidget)
        self.lbCut6.setObjectName(u"lbCut6")
        sizePolicy_IP.setHeightForWidth(self.lbCut6.sizePolicy().hasHeightForWidth())
        self.lbCut6.setSizePolicy(sizePolicy_IP)
        self.lbCut6.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbCut6, 7, 2, 1, 1)

        self.lbGrade7 = QLabel(self.centralwidget)
        self.lbGrade7.setObjectName(u"lbGrade7")
        sizePolicy_IP.setHeightForWidth(self.lbGrade7.sizePolicy().hasHeightForWidth())
        self.lbGrade7.setSizePolicy(sizePolicy_IP)
        self.lbGrade7.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbGrade7, 8, 0, 1, 1)

        self.lbRatio7 = QLabel(self.centralwidget)
        self.lbRatio7.setObjectName(u"lbRatio7")
        sizePolicy_IP.setHeightForWidth(self.lbRatio7.sizePolicy().hasHeightForWidth())
        self.lbRatio7.setSizePolicy(sizePolicy_IP)
        self.lbRatio7.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbRatio7, 8, 1, 1, 1)

        self.lbCut7 = QLabel(self.centralwidget)
        self.lbCut7.setObjectName(u"lbCut7")
        sizePolicy_IP.setHeightForWidth(self.lbCut7.sizePolicy().hasHeightForWidth())
        self.lbCut7.setSizePolicy(sizePolicy_IP)
        self.lbCut7.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbCut7, 8, 2, 1, 1)

        self.lbGrade8 = QLabel(self.centralwidget)
        self.lbGrade8.setObjectName(u"lbGrade8")
        sizePolicy_IP.setHeightForWidth(self.lbGrade8.sizePolicy().hasHeightForWidth())
        self.lbGrade8.setSizePolicy(sizePolicy_IP)
        self.lbGrade8.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbGrade8, 9, 0, 1, 1)

        self.lbRatio8 = QLabel(self.centralwidget)
        self.lbRatio8.setObjectName(u"lbRatio8")
        sizePolicy_IP.setHeightForWidth(self.lbRatio8.sizePolicy().hasHeightForWidth())
        self.lbRatio8.setSizePolicy(sizePolicy_IP)
        self.lbRatio8.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbRatio8, 9, 1, 1, 1)

        self.lbCut8 = QLabel(self.centralwidget)
        self.lbCut8.setObjectName(u"lbCut8")
        sizePolicy_IP.setHeightForWidth(self.lbCut8.sizePolicy().hasHeightForWidth())
        self.lbCut8.setSizePolicy(sizePolicy_IP)
        self.lbCut8.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbCut8, 9, 2, 1, 1)

        self.lbGrade9 = QLabel(self.centralwidget)
        self.lbGrade9.setObjectName(u"lbGrade9")
        sizePolicy_IP.setHeightForWidth(self.lbGrade9.sizePolicy().hasHeightForWidth())
        self.lbGrade9.setSizePolicy(sizePolicy_IP)
        self.lbGrade9.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbGrade9, 10, 0, 1, 1)

        self.lbRatio9 = QLabel(self.centralwidget)
        self.lbRatio9.setObjectName(u"lbRatio9")
        sizePolicy_FP.setHeightForWidth(self.lbRatio9.sizePolicy().hasHeightForWidth())
        self.lbRatio9.setSizePolicy(sizePolicy_FP)
        self.lbRatio9.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbRatio9, 10, 1, 1, 1)

        self.lbCut9 = QLabel(self.centralwidget)
        self.lbCut9.setObjectName(u"lbCut9")
        sizePolicy_IP.setHeightForWidth(self.lbCut9.sizePolicy().hasHeightForWidth())
        self.lbCut9.setSizePolicy(sizePolicy_IP)
        self.lbCut9.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbCut9, 10, 2, 1, 1)
        
        self.lbGrades = (self.lbGrade1,self.lbGrade2,self.lbGrade3,self.lbGrade4,self.lbGrade5,self.lbGrade6,self.lbGrade7,self.lbGrade8,self.lbGrade9)
        self.lbRatios = (self.lbRatio1,self.lbRatio2,self.lbRatio3,self.lbRatio4,self.lbRatio5,self.lbRatio6,self.lbRatio7,self.lbRatio8,self.lbRatio9)
        self.lbCuts   = (self.lbCut1  ,self.lbCut2  ,self.lbCut3  ,self.lbCut4  ,self.lbCut5  ,self.lbCut6  ,self.lbCut7  ,self.lbCut8  ,self.lbCut9  )

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

        self.retranslateUi(CutCalc)

        QMetaObject.connectSlotsByName(CutCalc)
    # setupUI

    def retranslateUi(self, CutCalc):
        CutCalc.setWindowTitle(QCoreApplication.translate("CutCalc", u"\ub4f1\uae09\ucef7 \uacc4\uc0b0", None))
        self.lbTitleCount.setText(QCoreApplication.translate("CutCalc", u"\uc778\uc6d0", None))
        self.lnPersonCount.setInputMask(QCoreApplication.translate("CutCalc", u"900", None))
        self.lbTitleGrade.setText(QCoreApplication.translate("CutCalc", u"\ub4f1\uae09", None))
        self.lbTitleRatio.setText(QCoreApplication.translate("CutCalc", u"\ube44\uc728", None))
        self.lbCut.setText(QCoreApplication.translate("CutCalc", u"\uc778\uc6d0\uc218", None))
        self.btnClose.setText(QCoreApplication.translate("CutCalc", u"\ub2eb\uae30", None))
        self.btnCalc.setText(QCoreApplication.translate("CutCalc", u"\uacc4\uc0b0", None))
    # retranslateUi

class Ui_ExamInput(object):
    def setupUI(self, ExamInput, subjects, nums):
        if not ExamInput.objectName():
            ExamInput.setObjectName(u"ExamInput")
        ExamInput.resize(389, 107)
        self.centralwidget = QWidget(ExamInput)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.glMain = QGridLayout(self.centralwidget)
        self.glMain.setObjectName(u"glMain")
        self.glMain.setHorizontalSpacing(15)
        
        self.lbTitleSubject = QLabel(self.centralwidget)
        self.lbTitleSubject.setObjectName(u"lbTitleSubject")
        sizePolicy_FP.setHeightForWidth(self.lbTitleSubject.sizePolicy().hasHeightForWidth())
        self.lbTitleSubject.setSizePolicy(sizePolicy_FP)
        self.lbTitleSubject.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbTitleSubject, 0, 0, 1, 1, Qt.AlignHCenter)

        self.lbTitleNum = QLabel(self.centralwidget)
        self.lbTitleNum.setObjectName(u"lbTitleNum")
        sizePolicy_FP.setHeightForWidth(self.lbTitleNum.sizePolicy().hasHeightForWidth())
        self.lbTitleNum.setSizePolicy(sizePolicy_FP)
        self.lbTitleNum.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbTitleNum, 0, 1, 1, 1, Qt.AlignHCenter)

        self.lbTitleScore = QLabel(self.centralwidget)
        self.lbTitleScore.setObjectName(u"lbTitleScore")
        sizePolicy_FP.setHeightForWidth(self.lbTitleScore.sizePolicy().hasHeightForWidth())
        self.lbTitleScore.setSizePolicy(sizePolicy_FP)
        self.lbTitleScore.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbTitleScore, 0, 2, 1, 1, Qt.AlignHCenter)

        self.lbTitlePerson = QLabel(self.centralwidget)
        self.lbTitlePerson.setObjectName(u"lbTitlePerson")
        sizePolicy_FP.setHeightForWidth(self.lbTitlePerson.sizePolicy().hasHeightForWidth())
        self.lbTitlePerson.setSizePolicy(sizePolicy_FP)
        self.lbTitlePerson.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbTitlePerson, 0, 4, 1, 1, Qt.AlignHCenter)

        self.lbTitleRank = QLabel(self.centralwidget)
        self.lbTitleRank.setObjectName(u"lbTitleRank")
        sizePolicy_FP.setHeightForWidth(self.lbTitleRank.sizePolicy().hasHeightForWidth())
        self.lbTitleRank.setSizePolicy(sizePolicy_FP)
        self.lbTitleRank.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbTitleRank, 0, 3, 1, 1, Qt.AlignHCenter)

        self.lbTitleDel = QLabel(self.centralwidget)
        self.lbTitleDel.setObjectName(u"lbTitleDel")
        sizePolicy_FP.setHeightForWidth(self.lbTitleDel.sizePolicy().hasHeightForWidth())
        self.lbTitleDel.setSizePolicy(sizePolicy_FP)
        self.lbTitleDel.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbTitleDel, 0, 5, 1, 1, Qt.AlignHCenter)

        validator_score=QRegExpValidator(QRegExp(r'(100|[1-9][0-9]?(\.[1-9])?)'))
        validator_person=QRegExpValidator(QRegExp(r'[1-9][0-9][0-9]'))
        
        self.ent=[]
        self.del_btn=[]
        for k,(subject,num) in enumerate(zip(subjects,nums)):
            lbSubject = QLabel(self.centralwidget)
            lbSubject.setObjectName(u"lbSubject")
            sizePolicy_FP.setHeightForWidth(lbSubject.sizePolicy().hasHeightForWidth())
            lbSubject.setSizePolicy(sizePolicy_FP)
            lbSubject.setAlignment(Qt.AlignCenter)
            lbSubject.setText(QCoreApplication.translate("ExamInput", subject, None))
            self.glMain.addWidget(lbSubject, k+1, 0, 1, 1, Qt.AlignHCenter)

            lbNum = QLabel(self.centralwidget)
            lbNum.setObjectName(u"lbNum")
            sizePolicy_FP.setHeightForWidth(lbNum.sizePolicy().hasHeightForWidth())
            lbNum.setSizePolicy(sizePolicy_FP)
            lbNum.setAlignment(Qt.AlignCenter)
            lbNum.setText(QCoreApplication.translate("ExamInput", str(num), None))
            self.glMain.addWidget(lbNum, k+1, 1, 1, 1, Qt.AlignHCenter)

            lnScore = QLineEdit(self.centralwidget)
            lnScore.setObjectName(u"lnScore")
            sizePolicy_FF.setHeightForWidth(lnScore.sizePolicy().hasHeightForWidth())
            lnScore.setSizePolicy(sizePolicy_FF)
            lnScore.setMaximumSize(QSize(60, 16777215))
            lnScore.setAlignment(Qt.AlignCenter)
            lnScore.setValidator(validator_score)
            self.glMain.addWidget(lnScore, k+1, 2, 1, 1, Qt.AlignHCenter)

            lnRank = QLineEdit(self.centralwidget)
            lnRank.setObjectName(u"lnRank")
            sizePolicy_FF.setHeightForWidth(lnRank.sizePolicy().hasHeightForWidth())
            lnRank.setSizePolicy(sizePolicy_FF)
            lnRank.setMaximumSize(QSize(60, 16777215))
            lnRank.setAlignment(Qt.AlignCenter)
            lnRank.setValidator(validator_person)
            self.glMain.addWidget(lnRank, k+1, 3, 1, 1, Qt.AlignHCenter)

            lnPerson = QLineEdit(self.centralwidget)
            lnPerson.setObjectName(u"lnPerson")
            sizePolicy_FF.setHeightForWidth(lnPerson.sizePolicy().hasHeightForWidth())
            lnPerson.setSizePolicy(sizePolicy_FF)
            lnPerson.setMaximumSize(QSize(60, 16777215))
            lnPerson.setAlignment(Qt.AlignCenter)
            lnPerson.setValidator(validator_person)
            self.glMain.addWidget(lnPerson, k+1, 4, 1, 1, Qt.AlignHCenter)

            btnDel = QPushButton(self.centralwidget)
            btnDel.setObjectName(u"btnDel")
            sizePolicy_FF.setHeightForWidth(btnDel.sizePolicy().hasHeightForWidth())
            btnDel.setSizePolicy(sizePolicy_FF)
            btnDel.setMaximumSize(QSize(28, 16777215))
            btnDel.setText(QCoreApplication.translate("ExamInput", u"X", None))
            self.glMain.addWidget(btnDel, k+1, 5, 1, 1, Qt.AlignHCenter)
            
            self.ent.append((lnScore,lnRank,lnPerson))
            self.del_btn.append(btnDel)
        
        self.widBot = QWidget(self.centralwidget)
        self.widBot.setObjectName(u"widBot")
        
        self.hlBot = QHBoxLayout(self.widBot)
        self.hlBot.setSpacing(0)
        self.hlBot.setObjectName(u"hlBot")
        self.hlBot.setContentsMargins(0, 0, 0, 0)
        
        self.btnClear = QPushButton(self.widBot)
        self.btnClear.setObjectName(u"btnClear")
        sizePolicy_FF.setHeightForWidth(self.btnClear.sizePolicy().hasHeightForWidth())
        self.btnClear.setSizePolicy(sizePolicy_FF)
        self.hlBot.addWidget(self.btnClear)

        self.spH = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.hlBot.addItem(self.spH)

        self.btnCancel = QPushButton(self.widBot)
        self.btnCancel.setObjectName(u"btnCancel")
        sizePolicy_FF.setHeightForWidth(self.btnCancel.sizePolicy().hasHeightForWidth())
        self.btnCancel.setSizePolicy(sizePolicy_FF)
        self.hlBot.addWidget(self.btnCancel)

        self.btnSet = QPushButton(self.widBot)
        self.btnSet.setObjectName(u"btnSet")
        sizePolicy_FF.setHeightForWidth(self.btnSet.sizePolicy().hasHeightForWidth())
        self.btnSet.setSizePolicy(sizePolicy_FF)
        self.hlBot.addWidget(self.btnSet)
        
        self.glMain.addWidget(self.widBot, k+2, 0, 1, 6)

        ExamInput.setCentralWidget(self.centralwidget)

        self.retranslateUi(ExamInput)

        QMetaObject.connectSlotsByName(ExamInput)
    # setupUI

    def retranslateUi(self, ExamInput):
        ExamInput.setWindowTitle(QCoreApplication.translate("ExamInput", u"(\ucd5c\uc885)\uc131\uc801\uc785\ub825", None))
        self.lbTitleSubject.setText(QCoreApplication.translate("ExamInput", u"\uacfc\ubaa9\uba85", None))
        self.lbTitleNum.setText(QCoreApplication.translate("ExamInput", u"\ub2e8\uc704\uc218", None))
        self.lbTitleScore.setText(QCoreApplication.translate("ExamInput", u"\uc6d0\uc810\uc218", None))
        self.lbTitlePerson.setText(QCoreApplication.translate("ExamInput", u"\uc218\uac15\uc778\uc6d0", None))
        self.lbTitleRank.setText(QCoreApplication.translate("ExamInput", u"\uc11d\ucc28", None))
        self.lbTitleDel.setText(QCoreApplication.translate("ExamInput", u"\uc0ad\uc81c", None))
        self.btnClear.setText(QCoreApplication.translate("ExamInput", u"\ucd08\uae30\ud654", None))
        self.btnCancel.setText(QCoreApplication.translate("ExamInput", u"\ucde8\uc18c", None))
        self.btnSet.setText(QCoreApplication.translate("ExamInput", u"\uc785\ub825", None))
    # retranslateUi

class Ui_ExamResult(object):
    def setupUI(self, ExamResult, subjects,nums,scores,grades,ranks,percents,total_grade=None):
        if not ExamResult.objectName():
            ExamResult.setObjectName(u"ExamResult")
        ExamResult.resize(252, 72)
        self.centralwidget = QWidget(ExamResult)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.glMain = QGridLayout(self.centralwidget)
        self.glMain.setObjectName(u"glMain")
        self.glMain.setSpacing(20)

        self.lbTitleSubject = QLabel(self.centralwidget)
        self.lbTitleSubject.setObjectName(u"lbTitleSubject")
        self.lbTitleSubject.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbTitleSubject, 0, 0, 1, 1)
        
        self.lbTitleNum = QLabel(self.centralwidget)
        self.lbTitleNum.setObjectName(u"lbTitleNum")
        self.lbTitleNum.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbTitleNum, 0, 1, 1, 1)

        self.lbTitleScore = QLabel(self.centralwidget)
        self.lbTitleScore.setObjectName(u"lbTitleScore")
        self.lbTitleScore.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbTitleScore, 0, 2, 1, 1)

        self.lbTitleGrade = QLabel(self.centralwidget)
        self.lbTitleGrade.setObjectName(u"lbTitleGrade")
        self.lbTitleGrade.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbTitleGrade, 0, 3, 1, 1)

        self.lbTitleRank = QLabel(self.centralwidget)
        self.lbTitleRank.setObjectName(u"lbTitleRank")
        self.lbTitleRank.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbTitleRank, 0, 4, 1, 1)

        self.lbTitlePercent = QLabel(self.centralwidget)
        self.lbTitlePercent.setObjectName(u"lbTitlePercent")
        self.lbTitlePercent.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbTitlePercent, 0, 5, 1, 1)

        for k,(subject,num,score,grade,rank,percent) in\
        enumerate(zip(subjects,nums,scores,grades,ranks,percents)):
            lbSubject = QLabel(self.centralwidget)
            lbSubject.setObjectName(u"lbSubject")
            lbSubject.setAlignment(Qt.AlignCenter)
            lbSubject.setText(QCoreApplication.translate("ExamResult", subject, None))
            self.glMain.addWidget(lbSubject, k+1, 0, 1, 1)

            lbNum = QLabel(self.centralwidget)
            lbNum.setObjectName(u"lbNum")
            lbNum.setAlignment(Qt.AlignCenter)
            lbNum.setText(QCoreApplication.translate("ExamResult", str(num), None))
            self.glMain.addWidget(lbNum, k+1, 1, 1, 1)

            if score:
                lbScore = QLabel(self.centralwidget)
                lbScore.setObjectName(u"lbScore")
                lbScore.setAlignment(Qt.AlignCenter)
                lbScore.setText(QCoreApplication.translate("ExamResult", score, None))
                self.glMain.addWidget(lbScore, k+1, 2, 1, 1)
            
                if grade and ranks and percent:
                    lbGrade = QLabel(self.centralwidget)
                    lbGrade.setObjectName(u"lbGrade")
                    lbGrade.setAlignment(Qt.AlignCenter)
                    lbGrade.setText(QCoreApplication.translate("ExamResult", str(grade), None))
                    self.glMain.addWidget(lbGrade, k+1, 3, 1, 1)

                    lbRank = QLabel(self.centralwidget)
                    lbRank.setObjectName(u"lbRank")
                    lbRank.setAlignment(Qt.AlignCenter)
                    lbRank.setText(QCoreApplication.translate("ExamResult", rank, None))
                    self.glMain.addWidget(lbRank, k+1, 4, 1, 1)
                    
                    lbPercent = QLabel(self.centralwidget)
                    lbPercent.setObjectName(u"lbPercent")
                    lbPercent.setAlignment(Qt.AlignCenter)
                    lbPercent.setText(QCoreApplication.translate("ExamResult", str(percent), None))
                    self.glMain.addWidget(lbPercent, k+1, 5, 1, 1)
                else:
                    lbNoGrade = QLabel(self.centralwidget)
                    lbNoGrade.setObjectName(u"lbNoGrade")
                    lbNoGrade.setAlignment(Qt.AlignCenter)
                    lbNoGrade.setText(QCoreApplication.translate("ExamResult", '등수 미입력', None))
                    self.glMain.addWidget(lbNoGrade, k+1, 3, 1, 3)
            
            else:
                lbNoScore = QLabel(self.centralwidget)
                lbNoScore.setObjectName(u"lbNoScore")
                lbNoScore.setAlignment(Qt.AlignCenter)
                lbNoScore.setText(QCoreApplication.translate("ExamResult", '가채점 전', None))
                self.glMain.addWidget(lbNoScore, k+1, 2, 1, 4)
        
        if total_grade:
            k+=1
            lbTotalGrade = QLabel(self.centralwidget)
            lbTotalGrade.setObjectName(u"lbTotalGrade")
            lbTotalGrade.setAlignment(Qt.AlignCenter)
            lbTotalGrade.setText(QCoreApplication.translate("ExamResult", f'총합: {total_grade}', None))
            self.glMain.addWidget(lbTotalGrade, k+2, 5, 1, 1)
        
        self.widBot = QWidget(self.centralwidget)
        self.widBot.setObjectName(u"widBot")
        
        self.hlBot = QHBoxLayout(self.widBot)
        self.hlBot.setObjectName(u"hlBot")
        self.hlBot.setContentsMargins(0, 0, 0, 0)
        
        self.sp = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.hlBot.addItem(self.sp)

        self.btnClose = QPushButton(self.widBot)
        self.btnClose.setObjectName(u"btnClose")
        self.hlBot.addWidget(self.btnClose)
        self.glMain.addWidget(self.widBot, k+2, 0, 1, 6)

        ExamResult.setCentralWidget(self.centralwidget)

        self.retranslateUi(ExamResult)

        QMetaObject.connectSlotsByName(ExamResult)
    # setupUI

    def retranslateUi(self, ExamResult):
        ExamResult.setWindowTitle(QCoreApplication.translate("ExamResult", u"\uc2dc\ud5d8\uacb0\uacfc", None))
        self.lbTitleSubject.setText(QCoreApplication.translate("ExamResult", u"\uacfc\ubaa9", None))
        self.lbTitleNum.setText(QCoreApplication.translate("ExamResult", u"\uc2dc\uc218", None))
        self.lbTitleScore.setText(QCoreApplication.translate("ExamResult", u"\uc810\uc218", None))
        self.lbTitleGrade.setText(QCoreApplication.translate("ExamResult", u"\ub4f1\uae09", None))
        self.lbTitleRank.setText(QCoreApplication.translate("ExamResult", u"\uc11d\ucc28", None))
        self.lbTitlePercent.setText(QCoreApplication.translate("ExamResult", u"\ubc31\ubd84\uc704", None))
        self.btnClose.setText(QCoreApplication.translate("ExamResult", u"\ub2eb\uae30", None))
    # retranslateUi

class Ui_GradeCalc(object):
    def setupUI(self, GradeCalc):
        if not GradeCalc.objectName():
            GradeCalc.setObjectName(u"GradeCalc")
        
        self.centralwidget = QWidget(GradeCalc)
        self.centralwidget.setObjectName(u"centralwidget")
        self.glMain = QGridLayout(self.centralwidget)
        self.glMain.setObjectName(u"glMain")
        
        self.widCent = QWidget(self.centralwidget)
        self.widCent.setObjectName(u"widCent")
        self.glCent = QGridLayout(self.widCent)
        self.glCent.setObjectName(u"glCent")
        
        self.lbTitleSubject = QLabel(self.widCent)
        self.lbTitleSubject.setObjectName(u"lbTitleSubject")
        sizePolicy_FP.setHeightForWidth(self.lbTitleSubject.sizePolicy().hasHeightForWidth())
        self.lbTitleSubject.setSizePolicy(sizePolicy_FP)
        self.lbTitleSubject.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbTitleSubject, 0, 0, 1, 1, Qt.AlignHCenter)

        self.lbTitleNum = QLabel(self.widCent)
        self.lbTitleNum.setObjectName(u"lbTitleNum")
        sizePolicy_FP.setHeightForWidth(self.lbTitleNum.sizePolicy().hasHeightForWidth())
        self.lbTitleNum.setSizePolicy(sizePolicy_FP)
        self.lbTitleNum.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbTitleNum, 0, 1, 1, 1, Qt.AlignHCenter)

        self.lbTitleGrade1 = QLabel(self.widCent)
        self.lbTitleGrade1.setObjectName(u"lbTitleGrade1")
        sizePolicy_FP.setHeightForWidth(self.lbTitleGrade1.sizePolicy().hasHeightForWidth())
        self.lbTitleGrade1.setSizePolicy(sizePolicy_FP)
        self.lbTitleGrade1.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbTitleGrade1, 0, 2, 1, 1, Qt.AlignHCenter)

        self.lbTitleGrade2 = QLabel(self.widCent)
        self.lbTitleGrade2.setObjectName(u"lbTitleGrade2")
        sizePolicy_FP.setHeightForWidth(self.lbTitleGrade2.sizePolicy().hasHeightForWidth())
        self.lbTitleGrade2.setSizePolicy(sizePolicy_FP)
        self.lbTitleGrade2.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbTitleGrade2, 0, 3, 1, 1, Qt.AlignHCenter)

        self.lbTitleEnable = QLabel(self.widCent)
        self.lbTitleEnable.setObjectName(u"lbEnable")
        self.lbTitleEnable.setMaximumSize(QSize(37, 16777215))
        self.glCent.addWidget(self.lbTitleEnable, 0, 4, 1, 1, Qt.AlignHCenter)

        self.glMain.addWidget(self.widCent, 0, 0, 1, 1)

        self.widBot = QWidget(self.centralwidget)
        self.widBot.setObjectName(u"widBot")
        self.hlBot = QHBoxLayout(self.widBot)
        self.hlBot.setSpacing(0)
        self.hlBot.setObjectName(u"hlBot")
        self.hlBot.setContentsMargins(0, 0, 0, 0)
        
        self.btnCutCalc = QPushButton(self.widBot)
        self.btnCutCalc.setObjectName(u"btnCutCalc")
        sizePolicy_FF.setHeightForWidth(self.btnCutCalc.sizePolicy().hasHeightForWidth())
        self.btnCutCalc.setSizePolicy(sizePolicy_FF)
        self.hlBot.addWidget(self.btnCutCalc)

        self.spH = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlBot.addItem(self.spH)

        self.btnClear = QPushButton(self.widBot)
        self.btnClear.setObjectName(u"btnClear")
        sizePolicy_FF.setHeightForWidth(self.btnClear.sizePolicy().hasHeightForWidth())
        self.btnClear.setSizePolicy(sizePolicy_FF)
        self.hlBot.addWidget(self.btnClear)

        self.btnCalc = QPushButton(self.widBot)
        self.btnCalc.setObjectName(u"btnCalc")
        self.hlBot.addWidget(self.btnCalc)

        self.btnClose = QPushButton(self.widBot)
        self.btnClose.setObjectName(u"btnClose")
        sizePolicy_FF.setHeightForWidth(self.btnClose.sizePolicy().hasHeightForWidth())
        self.btnClose.setSizePolicy(sizePolicy_FF)
        self.hlBot.addWidget(self.btnClose)

        self.glMain.addWidget(self.widBot, 1, 0, 1, 1)

        GradeCalc.setCentralWidget(self.centralwidget)

        self.retranslateUi(GradeCalc)

        QMetaObject.connectSlotsByName(GradeCalc)
    # setupUi

    def retranslateUi(self, GradeCalc):
        GradeCalc.setWindowTitle(QCoreApplication.translate("GradeCalc", u"\uc608\uc0c1\ub4f1\uae09\uacc4\uc0b0", None))
        self.lbTitleSubject.setText(QCoreApplication.translate("GradeCalc", u"\uacfc\ubaa9\uba85", None))
        self.lbTitleNum.setText(QCoreApplication.translate("GradeCalc", u"\ub2e8\uc704\uc218", None))
        self.lbTitleGrade1.setText(QCoreApplication.translate("GradeCalc", u"\ub4f1\uae091", None))
        self.lbTitleGrade2.setText(QCoreApplication.translate("GradeCalc", u"\ub4f1\uae092", None))
        self.lbTitleEnable.setText(QCoreApplication.translate("GradeCalc", u"\ud3ec\ud568?", None))
        self.btnCutCalc.setText(QCoreApplication.translate("GradeCalc", u"\uadf9\uac04\uacc4\uc0b0", None))
        self.btnClear.setText(QCoreApplication.translate("GradeCalc", u"\ucd08\uae30\ud654", None))
        self.btnCalc.setText(QCoreApplication.translate("GradeCalc", u"\uacc4\uc0b0", None))
        self.btnClose.setText(QCoreApplication.translate("GradeCalc", u"\ub2eb\uae30", None))
    # retranslateUi

    def addWidgets(self,k,subject_name,subject_num):
        lbSubject = QLabel(self.widCent)
        lbSubject.setObjectName(u"lbSubject")
        sizePolicy_FP.setHeightForWidth(lbSubject.sizePolicy().hasHeightForWidth())
        lbSubject.setSizePolicy(sizePolicy_FP)
        lbSubject.setAlignment(Qt.AlignCenter)
        lbSubject.setText(QCoreApplication.translate("GradeCalc", subject_name, None))
        self.glCent.addWidget(lbSubject, k+1, 0, 1, 1, Qt.AlignHCenter)

        lbNum = QLabel(self.widCent)
        lbNum.setObjectName(u"lbNum")
        sizePolicy_IP.setHeightForWidth(lbNum.sizePolicy().hasHeightForWidth())
        lbNum.setSizePolicy(sizePolicy_IP)
        lbNum.setAlignment(Qt.AlignCenter)
        lbNum.setText(QCoreApplication.translate("GradeCalc", str(subject_num), None))
        self.glCent.addWidget(lbNum, k+1, 1, 1, 1, Qt.AlignHCenter)

        lnGrade1 = QLineEdit(self.widCent)
        lnGrade1.setObjectName(u"lnGrade1")
        sizePolicy_MF.setHeightForWidth(lnGrade1.sizePolicy().hasHeightForWidth())
        lnGrade1.setSizePolicy(sizePolicy_MF)
        lnGrade1.setMaximumSize(QSize(100, 16777215))
        lnGrade1.setAlignment(Qt.AlignCenter)
        lnGrade1.setValidator(VALIDATOR_NUM_1)
        self.glCent.addWidget(lnGrade1, k+1, 2, 1, 1)

        lnGrade2 = QLineEdit(self.widCent)
        lnGrade2.setObjectName(u"lnGrade2")
        sizePolicy_MF.setHeightForWidth(lnGrade2.sizePolicy().hasHeightForWidth())
        lnGrade2.setSizePolicy(sizePolicy_MF)
        lnGrade2.setMaximumSize(QSize(100, 16777215))
        lnGrade2.setAlignment(Qt.AlignCenter)
        lnGrade2.setValidator(VALIDATOR_NUM_1)
        self.glCent.addWidget(lnGrade2, k+1, 3, 1, 1)

        chkEnable = QCheckBox(self.widCent)
        chkEnable.setObjectName(u"chkEnable")
        chkEnable.setChecked(True)
        chkEnable.setText("")
        self.glCent.addWidget(chkEnable, k+1, 4, 1, 1, Qt.AlignHCenter)
        
        return lnGrade1,lnGrade2,chkEnable

class Ui_GradDetail(object):
    def setupUI(self, GradDetail):
        if not GradDetail.objectName():
            GradDetail.setObjectName(u"GradDetail")
        GradDetail.resize(207, 274)
        self.centralwidget = QWidget(GradDetail)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.glMain = QGridLayout(self.centralwidget)
        self.glMain.setObjectName(u"glMain")

        self.btnClose = QPushButton(self.centralwidget)
        self.btnClose.setObjectName(u"btnClose")
        sizePolicy_FF.setHeightForWidth(self.btnClose.sizePolicy().hasHeightForWidth())
        self.btnClose.setSizePolicy(sizePolicy_FF)
        self.glMain.addWidget(self.btnClose, 2, 2, 1, 1)

        GradDetail.setCentralWidget(self.centralwidget)

        self.retranslateUi(GradDetail)

        QMetaObject.connectSlotsByName(GradDetail)
    # setupUI

    def retranslateUi(self, GradDetail):
        GradDetail.setWindowTitle(QCoreApplication.translate("GradDetail", u"\uc0c1\uc138", None))
        self.btnClose.setText(QCoreApplication.translate("GradDetail", u"\ub2eb\uae30", None))
    # retranslateUi

    def addSel(self,err):
        lbTitle1Sel = QLabel(self.centralwidget)
        lbTitle1Sel.setObjectName(u"lbTitle1Sel")
        sizePolicy_FF.setHeightForWidth(lbTitle1Sel.sizePolicy().hasHeightForWidth())
        lbTitle1Sel.setSizePolicy(sizePolicy_FF)
        lbTitle1Sel.setText(QCoreApplication.translate("GradDetail", u"\uc120\n\ud0dd\n\ud615\n\uc624\n\ub2f5", None))
        self.glMain.addWidget(lbTitle1Sel, 0, 0, 1, 1,Qt.AlignCenter)
        
        self.widSel = QWidget(self.centralwidget)
        self.widSel.setObjectName(u"widSel")
        self.glSel = QGridLayout(self.widSel)
        self.glSel.setObjectName(u"glSel")

        lbTitle1Num = QLabel(self.widSel)
        lbTitle1Num.setObjectName(u"lbTitle1Num")
        lbTitle1Num.setAlignment(Qt.AlignCenter)
        lbTitle1Num.setText(QCoreApplication.translate("GradDetail", u"\ubc88\ud638", None))
        self.glSel.addWidget(lbTitle1Num, 0, 1, 1, 1)

        lbTitle1Ans = QLabel(self.widSel)
        lbTitle1Ans.setObjectName(u"lbTitle1Ans")
        lbTitle1Ans.setAlignment(Qt.AlignCenter)
        lbTitle1Ans.setText(QCoreApplication.translate("GradDetail", u"\uc751\ub2f5", None))
        self.glSel.addWidget(lbTitle1Ans, 0, 2, 1, 1)

        lbTitle1Cor = QLabel(self.widSel)
        lbTitle1Cor.setObjectName(u"lbTitle1Cor")
        lbTitle1Cor.setAlignment(Qt.AlignCenter)
        lbTitle1Cor.setText(QCoreApplication.translate("GradDetail", u"\uc815\ub2f5", None))
        self.glSel.addWidget(lbTitle1Cor, 0, 3, 1, 1)

        lbTitle1Score = QLabel(self.widSel)
        lbTitle1Score.setObjectName(u"lbTitle1Score")
        lbTitle1Score.setAlignment(Qt.AlignCenter)
        lbTitle1Score.setText(QCoreApplication.translate("GradDetail", u"\ubc30\uc810", None))
        self.glSel.addWidget(lbTitle1Score, 0, 4, 1, 1)

        list_lbNum   = []
        list_lbAns   = []
        list_lbCor   = []
        list_lbScore = []
        for k,num in enumerate(err):
            lbNum = QLabel(self.widSel)
            lbNum.setObjectName(u"lbNum")
            lbNum.setAlignment(Qt.AlignCenter)
            lbNum.setText(QCoreApplication.translate("GradDetail", str(num), None))
            self.glSel.addWidget(lbNum, k+1, 1, 1, 1)

            lbAns = QLabel(self.widSel)
            lbAns.setObjectName(u"lbAns")
            lbAns.setAlignment(Qt.AlignCenter)
            lbAns.setText(QCoreApplication.translate("GradDetail", str(err[num][0]), None))
            self.glSel.addWidget(lbAns, k+1, 2, 1, 1)

            lbCor = QLabel(self.widSel)
            lbCor.setObjectName(u"lbCor")
            lbCor.setAlignment(Qt.AlignCenter)
            lbCor.setText(QCoreApplication.translate("GradDetail", str(err[num][1]), None))
            self.glSel.addWidget(lbCor, k+1, 3, 1, 1)

            lbScore = QLabel(self.widSel)
            lbScore.setObjectName(u"lbScore")
            lbScore.setAlignment(Qt.AlignCenter)
            lbScore.setText(QCoreApplication.translate("GradDetail", err[num][2], None))
            self.glSel.addWidget(lbScore, k+1, 4, 1, 1)
            
            list_lbNum.append(lbNum)
            list_lbAns.append(lbAns)
            list_lbCor.append(lbCor)
            list_lbScore.append(lbScore)
            
            self.glMain.addWidget(self.widSel, 0, 1, 1, 2)
    
    def addSupply(self,err):
        lbTitle2Supply = QLabel(self.centralwidget)
        lbTitle2Supply.setObjectName(u"lbTitle2Supply")
        sizePolicy_FF.setHeightForWidth(lbTitle2Supply.sizePolicy().hasHeightForWidth())
        lbTitle2Supply.setSizePolicy(sizePolicy_FF)
        lbTitle2Supply.setText(QCoreApplication.translate("GradDetail", u"\uc11c\n\ub2f5\n\ud615\n\uc624\n\ub2f5", None))
        self.glMain.addWidget(lbTitle2Supply, 1, 0, 1, 1,Qt.AlignCenter)

        self.widSupply = QWidget(self.centralwidget)
        self.widSupply.setObjectName(u"widSupply")
        self.glSupply = QGridLayout(self.widSupply)
        self.glSupply.setObjectName(u"glSupply")

        lbTitle2Num = QLabel(self.widSupply)
        lbTitle2Num.setObjectName(u"lbTitle2Num")
        lbTitle2Num.setAlignment(Qt.AlignCenter)
        lbTitle2Num.setText(QCoreApplication.translate("GradDetail", u"\ubc88\ud638", None))
        self.glSupply.addWidget(lbTitle2Num, 0, 1, 1, 1)
        
        lbTitle2Get = QLabel(self.widSupply)
        lbTitle2Get.setObjectName(u"lbTitle2Get")
        lbTitle2Get.setAlignment(Qt.AlignCenter)
        lbTitle2Get.setText(QCoreApplication.translate("GradDetail", u"\ub4dd\uc810", None))
        self.glSupply.addWidget(lbTitle2Get, 0, 2, 1, 1)

        lbTitle2Score = QLabel(self.widSupply)
        lbTitle2Score.setObjectName(u"lbTitle2Score")
        lbTitle2Score.setAlignment(Qt.AlignCenter)
        lbTitle2Score.setText(QCoreApplication.translate("GradDetail", u"\ubc30\uc810", None))
        self.glSupply.addWidget(lbTitle2Score, 0, 3, 1, 1)

        list_lbNum   = []
        list_lbGet   = []
        list_lbScore = []
        for k,num in enumerate(err):
            lbNum = QLabel(self.widSel)
            lbNum.setObjectName(u"lbNum")
            lbNum.setAlignment(Qt.AlignCenter)
            lbNum.setText(QCoreApplication.translate("GradDetail", str(num), None))
            self.glSupply.addWidget(lbNum, k+1, 1, 1, 1)

            lbGet = QLabel(self.widSel)
            lbGet.setObjectName(u"lbGet")
            lbGet.setAlignment(Qt.AlignCenter)
            lbGet.setText(QCoreApplication.translate("GradDetail", err[num][0], None))
            self.glSupply.addWidget(lbGet, k+1, 2, 1, 1)

            lbScore = QLabel(self.widSel)
            lbScore.setObjectName(u"lbScore")
            lbScore.setAlignment(Qt.AlignCenter)
            lbScore.setText(QCoreApplication.translate("GradDetail", err[num][1], None))
            self.glSupply.addWidget(lbScore, k+1, 3, 1, 1)
            
            list_lbNum.append(lbNum)
            list_lbGet.append(lbGet)
            list_lbScore.append(lbScore)
            
            self.glMain.addWidget(self.widSupply, 0, 1, 1, 2)
        
        self.glMain.addWidget(self.widSupply, 1, 1, 1, 2)


class Ui_GradResult(object):
    def setupUI(self, GradResult):
        if not GradResult.objectName():
            GradResult.setObjectName(u"GradResult")
        GradResult.resize(218, 107)
        
        self.centralwidget = QWidget(GradResult)
        self.centralwidget.setObjectName(u"centralwidget")
        self.glMain = QGridLayout(self.centralwidget)
        self.glMain.setObjectName(u"glMain")
        l,_,r,b=self.glMain.getContentsMargins()
        self.glMain.setContentsMargins(l,0,r,b)
        
        self.widCent=QWidget(GradResult)
        self.glCent=QGridLayout(self.widCent)

        self.lbTitleSubject = QLabel(self.widCent)
        self.lbTitleSubject.setObjectName(u"lbTitleSubject")
        sizePolicy_PF.setHeightForWidth(self.lbTitleSubject.sizePolicy().hasHeightForWidth())
        self.lbTitleSubject.setSizePolicy(sizePolicy_PF)
        self.lbTitleSubject.setAlignment(Qt.AlignCenter)
        self.lbTitleSubject.setMinimumSize(self.lbTitleSubject.width(),28)
        self.glCent.addWidget(self.lbTitleSubject, 0, 0, 1, 1)

        self.lbTitleWrong = QLabel(self.widCent)
        self.lbTitleWrong.setObjectName(u"lbTitleWrong")
        sizePolicy_PF.setHeightForWidth(self.lbTitleWrong.sizePolicy().hasHeightForWidth())
        self.lbTitleWrong.setSizePolicy(sizePolicy_PF)
        self.lbTitleWrong.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbTitleWrong, 0, 1, 1, 1)
        
        self.lbTitleGrade = QLabel(self.widCent)
        self.lbTitleGrade.setObjectName(u"lbTitleGrade")
        sizePolicy_PF.setHeightForWidth(self.lbTitleGrade.sizePolicy().hasHeightForWidth())
        self.lbTitleGrade.setSizePolicy(sizePolicy_PF)
        self.lbTitleGrade.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbTitleGrade, 0, 2, 1, 1)

        self.lbTitleDetail = QLabel(self.widCent)
        self.lbTitleDetail.setObjectName(u"lbTitleDetail")
        sizePolicy_PF.setHeightForWidth(self.lbTitleDetail.sizePolicy().hasHeightForWidth())
        self.lbTitleDetail.setSizePolicy(sizePolicy_PF)
        self.lbTitleDetail.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbTitleDetail, 0, 3, 1, 1)

        self.lbTitleDel = QLabel(self.widCent)
        self.lbTitleDel.setObjectName(u"lbTitleDel")
        sizePolicy_PF.setHeightForWidth(self.lbTitleDel.sizePolicy().hasHeightForWidth())
        self.lbTitleDel.setSizePolicy(sizePolicy_PF)
        self.lbTitleDel.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbTitleDel, 0, 4, 1, 1)
        
        self.glMain.addWidget(self.widCent)

        self.widBot = QWidget(self.centralwidget)
        self.widBot.setObjectName(u"widBot")
        
        self.hlBot = QHBoxLayout(self.widBot)
        self.hlBot.setObjectName(u"hlBot")
        self.hlBot.setContentsMargins(0, 0, 0, 0)

        self.btnDel = QPushButton(self.widBot)
        self.btnDel.setObjectName(u"btnDel")
        self.hlBot.addWidget(self.btnDel)
        
        self.sp = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.hlBot.addItem(self.sp)

        self.btnClose = QPushButton(self.widBot)
        self.btnClose.setObjectName(u"btnClose")
        self.hlBot.addWidget(self.btnClose)
        
        self.glMain.addWidget(self.widBot, 2, 0, 1, 1)

        GradResult.setCentralWidget(self.centralwidget)

        self.retranslateUi(GradResult)

        QMetaObject.connectSlotsByName(GradResult)
    # setupUI

    def retranslateUi(self, GradResult):
        GradResult.setWindowTitle(QCoreApplication.translate("GradResult", u"\uac00\ucc44\uc810\uacb0\uacfc", None))
        self.lbTitleDetail.setText(QCoreApplication.translate("GradResult", u"\uc0c1\uc138", None))
        self.lbTitleSubject.setText(QCoreApplication.translate("GradResult", u"\uacfc\ubaa9\uba85", None))
        self.lbTitleGrade.setText(QCoreApplication.translate("GradResult", u"\uc810\uc218", None))
        self.lbTitleWrong.setText(QCoreApplication.translate("GradResult", u"\uc624\ub2f5 \uc218", None))
        self.lbTitleDel.setText(QCoreApplication.translate("GradResult", u"\uc0ad\uc81c", None))
        self.btnDel.setText(QCoreApplication.translate("ExamResult", u"삭제", None))
        self.btnClose.setText(QCoreApplication.translate("GradResult", u"\ub2eb\uae30", None))
    # retranslateUi
    
    def addWidgets(self,n,subject,score,err_cnt):
        lbSubject = QLabel(self.widCent)
        lbSubject.setObjectName(u"lbSubject")
        sizePolicy_PF.setHeightForWidth(lbSubject.sizePolicy().hasHeightForWidth())
        lbSubject.setSizePolicy(sizePolicy_PF)
        lbSubject.setAlignment(Qt.AlignCenter)
        lbSubject.setMinimumSize(lbSubject.width(),28)
        lbSubject.setText(QCoreApplication.translate("GradResult", subject, None))
        self.glCent.addWidget(lbSubject, n+1, 0, 1, 1)

        if not score:
            lbNoScore = QLabel(self.widCent)
            lbNoScore.setObjectName(u"lbNoScore")
            sizePolicy_PF.setHeightForWidth(lbNoScore.sizePolicy().hasHeightForWidth())
            lbNoScore.setSizePolicy(sizePolicy_PF)
            lbNoScore.setAlignment(Qt.AlignCenter)
            lbNoScore.setText(QCoreApplication.translate("GradResult", '채점 전', None))
            self.glCent.addWidget(lbNoScore, n+1, 1, 1, 4)
        else:
            chkDel=QCheckBox(self.widCent)
            self.glCent.addWidget(chkDel,n+1,4,1,1,Qt.AlignHCenter)
            
            if score==100:
                lbWrong = QLabel(self.widCent)
                lbWrong.setObjectName(u"lbWrong")
                sizePolicy_PF.setHeightForWidth(lbWrong.sizePolicy().hasHeightForWidth())
                lbWrong.setSizePolicy(sizePolicy_PF)
                lbWrong.setAlignment(Qt.AlignCenter)
                lbWrong.setText(QCoreApplication.translate("GradResult", '0', None))
                self.glCent.addWidget(lbWrong, n+1, 1, 1, 1)

                lbScore = QLabel(self.widCent)
                lbScore.setObjectName(u"lbScore")
                sizePolicy_PF.setHeightForWidth(lbScore.sizePolicy().hasHeightForWidth())
                lbScore.setSizePolicy(sizePolicy_PF)
                lbScore.setAlignment(Qt.AlignCenter)
                lbScore.setText(QCoreApplication.translate("GradResult", '100', None))
                self.glCent.addWidget(lbScore, n+1, 2, 1, 1)
                
                btnDetail=None
            else:
                lbWrong = QLabel(self.widCent)
                lbWrong.setObjectName(u"lbWrong")
                sizePolicy_PF.setHeightForWidth(lbWrong.sizePolicy().hasHeightForWidth())
                lbWrong.setSizePolicy(sizePolicy_PF)
                lbWrong.setAlignment(Qt.AlignCenter)
                lbWrong.setText(QCoreApplication.translate("GradResult", str(err_cnt), None))
                self.glCent.addWidget(lbWrong, n+1, 1, 1, 1)

                lbScore = QLabel(self.widCent)
                lbScore.setObjectName(u"lbScore")
                sizePolicy_PF.setHeightForWidth(lbScore.sizePolicy().hasHeightForWidth())
                lbScore.setSizePolicy(sizePolicy_PF)
                lbScore.setAlignment(Qt.AlignCenter)
                lbScore.setText(QCoreApplication.translate("GradResult", str(score), None))
                self.glCent.addWidget(lbScore, n+1, 2, 1, 1)
                
                btnDetail = QPushButton(self.widCent)
                btnDetail.setObjectName(u"btnDetail")
                btnDetail.setMaximumSize(QSize(50, 16777215))
                btnDetail.setText(QCoreApplication.translate("GradResult", u"\ubcf4\uae30", None))
                self.glCent.addWidget(btnDetail, n+1, 3, 1, 1)
            
            return (chkDel,btnDetail)



class Ui_Grading1(object):
    def setupUI(self, Grading1):
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

        self.retranslateUi(Grading1)

        QMetaObject.connectSlotsByName(Grading1)
    # setupUI

    def retranslateUi(self, Grading1):
        Grading1.setWindowTitle(QCoreApplication.translate("Grading1", u"\uacfc\ubaa9\uc120\ud0dd", None))
        self.btnNext.setText(QCoreApplication.translate("Grading1", u"\ub2e4\uc74c", None))
        self.lbSubject.setText(QCoreApplication.translate("Grading1", u"\uacfc\ubaa9:", None))
        self.btnBack.setText(QCoreApplication.translate("Grading1", u"\ucde8\uc18c", None))
    # retranslateUi

class Ui_Grading2(object):
    def setupUI(self, Grading2):
        if not Grading2.objectName():
            Grading2.setObjectName(u"Grading2")
        Grading2.resize(358, 218)
        self.centralwidget = QWidget(Grading2)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.glMain = QGridLayout(self.centralwidget)
        self.glMain.setObjectName(u"glMain")
        
        self.lbSubject = QLabel(self.centralwidget)
        self.lbSubject.setObjectName(u"lbSubject")
        sizePolicy_FF.setHeightForWidth(self.lbSubject.sizePolicy().hasHeightForWidth())
        self.lbSubject.setSizePolicy(sizePolicy_FF)
        self.glMain.addWidget(self.lbSubject, 0, 0, 2, 1)

        self.lb11 = QLabel(self.centralwidget)
        self.lb11.setObjectName(u"lb11")
        sizePolicy_IF.setHeightForWidth(self.lb11.sizePolicy().hasHeightForWidth())
        self.lb11.setSizePolicy(sizePolicy_IF)
        self.lb11.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lb11, 0, 1, 1, 1)

        self.lb12 = QLabel(self.centralwidget)
        self.lb12.setObjectName(u"lb12")
        sizePolicy_IF.setHeightForWidth(self.lb12.sizePolicy().hasHeightForWidth())
        self.lb12.setSizePolicy(sizePolicy_IF)
        self.lb12.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lb12, 0, 2, 1, 1)

        self.lb13 = QLabel(self.centralwidget)
        self.lb13.setObjectName(u"lb13")
        sizePolicy_IF.setHeightForWidth(self.lb13.sizePolicy().hasHeightForWidth())
        self.lb13.setSizePolicy(sizePolicy_IF)
        self.lb13.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lb13, 0, 3, 1, 1)

        self.lb21 = QLabel(self.centralwidget)
        self.lb21.setObjectName(u"lb21")
        sizePolicy_IF.setHeightForWidth(self.lb21.sizePolicy().hasHeightForWidth())
        self.lb21.setSizePolicy(sizePolicy_IF)
        self.lb21.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lb21, 1, 1, 1, 1)

        self.lb22 = QLabel(self.centralwidget)
        self.lb22.setObjectName(u"lb22")
        sizePolicy_IF.setHeightForWidth(self.lb22.sizePolicy().hasHeightForWidth())
        self.lb22.setSizePolicy(sizePolicy_IF)
        self.lb22.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lb22, 1, 2, 1, 1)

        self.lb23 = QLabel(self.centralwidget)
        self.lb23.setObjectName(u"lb23")
        sizePolicy_IF.setHeightForWidth(self.lb23.sizePolicy().hasHeightForWidth())
        self.lb23.setSizePolicy(sizePolicy_IF)
        self.lb23.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lb23, 1, 3, 1, 1)

        self.lbAns = QLabel(self.centralwidget)
        self.lbAns.setObjectName(u"lbAns")
        sizePolicy_FF.setHeightForWidth(self.lbAns.sizePolicy().hasHeightForWidth())
        self.lbAns.setSizePolicy(sizePolicy_FF)
        self.glMain.addWidget(self.lbAns, 2, 0, 2, 1)

        answerFont=QFont()
        answerFont.setLetterSpacing(QFont.PercentageSpacing,150)
        
        self.lnAns11 = QLineEdit(self.centralwidget)
        self.lnAns11.setObjectName(u"lnAns11")
        sizePolicy_FF.setHeightForWidth(self.lnAns11.sizePolicy().hasHeightForWidth())
        self.lnAns11.setSizePolicy(sizePolicy_FF)
        self.lnAns11.setMaximumSize(QSize(100, 26))
        self.lnAns11.setFont(answerFont)
        self.lnAns11.setMaxLength(9)
        self.lnAns11.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lnAns11, 2, 1, 1, 1)

        self.lnAns12 = QLineEdit(self.centralwidget)
        self.lnAns12.setObjectName(u"lnAns12")
        sizePolicy_FF.setHeightForWidth(self.lnAns12.sizePolicy().hasHeightForWidth())
        self.lnAns12.setSizePolicy(sizePolicy_FF)
        self.lnAns12.setMaximumSize(QSize(100, 26))
        self.lnAns12.setFont(answerFont)
        self.lnAns12.setMaxLength(9)
        self.lnAns12.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lnAns12, 2, 2, 1, 1)

        self.lnAns13 = QLineEdit(self.centralwidget)
        self.lnAns13.setObjectName(u"lnAns13")
        sizePolicy_FF.setHeightForWidth(self.lnAns13.sizePolicy().hasHeightForWidth())
        self.lnAns13.setSizePolicy(sizePolicy_FF)
        self.lnAns13.setMaximumSize(QSize(100, 26))
        self.lnAns13.setFont(answerFont)
        self.lnAns13.setMaxLength(9)
        self.lnAns13.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lnAns13, 2, 3, 1, 1)

        self.lnAns21 = QLineEdit(self.centralwidget)
        self.lnAns21.setObjectName(u"lnAns21")
        sizePolicy_FF.setHeightForWidth(self.lnAns21.sizePolicy().hasHeightForWidth())
        self.lnAns21.setSizePolicy(sizePolicy_FF)
        self.lnAns21.setMaximumSize(QSize(100, 26))
        self.lnAns21.setFont(answerFont)
        self.lnAns21.setMaxLength(9)
        self.lnAns21.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lnAns21, 3, 1, 1, 1)

        self.lnAns22 = QLineEdit(self.centralwidget)
        self.lnAns22.setObjectName(u"lnAns22")
        sizePolicy_FF.setHeightForWidth(self.lnAns22.sizePolicy().hasHeightForWidth())
        self.lnAns22.setSizePolicy(sizePolicy_FF)
        self.lnAns22.setMaximumSize(QSize(100, 26))
        self.lnAns22.setFont(answerFont)
        self.lnAns22.setMaxLength(9)
        self.lnAns22.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lnAns22, 3, 2, 1, 1)

        self.lnAns23 = QLineEdit(self.centralwidget)
        self.lnAns23.setObjectName(u"lnAns23")
        sizePolicy_FF.setHeightForWidth(self.lnAns23.sizePolicy().hasHeightForWidth())
        self.lnAns23.setSizePolicy(sizePolicy_FF)
        self.lnAns23.setMaximumSize(QSize(100, 26))
        self.lnAns23.setFont(answerFont)
        self.lnAns23.setMaxLength(9)
        self.lnAns23.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lnAns23, 3, 3, 1, 1)

        self.lbCor = QLabel(self.centralwidget)
        self.lbCor.setObjectName(u"lbCor")
        sizePolicy_FF.setHeightForWidth(self.lbCor.sizePolicy().hasHeightForWidth())
        self.lbCor.setSizePolicy(sizePolicy_FF)
        self.glMain.addWidget(self.lbCor, 4, 0, 2, 1)

        self.lnCor11 = QLineEdit(self.centralwidget)
        self.lnCor11.setObjectName(u"lnCor11")
        sizePolicy_FF.setHeightForWidth(self.lnCor11.sizePolicy().hasHeightForWidth())
        self.lnCor11.setSizePolicy(sizePolicy_FF)
        self.lnCor11.setMaximumSize(QSize(100, 26))
        self.lnCor11.setFont(answerFont)
        self.lnCor11.setMaxLength(9)
        self.lnCor11.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lnCor11, 4, 1, 1, 1)

        self.lnCor12 = QLineEdit(self.centralwidget)
        self.lnCor12.setObjectName(u"lnCor12")
        sizePolicy_FF.setHeightForWidth(self.lnCor12.sizePolicy().hasHeightForWidth())
        self.lnCor12.setSizePolicy(sizePolicy_FF)
        self.lnCor12.setMaximumSize(QSize(100, 26))
        self.lnCor12.setFont(answerFont)
        self.lnCor12.setMaxLength(9)
        self.lnCor12.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lnCor12, 4, 2, 1, 1)

        self.lnCor13 = QLineEdit(self.centralwidget)
        self.lnCor13.setObjectName(u"lnCor13")
        sizePolicy_FF.setHeightForWidth(self.lnCor13.sizePolicy().hasHeightForWidth())
        self.lnCor13.setSizePolicy(sizePolicy_FF)
        self.lnCor13.setMaximumSize(QSize(100, 26))
        self.lnCor13.setFont(answerFont)
        self.lnCor13.setMaxLength(9)
        self.lnCor13.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lnCor13, 4, 3, 1, 1)

        self.lnCor21 = QLineEdit(self.centralwidget)
        self.lnCor21.setObjectName(u"lnCor21")
        sizePolicy_FF.setHeightForWidth(self.lnCor21.sizePolicy().hasHeightForWidth())
        self.lnCor21.setSizePolicy(sizePolicy_FF)
        self.lnCor21.setMaximumSize(QSize(100, 26))
        self.lnCor21.setFont(answerFont)
        self.lnCor21.setMaxLength(9)
        self.lnCor21.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lnCor21, 5, 1, 1, 1)

        self.lnCor22 = QLineEdit(self.centralwidget)
        self.lnCor22.setObjectName(u"lnCor22")
        sizePolicy_FF.setHeightForWidth(self.lnCor22.sizePolicy().hasHeightForWidth())
        self.lnCor22.setSizePolicy(sizePolicy_FF)
        self.lnCor22.setMaximumSize(QSize(100, 26))
        self.lnCor22.setFont(answerFont)
        self.lnCor22.setMaxLength(9)
        self.lnCor22.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lnCor22, 5, 2, 1, 1)

        self.lnCor23 = QLineEdit(self.centralwidget)
        self.lnCor23.setObjectName(u"lnCor23")
        sizePolicy_FF.setHeightForWidth(self.lnCor23.sizePolicy().hasHeightForWidth())
        self.lnCor23.setSizePolicy(sizePolicy_FF)
        self.lnCor23.setMaximumSize(QSize(100, 26))
        self.lnCor23.setFont(answerFont)
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
        sizePolicy_FF.setHeightForWidth(self.btnBack.sizePolicy().hasHeightForWidth())
        self.btnBack.setSizePolicy(sizePolicy_FF)
        self.hlBot.addWidget(self.btnBack)

        self.sp1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlBot.addItem(self.sp1)

        self.btnRe = QPushButton(self.widBot)
        self.btnRe.setObjectName(u"btnRe")
        sizePolicy_FF.setHeightForWidth(self.btnRe.sizePolicy().hasHeightForWidth())
        self.btnRe.setSizePolicy(sizePolicy_FF)
        self.hlBot.addWidget(self.btnRe)

        self.sp2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlBot.addItem(self.sp2)

        self.btnNext = QPushButton(self.widBot)
        self.btnNext.setObjectName(u"btnNext")
        sizePolicy_FF.setHeightForWidth(self.btnNext.sizePolicy().hasHeightForWidth())
        self.btnNext.setSizePolicy(sizePolicy_FF)
        self.hlBot.addWidget(self.btnNext)
        self.glMain.addWidget(self.widBot, 6, 0, 1, 4)

        Grading2.setCentralWidget(self.centralwidget)

        self.retranslateUi(Grading2)

        QMetaObject.connectSlotsByName(Grading2)
    # setupUI

    def retranslateUi(self, Grading2):
        validator_answer =QRegExpValidator(QRegExp(r'[1-7]{5}'))
        validator_correct=QRegExpValidator(QRegExp(r'[0-5]{5}'))
        
        Grading2.setWindowTitle(QCoreApplication.translate("Grading2", u"\uac00\ucc44\uc810\uc785\ub825", None))
        self.lbSubject.setText(QCoreApplication.translate("Grading2", u"\uacfc\n\ubaa9", None))
        self.lb11.setText(QCoreApplication.translate("Grading2", u"1~5", None))
        self.lb12.setText(QCoreApplication.translate("Grading2", u"6~10", None))
        self.lb13.setText(QCoreApplication.translate("Grading2", u"11~15", None))
        self.lb21.setText(QCoreApplication.translate("Grading2", u"16~20", None))
        self.lb22.setText(QCoreApplication.translate("Grading2", u"21~25", None))
        self.lb23.setText(QCoreApplication.translate("Grading2", u"26~30", None))
        self.lbAns.setText(QCoreApplication.translate("Grading2", u"\uc751\n\ub2f5", None))
        
        self.lnAns11.setValidator(validator_answer)
        self.lnAns12.setValidator(validator_answer)
        self.lnAns13.setValidator(validator_answer)
        self.lnAns21.setValidator(validator_answer)
        self.lnAns22.setValidator(validator_answer)
        self.lnAns23.setValidator(validator_answer)
        self.lbCor.setText(QCoreApplication.translate("Grading2", u"\uc815\n\ub2f5", None))
        self.lnCor11.setValidator(validator_correct)
        self.lnCor12.setValidator(validator_correct)
        self.lnCor13.setValidator(validator_correct)
        self.lnCor21.setValidator(validator_correct)
        self.lnCor22.setValidator(validator_correct)
        self.lnCor23.setValidator(validator_correct)
        self.btnBack.setText(QCoreApplication.translate("Grading2", u"\uc774\uc804", None))
        self.btnRe.setText(QCoreApplication.translate("Grading2", u"\ub2e4\uc2dc", None))
        self.btnNext.setText(QCoreApplication.translate("Grading2", u"\ub2e4\uc74c", None))
    # retranslateUi

class Ui_Grading31(object):
    def setupUI(self, Grading31):
        if not Grading31.objectName():
            Grading31.setObjectName(u"Grading31")
        Grading31.resize(215, 103)
        self.centralwidget = QWidget(Grading31)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.glMain = QGridLayout(self.centralwidget)
        self.glMain.setObjectName(u"glMain")
        
        self.widCent=QWidget(Grading31)
        self.glCent=QGridLayout(self.widCent)
        
        self.lbNum = QLabel(self.widCent)
        self.lbNum.setObjectName(u"lbNum")
        self.lbNum.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbNum, 0, 0, 1, 1)

        self.lbPoint = QLabel(self.widCent)
        self.lbPoint.setObjectName(u"lbPoint")
        self.lbPoint.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbPoint, 0, 1, 1, 1)
        
        self.glMain.addWidget(self.widCent,0,0,1,1)

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
        self.glMain.addWidget(self.widBot, 1, 0, 1, 1)

        Grading31.setCentralWidget(self.centralwidget)

        self.retranslateUi(Grading31)

        QMetaObject.connectSlotsByName(Grading31)
    # setupUI

    def retranslateUi(self, Grading31):
        Grading31.setWindowTitle(QCoreApplication.translate("Grading31", u"\uc120\ud0dd\ud615 \ubc30\uc810", None))
        self.lbNum.setText(QCoreApplication.translate("Grading31", u"\ubc88\ud638", None))
        self.lbPoint.setText(QCoreApplication.translate("Grading31", u"\ubc30\uc810", None))
        self.btnBack.setText(QCoreApplication.translate("Grading31", u"\uc774\uc804", None))
        self.btnNext.setText(QCoreApplication.translate("Grading31", u"\ub2e4\uc74c", None))
    # retranslateUi
    
    def addWidgets(self,n,number):
        lbNo = QLabel(self.widCent)
        lbNo.setObjectName(u"lbNo")
        lbNo.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(lbNo, n+1, 0, 1, 1)
        lbNo.setText(QCoreApplication.translate("Grading31", str(number), None))
        
        lnScore = QLineEdit(self.widCent)
        lnScore.setObjectName(u"lineEdit")
        lnScore.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.glCent.addWidget(lnScore, n+1, 1, 1, 1)
        lnScore.setValidator(VALIDATOR_SCORE_IN)
        
        return lnScore

class Ui_Grading32(object):
    def setupUI(self, Grading32):
        if not Grading32.objectName():
            Grading32.setObjectName(u"Grading32")
        Grading32.resize(260, 104)
        self.centralwidget = QWidget(Grading32)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.glMain = QGridLayout(self.centralwidget)
        self.glMain.setObjectName(u"glMain")
        
        self.widCent=QWidget(Grading32)
        self.glCent=QGridLayout(self.widCent)
        
        self.lbTitleNo = QLabel(self.widCent)
        self.lbTitleNo.setObjectName(u"lbTitleNo")
        self.lbTitleNo.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbTitleNo, 0, 0, 1, 1)

        self.lbTitlePoint = QLabel(self.widCent)
        self.lbTitlePoint.setObjectName(u"lbTitlePoint")
        self.lbTitlePoint.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbTitlePoint, 0, 1, 1, 1)

        self.lbTitleGet = QLabel(self.widCent)
        self.lbTitleGet.setObjectName(u"lbTitleGet")
        self.lbTitleGet.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbTitleGet, 0, 2, 1, 1)
        
        self.glMain.addWidget(self.widCent,0,0,1,1)

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
        self.glMain.addWidget(self.widBot, 1, 0, 1, 1)

        Grading32.setCentralWidget(self.centralwidget)

        self.retranslateUi(Grading32)

        QMetaObject.connectSlotsByName(Grading32)
    # setupUI

    def retranslateUi(self, Grading32):
        Grading32.setWindowTitle(QCoreApplication.translate("Grading32", u"\uc11c\ub2f5\ud615 \ubc30\uc810", None))
        self.lbTitleNo.setText(QCoreApplication.translate("Grading32", u"\ubc88\ud638", None))
        self.lbTitlePoint.setText(QCoreApplication.translate("Grading32", u"\ub4dd\uc810", None))
        self.lbTitleGet.setText(QCoreApplication.translate("Grading32", u"\ubc30\uc810", None))
        self.btnBack.setText(QCoreApplication.translate("Grading32", u"\uc774\uc804", None))
        self.btnNext.setText(QCoreApplication.translate("Grading32", u"\ub2e4\uc74c", None))
    # retranslateUi
    
    def addWidgets(self,n,number):
        lbNo = QLabel(self.widCent)
        lbNo.setObjectName(u"lbNo")
        lbNo.setAlignment(Qt.AlignCenter)
        lbNo.setText(QCoreApplication.translate("Grading32", str(number), None))
        self.glCent.addWidget(lbNo, n+1, 0, 1, 1)

        lnPoint = QLineEdit(self.widCent)
        lnPoint.setObjectName(u"lnPoint")
        lnPoint.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        lnPoint.setValidator(VALIDATOR_SCORE_IN)
        self.glCent.addWidget(lnPoint, n+1, 1, 1, 1)

        lnGet = QLineEdit(self.widCent)
        lnGet.setObjectName(u"lnGet")
        lnGet.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        lnGet.setValidator(VALIDATOR_SCORE_IN)
        self.glCent.addWidget(lnGet, n+1, 2, 1, 1)
        
        return lnPoint,lnGet

class Ui_Main(object):
    def setupUI(self, Main, order):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(400, 300)
        
        self.save = QAction(Main)
        self.save.setObjectName(u"save")
        self.saveAs = QAction(Main)
        self.saveAs.setObjectName(u"saveAs")
        self.exit = QAction(Main)
        self.exit.setObjectName(u"exit")
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
        sizePolicy_EP.setHeightForWidth(self.widManage.sizePolicy().hasHeightForWidth())
        self.widManage.setSizePolicy(sizePolicy_EP)
        
        self.vlManage = QVBoxLayout(self.widManage)
        self.vlManage.setObjectName(u"vlManage")
        
        self.btnCalc = QPushButton(self.widManage)
        self.btnCalc.setObjectName(u"btnCalc")
        sizePolicy_EE.setHeightForWidth(self.btnCalc.sizePolicy().hasHeightForWidth())
        self.btnCalc.setSizePolicy(sizePolicy_EE)
        self.vlManage.addWidget(self.btnCalc)

        self.btnInput = QPushButton(self.widManage)
        self.btnInput.setObjectName(u"btnInput")
        sizePolicy_EE.setHeightForWidth(self.btnInput.sizePolicy().hasHeightForWidth())
        self.btnInput.setSizePolicy(sizePolicy_EE)
        self.vlManage.addWidget(self.btnInput)

        self.btnRes = QPushButton(self.widManage)
        self.btnRes.setObjectName(u"btnRes")
        sizePolicy_EE.setHeightForWidth(self.btnRes.sizePolicy().hasHeightForWidth())
        self.btnRes.setSizePolicy(sizePolicy_EE)
        self.vlManage.addWidget(self.btnRes)

        self.btnManage = QPushButton(self.widManage)
        self.btnManage.setObjectName(u"btnManage")
        sizePolicy_EE.setHeightForWidth(self.btnManage.sizePolicy().hasHeightForWidth())
        self.btnManage.setSizePolicy(sizePolicy_EE)
        self.vlManage.addWidget(self.btnManage)
        self.glMain.addWidget(self.widManage, 1, 1, 1, 1)

        self.widGrade = QGroupBox(self.centralwidget)
        self.widGrade.setObjectName(u"widGrade")
        sizePolicy_EP.setHeightForWidth(self.widGrade.sizePolicy().hasHeightForWidth())
        self.widGrade.setSizePolicy(sizePolicy_EP)
        
        self.vlGrade = QVBoxLayout(self.widGrade)
        self.vlGrade.setObjectName(u"vlGrade")
        
        self.btnSubject = QPushButton(self.widGrade)
        self.btnSubject.setObjectName(u"btnSubject")
        sizePolicy_EE.setHeightForWidth(self.btnSubject.sizePolicy().hasHeightForWidth())
        self.btnSubject.setSizePolicy(sizePolicy_EE)
        self.vlGrade.addWidget(self.btnSubject)

        self.btnGrading = QPushButton(self.widGrade)
        self.btnGrading.setObjectName(u"btnGrading")
        sizePolicy_EE.setHeightForWidth(self.btnGrading.sizePolicy().hasHeightForWidth())
        self.btnGrading.setSizePolicy(sizePolicy_EE)
        self.vlGrade.addWidget(self.btnGrading)

        self.btnGradingRes = QPushButton(self.widGrade)
        self.btnGradingRes.setObjectName(u"btnGradingRes")
        sizePolicy_EE.setHeightForWidth(self.btnGradingRes.sizePolicy().hasHeightForWidth())
        self.btnGradingRes.setSizePolicy(sizePolicy_EE)
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
        
        self.__option=(('1학년','2학년','3학년'),('1학기','2학기'),('중간고사','기말고사','학기말'))
        for option in self.__option[0]:
            self.comboYear.addItem(option)
            self.comboYear.setCurrentIndex(order[0])
        for option in self.__option[1]:
            self.comboSemester.addItem(option)
            self.comboSemester.setCurrentIndex(order[1])
        for option in self.__option[2]:
            self.comboExam.addItem(option)
            self.comboExam.setCurrentIndex(order[2])

        '''
        self.btnSet = QPushButton(self.widYear)
        self.btnSet.setObjectName(u"btnSet")
        sizePolicy_FF.setHeightForWidth(self.btnSet.sizePolicy().hasHeightForWidth())
        self.btnSet.setSizePolicy(sizePolicy_FF)
        self.hlYear.addWidget(self.btnSet)
        '''
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
        

        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.tools.menuAction())
        self.menubar.addAction(self.info.menuAction())
        
        self.file.addAction(self.load)
        self.file.addAction(self.save)
        self.file.addAction(self.saveAs)
        self.file.addSeparator()
        self.file.addAction(self.exit)
        
        self.tools.addAction(self.cut_calc)
        
        self.info.addAction(self.license)
        self.info.addSeparator()
        self.info.addAction(self.about)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUI

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"\uc131\uc801\uad00\ub9ac", None))
        self.save.setText(QCoreApplication.translate("Main", u"\uc800\uc7a5", None))
        self.saveAs.setText(QCoreApplication.translate("Main", u"\ub2e4\ub978 \uc774\ub984\uc73c\ub85c \uc800\uc7a5", None))
        self.exit.setText(QCoreApplication.translate("Main", u"\uc885\ub8cc", None))
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
        #self.btnSet.setText(QCoreApplication.translate("Main", u"\uc124\uc815", None))
        self.file.setTitle(QCoreApplication.translate("Main", u"\ud30c\uc77c", None))
        self.tools.setTitle(QCoreApplication.translate("Main", u"\ub3c4\uad6c", None))
        self.info.setTitle(QCoreApplication.translate("Main", u"\uc815\ubcf4", None))
    # retranslateUi


class Ui_SubjectIn(object):
    def setupUI(self, SubjectIn):
        if not SubjectIn.objectName():
            SubjectIn.setObjectName(u"SubjectIn")
        SubjectIn.resize(345, 110)
        
        self.centralwidget = QWidget(SubjectIn)
        self.centralwidget.setObjectName(u"centralwidget")
        self.glMain = QGridLayout(self.centralwidget)
        self.glMain.setObjectName(u"glMain")
        
        self.widCent=QWidget(SubjectIn)
        self.glCent=QGridLayout(self.widCent)
        
        self.lbTitleSubject = QLabel(self.widCent)
        self.lbTitleSubject.setObjectName(u"lbTitleSubject")
        sizePolicy_IP.setHeightForWidth(self.lbTitleSubject.sizePolicy().hasHeightForWidth())
        self.lbTitleSubject.setSizePolicy(sizePolicy_IP)
        self.lbTitleSubject.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbTitleSubject, 0, 0, 1, 1)

        self.lbTitleNum = QLabel(self.widCent)
        self.lbTitleNum.setObjectName(u"lbTitleNum")
        sizePolicy_IP.setHeightForWidth(self.lbTitleNum.sizePolicy().hasHeightForWidth())
        self.lbTitleNum.setSizePolicy(sizePolicy_IP)
        self.lbTitleNum.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbTitleNum, 0, 1, 1, 1)

        self.lbTitleMid = QLabel(self.widCent)
        self.lbTitleMid.setObjectName(u"lbTitleMid")
        sizePolicy_FP.setHeightForWidth(self.lbTitleMid.sizePolicy().hasHeightForWidth())
        self.lbTitleMid.setSizePolicy(sizePolicy_FP)
        self.lbTitleMid.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbTitleMid, 0, 2, 1, 1)

        self.lbTitleEnd = QLabel(self.widCent)
        self.lbTitleEnd.setObjectName(u"lbTitleEnd")
        sizePolicy_FP.setHeightForWidth(self.lbTitleEnd.sizePolicy().hasHeightForWidth())
        self.lbTitleEnd.setSizePolicy(sizePolicy_FP)
        self.lbTitleEnd.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbTitleEnd, 0, 3, 1, 1)

        self.lbTitleDel = QLabel(self.widCent)
        self.lbTitleDel.setObjectName(u"lbTitleDel")
        sizePolicy_FP.setHeightForWidth(self.lbTitleDel.sizePolicy().hasHeightForWidth())
        self.lbTitleDel.setSizePolicy(sizePolicy_FP)
        self.lbTitleDel.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbTitleDel, 0, 4, 1, 1)
        
        self.glMain.addWidget(self.widCent,1,0,1,1)

        self.widBot = QWidget(self.centralwidget)
        self.widBot.setObjectName(u"widBot")
        self.hlBot = QHBoxLayout(self.widBot)
        self.hlBot.setSpacing(0)
        self.hlBot.setObjectName(u"hlBot")
        self.hlBot.setContentsMargins(0, 0, 0, 0)
        self.btnAdd = QPushButton(self.widBot)
        self.btnAdd.setObjectName(u"btnAdd")
        sizePolicy_FF.setHeightForWidth(self.btnAdd.sizePolicy().hasHeightForWidth())
        self.btnAdd.setSizePolicy(sizePolicy_FF)
        self.hlBot.addWidget(self.btnAdd)

        self.sp = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlBot.addItem(self.sp)

        self.btnCancel = QPushButton(self.widBot)
        self.btnCancel.setObjectName(u"btnCancel")
        sizePolicy_FF.setHeightForWidth(self.btnCancel.sizePolicy().hasHeightForWidth())
        self.btnCancel.setSizePolicy(sizePolicy_FF)
        self.hlBot.addWidget(self.btnCancel)

        self.btnSet = QPushButton(self.widBot)
        self.btnSet.setObjectName(u"btnSet")
        sizePolicy_FF.setHeightForWidth(self.btnSet.sizePolicy().hasHeightForWidth())
        self.btnSet.setSizePolicy(sizePolicy_FF)
        self.hlBot.addWidget(self.btnSet)
        self.glMain.addWidget(self.widBot, 2, 0, 1, 1)

        SubjectIn.setCentralWidget(self.centralwidget)

        self.retranslateUi(SubjectIn)

        QMetaObject.connectSlotsByName(SubjectIn)
    # setupUI

    def retranslateUi(self, SubjectIn):
        SubjectIn.setWindowTitle(QCoreApplication.translate("SubjectIn", u"\uacfc\ubaa9\uc785\ub825", None))
        self.lbTitleSubject.setText(QCoreApplication.translate("SubjectIn", u"\uacfc\ubaa9\uba85", None))
        self.lbTitleNum.setText(QCoreApplication.translate("SubjectIn", u"\ub2e8\uc704\uc218", None))
        self.lbTitleMid.setText(QCoreApplication.translate("SubjectIn", u"\uc911\uac04", None))
        self.lbTitleEnd.setText(QCoreApplication.translate("SubjectIn", u"\uae30\ub9d0", None))
        self.lbTitleDel.setText(QCoreApplication.translate("SubjectIn", u"\uc0ad\uc81c", None))
        self.btnAdd.setText(QCoreApplication.translate("SubjectIn", u"\ucd94\uac00", None))
        self.btnCancel.setText(QCoreApplication.translate("SubjectIn", u"\ucde8\uc18c", None))
        self.btnSet.setText(QCoreApplication.translate("SubjectIn", u"\uc785\ub825", None))
    # retranslateUi
    
    def addWidgets(self,n,subject,values):
        assert type(subject) is str
        assert type(values) is tuple or type(values) is list 
        assert len(values)==3
        
        lnSubject = QLineEdit(self.widCent)
        lnSubject.setObjectName(u"lnSubject")
        lnSubject.setAlignment(Qt.AlignCenter)
        lnSubject.setText(subject)
        self.glCent.addWidget(lnSubject, n+1, 0, 1, 1)

        lnNum = QLineEdit(self.widCent)
        lnNum.setObjectName(u"lnNum")
        lnNum.setMaximumSize(QSize(45, 16777215))
        lnNum.setAlignment(Qt.AlignCenter)
        if values[0]:
            lnNum.setText(str(values[0]))
        self.glCent.addWidget(lnNum, n+1, 1, 1, 1)

        chkMid = QCheckBox(self.widCent)
        chkMid.setObjectName(u"chkMid")
        chkMid.setChecked(values[1])
        self.glCent.addWidget(chkMid, n+1, 2, 1, 1, Qt.AlignHCenter)

        chkEnd = QCheckBox(self.widCent)
        chkEnd.setObjectName(u"chkEnd")
        chkEnd.setChecked(values[2])
        self.glCent.addWidget(chkEnd, n+1, 3, 1, 1, Qt.AlignHCenter)

        btnDel = QPushButton(self.widCent)
        btnDel.setObjectName(u"btnDel")
        sizePolicy_IF.setHeightForWidth(btnDel.sizePolicy().hasHeightForWidth())
        btnDel.setSizePolicy(sizePolicy_IF)
        self.glCent.addWidget(btnDel, n+1, 4, 1, 1)
        
        lnNum.setValidator(VALIDATOR_NUM_1)
        chkMid.setText("")
        chkEnd.setText("")
        btnDel.setText(QCoreApplication.translate("SubjectIn", u"X", None))
        
        return [lnSubject,lnNum,chkMid,chkEnd,btnDel]
