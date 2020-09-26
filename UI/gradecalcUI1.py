# -*- coding: utf-8 -*-

class Ui_GradeCalc(object):
    def setupUi(self, GradeCalc):
        if not GradeCalc.objectName():
            GradeCalc.setObjectName(u"GradeCalc")
        #GradeCalc.setEnabled(True)
        GradeCalc.resize(434, 125)
        
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
        self.glCent.addWidget(self.lbTitleSubject, 0, 0, 1, 1)

        self.lbTitleNum = QLabel(self.widCent)
        self.lbTitleNum.setObjectName(u"lbTitleNum")
        sizePolicy_FP.setHeightForWidth(self.lbTitleNum.sizePolicy().hasHeightForWidth())
        self.lbTitleNum.setSizePolicy(sizePolicy_FP)
        self.lbTitleNum.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbTitleNum, 0, 1, 1, 1)

        self.lbTitleGrade1 = QLabel(self.widCent)
        self.lbTitleGrade1.setObjectName(u"lbTitleGrade1")
        sizePolicy_FP.setHeightForWidth(self.lbTitleGrade1.sizePolicy().hasHeightForWidth())
        self.lbTitleGrade1.setSizePolicy(sizePolicy_FP)
        self.lbTitleGrade1.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbTitleGrade1, 0, 2, 1, 1)

        self.lbTitleGrade2 = QLabel(self.widCent)
        self.lbTitleGrade2.setObjectName(u"lbTitleGrade2")
        sizePolicy_FP.setHeightForWidth(self.lbTitleGrade2.sizePolicy().hasHeightForWidth())
        self.lbTitleGrade2.setSizePolicy(sizePolicy_FP)
        self.lbTitleGrade2.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbTitleGrade2, 0, 3, 1, 1)

        self.lbEnable = QLabel(self.widCent)
        self.lbEnable.setObjectName(u"lbEnable")
        self.glCent.addWidget(self.lbEnable, 0, 4, 1, 1))

        self.glMain.addWidget(self.widCent, 0, 0, 1, 1)

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

        self.spH = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlBot.addItem(self.spH)

        self.btnCancel = QPushButton(self.widBot)
        self.btnCancel.setObjectName(u"btnCancel")
        sizePolicy_FF.setHeightForWidth(self.btnCancel.sizePolicy().hasHeightForWidth())
        self.btnCancel.setSizePolicy(sizePolicy_FF)
        self.hlBot.addWidget(self.btnCancel)

        self.btnCalc = QPushButton(self.widBot)
        self.btnCalc.setObjectName(u"btnCalc")
        self.hlBot.addWidget(self.btnCalc)

        self.btnSet = QPushButton(self.widBot)
        self.btnSet.setObjectName(u"btnSet")
        sizePolicy_FF.setHeightForWidth(self.btnSet.sizePolicy().hasHeightForWidth())
        self.btnSet.setSizePolicy(sizePolicy_FF)
        self.hlBot.addWidget(self.btnSet)

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
        self.lbEnable.setText(QCoreApplication.translate("GradeCalc", u"\ud3ec\ud568?", None))
        self.btnAdd.setText(QCoreApplication.translate("GradeCalc", u"\uadf9\uac04\uacc4\uc0b0", None))
        self.btnCancel.setText(QCoreApplication.translate("GradeCalc", u"\ucd08\uae30\ud654", None))
        self.btnCalc.setText(QCoreApplication.translate("GradeCalc", u"\uacc4\uc0b0", None))
        self.btnSet.setText(QCoreApplication.translate("GradeCalc", u"\ub2eb\uae30", None))
    # retranslateUi

    def makeWidgets(self,k,subject_name,subject_num):
        lbSubject = QLabel(self.widCent)
        lbSubject.setObjectName(u"lbSubject")
        sizePolicy_FP.setHeightForWidth(lbSubject.sizePolicy().hasHeightForWidth())
        lbSubject.setSizePolicy(sizePolicy_FP)
        lbSubject.setAlignment(Qt.AlignCenter)
        lbSubject.setText(QCoreApplication.translate("GradeCalc", subject_name, None))
        self.glCent.addWidget(lbSubject, k+1, 0, 1, 1)

        lbNum = QLabel(self.widCent)
        lbNum.setObjectName(u"lbNum")
        sizePolicy_IP.setHeightForWidth(lbNum.sizePolicy().hasHeightForWidth())
        lbNum.setSizePolicy(sizePolicy_IP)
        lbNum.setAlignment(Qt.AlignCenter)
        lbNum.setText(QCoreApplication.translate("GradeCalc", subject_num, None))
        self.glCent.addWidget(lbNum, k+1, 1, 1, 1)

        lnGrade1 = QLineEdit(self.widCent)
        lnGrade1.setObjectName(u"lnGrade1")
        sizePolicy_MF.setHeightForWidth(lnGrade1.sizePolicy().hasHeightForWidth())
        lnGrade1.setSizePolicy(sizePolicy_MF)
        lnGrade1.setMaximumSize(QSize(100, 16777215))
        lnGrade1.setAlignment(Qt.AlignCenter)
        lnGrade1.setInputMask(QCoreApplication.translate("GradeCalc", u"D", None))
        self.glCent.addWidget(lnGrade1, k+1, 2, 1, 1)

        lnGrade2 = QLineEdit(self.widCent)
        lnGrade2.setObjectName(u"lnGrade2")
        sizePolicy_MF.setHeightForWidth(lnGrade2.sizePolicy().hasHeightForWidth())
        lnGrade2.setSizePolicy(sizePolicy_MF)
        lnGrade2.setMaximumSize(QSize(100, 16777215))
        lnGrade2.setAlignment(Qt.AlignCenter)
        lnGrade2.setInputMask(QCoreApplication.translate("GradeCalc", u"d", None))
        self.glCent.addWidget(lnGrade2, k+1, 3, 1, 1)

        self.chkEnable = QCheckBox(self.widCent)
        self.chkEnable.setObjectName(u"chkEnable")
        self.chkEnable.setChecked(True)
        self.chkEnable.setText("")
        self.glCent.addWidget(self.chkEnable, k+1, 4, 1, 1, Qt.AlignHCenter)
        
        return lnGrade1,lnGrade2,chkEnable
