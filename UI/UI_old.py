# -*- coding: utf-8 -*-

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
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gbManage = QGroupBox(self.centralwidget)
        self.gbManage.setObjectName(u"gbManage")
        sizePolicy.setHeightForWidth(self.gbManage.sizePolicy().hasHeightForWidth())
        self.gbManage.setSizePolicy(sizePolicy)
        self.glManage = QGridLayout(self.gbManage)
        self.glManage.setObjectName(u"glManage")
        self.btnManage = QPushButton(self.gbManage)
        self.btnManage.setObjectName(u"btnManage")
        sizePolicy_EE.setHeightForWidth(self.btnManage.sizePolicy().hasHeightForWidth())
        self.btnManage.setSizePolicy(sizePolicy_EE)

        self.glManage.addWidget(self.btnManage, 3, 0, 1, 1)

        self.btnInput = QPushButton(self.gbManage)
        self.btnInput.setObjectName(u"btnInput")
        sizePolicy_EE.setHeightForWidth(self.btnInput.sizePolicy().hasHeightForWidth())
        self.btnInput.setSizePolicy(sizePolicy_EE)

        self.glManage.addWidget(self.btnInput, 1, 0, 1, 1)

        self.btnCalc = QPushButton(self.gbManage)
        self.btnCalc.setObjectName(u"btnCalc")
        sizePolicy_EE.setHeightForWidth(self.btnCalc.sizePolicy().hasHeightForWidth())
        self.btnCalc.setSizePolicy(sizePolicy_EE)

        self.glManage.addWidget(self.btnCalc, 0, 0, 1, 1)

        self.btnRes = QPushButton(self.gbManage)
        self.btnRes.setObjectName(u"btnRes")
        sizePolicy_EE.setHeightForWidth(self.btnRes.sizePolicy().hasHeightForWidth())
        self.btnRes.setSizePolicy(sizePolicy_EE)

        self.glManage.addWidget(self.btnRes, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.gbManage, 1, 1, 1, 1)

        self.gbGrade = QGroupBox(self.centralwidget)
        self.gbGrade.setObjectName(u"gbGrade")
        sizePolicy_EP.setHeightForWidth(self.gbGrade.sizePolicy().hasHeightForWidth())
        self.gbGrade.setSizePolicy(sizePolicy_EP)
        self.glGrade = QGridLayout(self.gbGrade)
        self.glGrade.setObjectName(u"glGrade")
        self.btnSubject = QPushButton(self.gbGrade)
        self.btnSubject.setObjectName(u"btnSubject")
        sizePolicy_EE.setHeightForWidth(self.btnSubject.sizePolicy().hasHeightForWidth())
        self.btnSubject.setSizePolicy(sizePolicy_EE)

        self.glGrade.addWidget(self.btnSubject, 0, 0, 1, 1)

        self.btnGrading = QPushButton(self.gbGrade)
        self.btnGrading.setObjectName(u"btnGrading")
        sizePolicy_EE.setHeightForWidth(self.btnGrading.sizePolicy().hasHeightForWidth())
        self.btnGrading.setSizePolicy(sizePolicy_EE)

        self.glGrade.addWidget(self.btnGrading, 1, 0, 1, 1)

        self.btnGradingRes = QPushButton(self.gbGrade)
        self.btnGradingRes.setObjectName(u"btnGradingRes")
        sizePolicy_EE.setHeightForWidth(self.btnGradingRes.sizePolicy().hasHeightForWidth())
        self.btnGradingRes.setSizePolicy(sizePolicy_EE)

        self.glGrade.addWidget(self.btnGradingRes, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.gbGrade, 1, 0, 1, 1)

        self.gbYear = QGroupBox(self.centralwidget)
        self.gbYear.setObjectName(u"gbYear")
        self.hlYear = QHBoxLayout(self.gbYear)
        self.hlYear.setObjectName(u"hlYear")
        self.comboYear = QComboBox(self.gbYear)
        self.comboYear.setObjectName(u"comboYear")

        self.hlYear.addWidget(self.comboYear)

        self.comboSemester = QComboBox(self.gbYear)
        self.comboSemester.setObjectName(u"comboSemester")

        self.hlYear.addWidget(self.comboSemester)

        self.comboExam = QComboBox(self.gbYear)
        self.comboExam.setObjectName(u"comboExam")

        self.hlYear.addWidget(self.comboExam)

        self.btnSet = QPushButton(self.gbYear)
        self.btnSet.setObjectName(u"btnSet")
        sizePolicy_FF.setHeightForWidth(self.btnSet.sizePolicy().hasHeightForWidth())
        self.btnSet.setSizePolicy(sizePolicy_FF)

        self.hlYear.addWidget(self.btnSet)


        self.gridLayout.addWidget(self.gbYear, 0, 0, 1, 2)

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
        Main.setWindowTitle(QCoreApplication.translate("Main", u"\\uc131\\uc801\\uad00\\ub9ac", None))
        self.save.setText(QCoreApplication.translate("Main", u"\\uc800\\uc7a5", None))
        self.exit.setText(QCoreApplication.translate("Main", u"\\uc885\\ub8cc", None))
        self.actiontest.setText(QCoreApplication.translate("Main", u"test", None))
        self.load.setText(QCoreApplication.translate("Main", u"\\ubd88\\ub7ec\\uc624\\uae30", None))
        self.cut_calc.setText(QCoreApplication.translate("Main", u"\\ub4f1\\uae09\\uc778\\uc6d0\\uacc4\\uc0b0", None))
        self.license.setText(QCoreApplication.translate("Main", u"License", None))
        self.about.setText(QCoreApplication.translate("Main", u"\\uc815\\ubcf4", None))
        self.gbManage.setTitle(QCoreApplication.translate("Main", u"\\uc131\\uc801\\uad00\\ub9ac", None))
        self.btnManage.setText(QCoreApplication.translate("Main", u"\\uc131\\uc801\\ucd94\\uc774", None))
        self.btnInput.setText(QCoreApplication.translate("Main", u"\\uc131\\uc801\\uc785\\ub825", None))
        self.btnCalc.setText(QCoreApplication.translate("Main", u"\\ub4f1\\uae09\\uacc4\\uc0b0", None))
        self.btnRes.setText(QCoreApplication.translate("Main", u"\\uc2dc\\ud5d8\\uacb0\\uacfc", None))
        self.gbGrade.setTitle(QCoreApplication.translate("Main", u"\\uac00\\ucc44\\uc810", None))
        self.btnSubject.setText(QCoreApplication.translate("Main", u"\\uacfc\\ubaa9 \\uc785\\ub825", None))
        self.btnGrading.setText(QCoreApplication.translate("Main", u"\\uac00\\ucc44\\uc810 \\uc785\\ub825", None))
        self.btnGradingRes.setText(QCoreApplication.translate("Main", u"\\uac00\\ucc44\\uc810 \\uacb0\\uacfc", None))
        self.gbYear.setTitle(QCoreApplication.translate("Main", u"\\ud559\\ub144\\ub3c4", None))
        self.btnSet.setText(QCoreApplication.translate("Main", u"\\uc124\\uc815", None))
        self.file.setTitle(QCoreApplication.translate("Main", u"\\ud30c\\uc77c", None))
        self.tools.setTitle(QCoreApplication.translate("Main", u"\\ub3c4\\uad6c", None))
        self.info.setTitle(QCoreApplication.translate("Main", u"\\uc815\\ubcf4", None))
    # retranslateUi


class Ui_SubjectIn(object):
    def setupUi(self, SubjectIn):
        if not SubjectIn.objectName():
            SubjectIn.setObjectName(u"SubjectIn")
        SubjectIn.resize(345, 110)
        self.centralwidget = QWidget(SubjectIn)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbSubject = QLabel(self.centralwidget)
        self.lbSubject.setObjectName(u"lbSubject")
        sizePolicy_IP.setHeightForWidth(self.lbSubject.sizePolicy().hasHeightForWidth())
        self.lbSubject.setSizePolicy(sizePolicy_IP)
        self.lbSubject.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbSubject, 0, 0, 1, 1)

        self.lbNum = QLabel(self.centralwidget)
        self.lbNum.setObjectName(u"lbNum")
        sizePolicy_IP.setHeightForWidth(self.lbNum.sizePolicy().hasHeightForWidth())
        self.lbNum.setSizePolicy(sizePolicy_IP)
        self.lbNum.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbNum, 0, 1, 1, 1)

        self.lbMid = QLabel(self.centralwidget)
        self.lbMid.setObjectName(u"lbMid")
        sizePolicy_FP.setHeightForWidth(self.lbMid.sizePolicy().hasHeightForWidth())
        self.lbMid.setSizePolicy(sizePolicy_FP)
        self.lbMid.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbMid, 0, 2, 1, 1)

        self.lbEnd = QLabel(self.centralwidget)
        self.lbEnd.setObjectName(u"lbEnd")
        sizePolicy_FP.setHeightForWidth(self.lbEnd.sizePolicy().hasHeightForWidth())
        self.lbEnd.setSizePolicy(sizePolicy_FP)
        self.lbEnd.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbEnd, 0, 3, 1, 1)

        self.lbDel = QLabel(self.centralwidget)
        self.lbDel.setObjectName(u"lbDel")
        sizePolicy_FP.setHeightForWidth(self.lbDel.sizePolicy().hasHeightForWidth())
        self.lbDel.setSizePolicy(sizePolicy_FP)
        self.lbDel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbDel, 0, 4, 1, 1)

        self.lnSubject = QLineEdit(self.centralwidget)
        self.lnSubject.setObjectName(u"lnSubject")
        self.lnSubject.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lnSubject, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(45, 16777215))
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.widMid = QWidget(self.centralwidget)
        self.widMid.setObjectName(u"widMid")
        self.horizontalLayout_2 = QHBoxLayout(self.widMid)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.chkWid = QCheckBox(self.widMid)
        self.chkWid.setObjectName(u"chkWid")

        self.horizontalLayout_2.addWidget(self.chkWid, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.widMid, 1, 2, 1, 1)

        self.widEnd = QWidget(self.centralwidget)
        self.widEnd.setObjectName(u"widEnd")
        self.horizontalLayout_3 = QHBoxLayout(self.widEnd)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.chkEnd = QCheckBox(self.widEnd)
        self.chkEnd.setObjectName(u"chkEnd")

        self.horizontalLayout_3.addWidget(self.chkEnd, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.widEnd, 1, 3, 1, 1)

        self.btnDel = QPushButton(self.centralwidget)
        self.btnDel.setObjectName(u"btnDel")
        sizePolicy_IF.setHeightForWidth(self.btnDel.sizePolicy().hasHeightForWidth())
        self.btnDel.setSizePolicy(sizePolicy_IF)

        self.gridLayout.addWidget(self.btnDel, 1, 4, 1, 1)

        self.widBot = QWidget(self.centralwidget)
        self.widBot.setObjectName(u"widBot")
        self.horizontalLayout = QHBoxLayout(self.widBot)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnAdd = QPushButton(self.widBot)
        self.btnAdd.setObjectName(u"btnAdd")
        sizePolicy_FF.setHeightForWidth(self.btnAdd.sizePolicy().hasHeightForWidth())
        self.btnAdd.setSizePolicy(sizePolicy_FF)

        self.horizontalLayout.addWidget(self.btnAdd)

        self.spH = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.spH)

        self.btnCancel = QPushButton(self.widBot)
        self.btnCancel.setObjectName(u"btnCancel")
        sizePolicy_FF.setHeightForWidth(self.btnCancel.sizePolicy().hasHeightForWidth())
        self.btnCancel.setSizePolicy(sizePolicy_FF)

        self.horizontalLayout.addWidget(self.btnCancel)

        self.btnSet = QPushButton(self.widBot)
        self.btnSet.setObjectName(u"btnSet")
        sizePolicy_FF.setHeightForWidth(self.btnSet.sizePolicy().hasHeightForWidth())
        self.btnSet.setSizePolicy(sizePolicy_FF)

        self.horizontalLayout.addWidget(self.btnSet)


        self.gridLayout.addWidget(self.widBot, 2, 0, 1, 5)

        SubjectIn.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.lnSubject, self.chkWid)
        QWidget.setTabOrder(self.chkWid, self.chkEnd)
        QWidget.setTabOrder(self.chkEnd, self.btnDel)
        QWidget.setTabOrder(self.btnDel, self.btnAdd)
        QWidget.setTabOrder(self.btnAdd, self.btnSet)
        QWidget.setTabOrder(self.btnSet, self.btnCancel)

        self.retranslateUi(SubjectIn)

        QMetaObject.connectSlotsByName(SubjectIn)
    # setupUi

    def retranslateUi(self, SubjectIn):
        SubjectIn.setWindowTitle(QCoreApplication.translate("SubjectIn", u"\\uacfc\\ubaa9\\uc785\\ub825", None))
        self.lbSubject.setText(QCoreApplication.translate("SubjectIn", u"\\uacfc\\ubaa9\\uba85", None))
        self.lbNum.setText(QCoreApplication.translate("SubjectIn", u"\\ub2e8\\uc704\\uc218", None))
        self.lbMid.setText(QCoreApplication.translate("SubjectIn", u"\\uc911\\uac04", None))
        self.lbEnd.setText(QCoreApplication.translate("SubjectIn", u"\\uae30\\ub9d0", None))
        self.lbDel.setText(QCoreApplication.translate("SubjectIn", u"\\uc0ad\\uc81c", None))
        self.lineEdit.setInputMask(QCoreApplication.translate("SubjectIn", u"D", None))
        self.chkWid.setText("")
        self.chkEnd.setText("")
        self.btnDel.setText(QCoreApplication.translate("SubjectIn", u"X", None))
        self.btnAdd.setText(QCoreApplication.translate("SubjectIn", u"\\ucd94\\uac00", None))
        self.btnCancel.setText(QCoreApplication.translate("SubjectIn", u"\\ucde8\\uc18c", None))
        self.btnSet.setText(QCoreApplication.translate("SubjectIn", u"\\uc785\\ub825", None))
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

        self.retranslateUi(Grading1)

        QMetaObject.connectSlotsByName(Grading1)
    # setupUi

    def retranslateUi(self, Grading1):
        Grading1.setWindowTitle(QCoreApplication.translate("Grading1", u"\\uacfc\\ubaa9\\uc120\\ud0dd", None))
        self.btnNext.setText(QCoreApplication.translate("Grading1", u"\\ub2e4\\uc74c", None))
        self.lbSubject.setText(QCoreApplication.translate("Grading1", u"\\uacfc\\ubaa9:", None))
        self.btnBack.setText(QCoreApplication.translate("Grading1", u"\\ucde8\\uc18c", None))
    # retranslateUi



class Ui_Grading2(object):
    def setupUi(self, Grading2):
        if not Grading2.objectName():
            Grading2.setObjectName(u"Grading2")
        Grading2.resize(358, 218)
        self.centralwidget = QWidget(Grading2)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbSubject = QLabel(self.centralwidget)
        self.lbSubject.setObjectName(u"lbSubject")
        sizePolicy_FF.setHeightForWidth(self.lbSubject.sizePolicy().hasHeightForWidth())
        self.lbSubject.setSizePolicy(sizePolicy_FF)

        self.gridLayout.addWidget(self.lbSubject, 0, 0, 2, 1)

        self.lb15 = QLabel(self.centralwidget)
        self.lb15.setObjectName(u"lb15")
        sizePolicy_IF.setHeightForWidth(self.lb15.sizePolicy().hasHeightForWidth())
        self.lb15.setSizePolicy(sizePolicy_IF)
        self.lb15.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb15, 0, 1, 1, 1)

        self.lb610 = QLabel(self.centralwidget)
        self.lb610.setObjectName(u"lb610")
        sizePolicy_IF.setHeightForWidth(self.lb610.sizePolicy().hasHeightForWidth())
        self.lb610.setSizePolicy(sizePolicy_IF)
        self.lb610.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb610, 0, 2, 1, 1)

        self.lb1115 = QLabel(self.centralwidget)
        self.lb1115.setObjectName(u"lb1115")
        sizePolicy_IF.setHeightForWidth(self.lb1115.sizePolicy().hasHeightForWidth())
        self.lb1115.setSizePolicy(sizePolicy_IF)
        self.lb1115.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb1115, 0, 3, 1, 1)

        self.lb1620 = QLabel(self.centralwidget)
        self.lb1620.setObjectName(u"lb1620")
        sizePolicy_IF.setHeightForWidth(self.lb1620.sizePolicy().hasHeightForWidth())
        self.lb1620.setSizePolicy(sizePolicy_IF)
        self.lb1620.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb1620, 1, 1, 1, 1)

        self.lb2125 = QLabel(self.centralwidget)
        self.lb2125.setObjectName(u"lb2125")
        sizePolicy_IF.setHeightForWidth(self.lb2125.sizePolicy().hasHeightForWidth())
        self.lb2125.setSizePolicy(sizePolicy_IF)
        self.lb2125.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb2125, 1, 2, 1, 1)

        self.lb2630 = QLabel(self.centralwidget)
        self.lb2630.setObjectName(u"lb2630")
        sizePolicy_IF.setHeightForWidth(self.lb2630.sizePolicy().hasHeightForWidth())
        self.lb2630.setSizePolicy(sizePolicy_IF)
        self.lb2630.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb2630, 1, 3, 1, 1)

        self.lbAns = QLabel(self.centralwidget)
        self.lbAns.setObjectName(u"lbAns")
        sizePolicy_FF.setHeightForWidth(self.lbAns.sizePolicy().hasHeightForWidth())
        self.lbAns.setSizePolicy(sizePolicy_FF)

        self.gridLayout.addWidget(self.lbAns, 2, 0, 2, 1)

        self.lnAns15 = QLineEdit(self.centralwidget)
        self.lnAns15.setObjectName(u"lnAns15")
        sizePolicy_FF.setHeightForWidth(self.lnAns15.sizePolicy().hasHeightForWidth())
        self.lnAns15.setSizePolicy(sizePolicy_FF)
        self.lnAns15.setMaximumSize(QSize(100, 24))
        self.lnAns15.setStyleSheet(u"padding:16px")
        self.lnAns15.setMaxLength(9)
        self.lnAns15.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lnAns15, 2, 1, 1, 1)

        self.lnAns610 = QLineEdit(self.centralwidget)
        self.lnAns610.setObjectName(u"lnAns610")
        sizePolicy_FF.setHeightForWidth(self.lnAns610.sizePolicy().hasHeightForWidth())
        self.lnAns610.setSizePolicy(sizePolicy_FF)
        self.lnAns610.setMaximumSize(QSize(100, 24))
        self.lnAns610.setStyleSheet(u"padding:16px")
        self.lnAns610.setMaxLength(9)
        self.lnAns610.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lnAns610, 2, 2, 1, 1)

        self.lnAns1115 = QLineEdit(self.centralwidget)
        self.lnAns1115.setObjectName(u"lnAns1115")
        sizePolicy_FF.setHeightForWidth(self.lnAns1115.sizePolicy().hasHeightForWidth())
        self.lnAns1115.setSizePolicy(sizePolicy_FF)
        self.lnAns1115.setMaximumSize(QSize(100, 24))
        self.lnAns1115.setStyleSheet(u"padding:16px")
        self.lnAns1115.setMaxLength(9)
        self.lnAns1115.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lnAns1115, 2, 3, 1, 1)

        self.lnAns1620 = QLineEdit(self.centralwidget)
        self.lnAns1620.setObjectName(u"lnAns1620")
        sizePolicy_FF.setHeightForWidth(self.lnAns1620.sizePolicy().hasHeightForWidth())
        self.lnAns1620.setSizePolicy(sizePolicy_FF)
        self.lnAns1620.setMaximumSize(QSize(100, 24))
        self.lnAns1620.setStyleSheet(u"padding:16px")
        self.lnAns1620.setMaxLength(9)
        self.lnAns1620.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lnAns1620, 3, 1, 1, 1)

        self.lnAns2125 = QLineEdit(self.centralwidget)
        self.lnAns2125.setObjectName(u"lnAns2125")
        sizePolicy_FF.setHeightForWidth(self.lnAns2125.sizePolicy().hasHeightForWidth())
        self.lnAns2125.setSizePolicy(sizePolicy_FF)
        self.lnAns2125.setMaximumSize(QSize(100, 24))
        self.lnAns2125.setStyleSheet(u"padding:16px")
        self.lnAns2125.setMaxLength(9)
        self.lnAns2125.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lnAns2125, 3, 2, 1, 1)

        self.lnAns2630 = QLineEdit(self.centralwidget)
        self.lnAns2630.setObjectName(u"lnAns2630")
        sizePolicy_FF.setHeightForWidth(self.lnAns2630.sizePolicy().hasHeightForWidth())
        self.lnAns2630.setSizePolicy(sizePolicy_FF)
        self.lnAns2630.setMaximumSize(QSize(100, 24))
        self.lnAns2630.setStyleSheet(u"padding:16px")
        self.lnAns2630.setMaxLength(9)
        self.lnAns2630.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lnAns2630, 3, 3, 1, 1)

        self.lbCor = QLabel(self.centralwidget)
        self.lbCor.setObjectName(u"lbCor")
        sizePolicy_FF.setHeightForWidth(self.lbCor.sizePolicy().hasHeightForWidth())
        self.lbCor.setSizePolicy(sizePolicy_FF)

        self.gridLayout.addWidget(self.lbCor, 4, 0, 2, 1)

        self.lnCor15 = QLineEdit(self.centralwidget)
        self.lnCor15.setObjectName(u"lnCor15")
        sizePolicy_FF.setHeightForWidth(self.lnCor15.sizePolicy().hasHeightForWidth())
        self.lnCor15.setSizePolicy(sizePolicy_FF)
        self.lnCor15.setMaximumSize(QSize(100, 24))
        self.lnCor15.setStyleSheet(u"padding:16px")
        self.lnCor15.setMaxLength(9)
        self.lnCor15.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lnCor15, 4, 1, 1, 1)

        self.lnCor610 = QLineEdit(self.centralwidget)
        self.lnCor610.setObjectName(u"lnCor610")
        sizePolicy_FF.setHeightForWidth(self.lnCor610.sizePolicy().hasHeightForWidth())
        self.lnCor610.setSizePolicy(sizePolicy_FF)
        self.lnCor610.setMaximumSize(QSize(100, 24))
        self.lnCor610.setStyleSheet(u"padding:16px")
        self.lnCor610.setMaxLength(9)
        self.lnCor610.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lnCor610, 4, 2, 1, 1)

        self.lnCor1115 = QLineEdit(self.centralwidget)
        self.lnCor1115.setObjectName(u"lnCor1115")
        sizePolicy_FF.setHeightForWidth(self.lnCor1115.sizePolicy().hasHeightForWidth())
        self.lnCor1115.setSizePolicy(sizePolicy_FF)
        self.lnCor1115.setMaximumSize(QSize(100, 24))
        self.lnCor1115.setStyleSheet(u"padding:16px")
        self.lnCor1115.setMaxLength(9)
        self.lnCor1115.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lnCor1115, 4, 3, 1, 1)

        self.lnCor1620 = QLineEdit(self.centralwidget)
        self.lnCor1620.setObjectName(u"lnCor1620")
        sizePolicy_FF.setHeightForWidth(self.lnCor1620.sizePolicy().hasHeightForWidth())
        self.lnCor1620.setSizePolicy(sizePolicy_FF)
        self.lnCor1620.setMaximumSize(QSize(100, 24))
        self.lnCor1620.setStyleSheet(u"padding:16px")
        self.lnCor1620.setMaxLength(9)
        self.lnCor1620.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lnCor1620, 5, 1, 1, 1)

        self.lnCor2125 = QLineEdit(self.centralwidget)
        self.lnCor2125.setObjectName(u"lnCor2125")
        sizePolicy_FF.setHeightForWidth(self.lnCor2125.sizePolicy().hasHeightForWidth())
        self.lnCor2125.setSizePolicy(sizePolicy_FF)
        self.lnCor2125.setMaximumSize(QSize(100, 24))
        self.lnCor2125.setStyleSheet(u"padding:16px")
        self.lnCor2125.setMaxLength(9)
        self.lnCor2125.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lnCor2125, 5, 2, 1, 1)

        self.lnCor2630 = QLineEdit(self.centralwidget)
        self.lnCor2630.setObjectName(u"lnCor2630")
        sizePolicy_FF.setHeightForWidth(self.lnCor2630.sizePolicy().hasHeightForWidth())
        self.lnCor2630.setSizePolicy(sizePolicy_FF)
        self.lnCor2630.setMaximumSize(QSize(100, 24))
        self.lnCor2630.setStyleSheet(u"padding:16px")
        self.lnCor2630.setMaxLength(9)
        self.lnCor2630.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lnCor2630, 5, 3, 1, 1)

        self.widBot = QWidget(self.centralwidget)
        self.widBot.setObjectName(u"widBot")
        self.horizontalLayout_2 = QHBoxLayout(self.widBot)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnBack_2 = QPushButton(self.widBot)
        self.btnBack_2.setObjectName(u"btnBack_2")
        sizePolicy_FF.setHeightForWidth(self.btnBack_2.sizePolicy().hasHeightForWidth())
        self.btnBack_2.setSizePolicy(sizePolicy_FF)

        self.horizontalLayout_2.addWidget(self.btnBack_2)

        self.sp1_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.sp1_2)

        self.btnRe_2 = QPushButton(self.widBot)
        self.btnRe_2.setObjectName(u"btnRe_2")
        sizePolicy_FF.setHeightForWidth(self.btnRe_2.sizePolicy().hasHeightForWidth())
        self.btnRe_2.setSizePolicy(sizePolicy_FF)

        self.horizontalLayout_2.addWidget(self.btnRe_2)

        self.sp2_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.sp2_2)

        self.btnNext_2 = QPushButton(self.widBot)
        self.btnNext_2.setObjectName(u"btnNext_2")
        sizePolicy_FF.setHeightForWidth(self.btnNext_2.sizePolicy().hasHeightForWidth())
        self.btnNext_2.setSizePolicy(sizePolicy_FF)

        self.horizontalLayout_2.addWidget(self.btnNext_2)


        self.gridLayout.addWidget(self.widBot, 6, 0, 1, 4)

        Grading2.setCentralWidget(self.centralwidget)

        self.retranslateUi(Grading2)

        QMetaObject.connectSlotsByName(Grading2)
    # setupUi

    def retranslateUi(self, Grading2):
        Grading2.setWindowTitle(QCoreApplication.translate("Grading2", u"\\uac00\\ucc44\\uc810\\uc785\\ub825", None))
        self.lbSubject.setText(QCoreApplication.translate("Grading2", u"\\uacfc\\n"
"\\ubaa9", None))
        self.lb15.setText(QCoreApplication.translate("Grading2", u"1~5", None))
        self.lb610.setText(QCoreApplication.translate("Grading2", u"6~10", None))
        self.lb1115.setText(QCoreApplication.translate("Grading2", u"11~15", None))
        self.lb1620.setText(QCoreApplication.translate("Grading2", u"16~20", None))
        self.lb2125.setText(QCoreApplication.translate("Grading2", u"21~25", None))
        self.lb2630.setText(QCoreApplication.translate("Grading2", u"26~30", None))
        self.lbAns.setText(QCoreApplication.translate("Grading2", u"\\uc751\\n"
"\\ub2f5", None))
        self.lnAns15.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnAns610.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnAns1115.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnAns1620.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnAns2125.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnAns2630.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lbCor.setText(QCoreApplication.translate("Grading2", u"\\uc815\\n"
"\\ub2f5", None))
        self.lnCor15.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnCor610.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnCor1115.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnCor1620.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnCor2125.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.lnCor2630.setInputMask(QCoreApplication.translate("Grading2", u"D D D D D", None))
        self.btnBack_2.setText(QCoreApplication.translate("Grading2", u"\\uc774\\uc804", None))
        self.btnRe_2.setText(QCoreApplication.translate("Grading2", u"\\ub2e4\\uc2dc", None))
        self.btnNext_2.setText(QCoreApplication.translate("Grading2", u"\\ub2e4\\uc74c", None))
    # retranslateUi


class Ui_Grading31(object):
    def setupUi(self, Grading31):
        if not Grading31.objectName():
            Grading31.setObjectName(u"Grading31")
        Grading31.resize(215, 103)
        self.centralwidget = QWidget(Grading31)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbNum = QLabel(self.centralwidget)
        self.lbNum.setObjectName(u"lbNum")
        self.lbNum.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbNum, 0, 0, 1, 1)

        self.lbPoint = QLabel(self.centralwidget)
        self.lbPoint.setObjectName(u"lbPoint")
        self.lbPoint.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbPoint, 0, 1, 1, 1)

        self.lbNo = QLabel(self.centralwidget)
        self.lbNo.setObjectName(u"lbNo")
        self.lbNo.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbNo, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.widBot = QWidget(self.centralwidget)
        self.widBot.setObjectName(u"widBot")
        self.horizontalLayout_3 = QHBoxLayout(self.widBot)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnBack = QPushButton(self.widBot)
        self.btnBack.setObjectName(u"btnBack")

        self.horizontalLayout_3.addWidget(self.btnBack)

        self.spH = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.spH)

        self.btnNext = QPushButton(self.widBot)
        self.btnNext.setObjectName(u"btnNext")

        self.horizontalLayout_3.addWidget(self.btnNext)


        self.gridLayout.addWidget(self.widBot, 2, 0, 1, 2)

        Grading31.setCentralWidget(self.centralwidget)

        self.retranslateUi(Grading31)

        QMetaObject.connectSlotsByName(Grading31)
    # setupUi

    def retranslateUi(self, Grading31):
        Grading31.setWindowTitle(QCoreApplication.translate("Grading31", u"\\uc120\\ud0dd\\ud615 \\ubc30\\uc810", None))
        self.lbNum.setText(QCoreApplication.translate("Grading31", u"\\ubc88\\ud638", None))
        self.lbPoint.setText(QCoreApplication.translate("Grading31", u"\\ubc30\\uc810", None))
        self.lbNo.setText(QCoreApplication.translate("Grading31", u"111", None))
        self.lineEdit.setInputMask(QCoreApplication.translate("Grading31", u"D.d", None))
        self.btnBack.setText(QCoreApplication.translate("Grading31", u"\\uc774\\uc804", None))
        self.btnNext.setText(QCoreApplication.translate("Grading31", u"\\ub2e4\\uc74c", None))
    # retranslateUi


class Ui_Grading32(object):
    def setupUi(self, Grading32):
        if not Grading32.objectName():
            Grading32.setObjectName(u"Grading32")
        Grading32.resize(260, 104)
        self.centralwidget = QWidget(Grading32)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbNum = QLabel(self.centralwidget)
        self.lbNum.setObjectName(u"lbNum")
        self.lbNum.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbNum, 0, 0, 1, 1)

        self.lbPoint = QLabel(self.centralwidget)
        self.lbPoint.setObjectName(u"lbPoint")
        self.lbPoint.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbPoint, 0, 1, 1, 1)

        self.lbGet = QLabel(self.centralwidget)
        self.lbGet.setObjectName(u"lbGet")
        self.lbGet.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbGet, 0, 2, 1, 1)

        self.lbNo = QLabel(self.centralwidget)
        self.lbNo.setObjectName(u"lbNo")
        self.lbNo.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbNo, 1, 0, 1, 1)

        self.lnPoint = QLineEdit(self.centralwidget)
        self.lnPoint.setObjectName(u"lnPoint")
        self.lnPoint.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lnPoint, 1, 1, 1, 1)

        self.lnGet = QLineEdit(self.centralwidget)
        self.lnGet.setObjectName(u"lnGet")
        self.lnGet.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lnGet, 1, 2, 1, 1)

        self.widBot = QWidget(self.centralwidget)
        self.widBot.setObjectName(u"widBot")
        self.horizontalLayout = QHBoxLayout(self.widBot)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnBack = QPushButton(self.widBot)
        self.btnBack.setObjectName(u"btnBack")

        self.horizontalLayout.addWidget(self.btnBack)

        self.spH = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.spH)

        self.btnNext = QPushButton(self.widBot)
        self.btnNext.setObjectName(u"btnNext")

        self.horizontalLayout.addWidget(self.btnNext)


        self.gridLayout.addWidget(self.widBot, 2, 0, 1, 3)

        Grading32.setCentralWidget(self.centralwidget)

        self.retranslateUi(Grading32)

        QMetaObject.connectSlotsByName(Grading32)
    # setupUi

    def retranslateUi(self, Grading32):
        Grading32.setWindowTitle(QCoreApplication.translate("Grading32", u"\\uc11c\\ub2f5\\ud615 \\ubc30\\uc810", None))
        self.lbNum.setText(QCoreApplication.translate("Grading32", u"\\ubc88\\ud638", None))
        self.lbPoint.setText(QCoreApplication.translate("Grading32", u"\\ubc30\\uc810", None))
        self.lbGet.setText(QCoreApplication.translate("Grading32", u"\\ubc30\\uc810", None))
        self.lbNo.setText(QCoreApplication.translate("Grading32", u"99", None))
        self.lnPoint.setInputMask(QCoreApplication.translate("Grading32", u"D.d", None))
        self.lnGet.setInputMask(QCoreApplication.translate("Grading32", u"D.d", None))
        self.btnBack.setText(QCoreApplication.translate("Grading32", u"\\uc774\\uc804", None))
        self.btnNext.setText(QCoreApplication.translate("Grading32", u"\\ub2e4\\uc74c", None))
    # retranslateUi


class Ui_GradRes(object):
    def setupUi(self, GradRes):
        if not GradRes.objectName():
            GradRes.setObjectName(u"GradRes")
        GradRes.resize(261, 107)
        self.centralwidget = QWidget(GradRes)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy_PF.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy_PF)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy_PF.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy_PF)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy_PF.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy_PF)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 3, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy_PF.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy_PF)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy_PF.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy_PF)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy_PF.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy_PF)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy_PF.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy_PF)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 2, 3, 1, 1)

        GradRes.setCentralWidget(self.centralwidget)

        self.retranslateUi(GradRes)

        QMetaObject.connectSlotsByName(GradRes)
    # setupUi

    def retranslateUi(self, GradRes):
        GradRes.setWindowTitle(QCoreApplication.translate("GradRes", u"\\uac00\\ucc44\\uc810\\uacb0\\uacfc", None))
        self.label_3.setText(QCoreApplication.translate("GradRes", u"\\uc810\\uc218", None))
        self.label_5.setText(QCoreApplication.translate("GradRes", u"\\uacfc\\ubaa9\\uba85", None))
        self.label_2.setText(QCoreApplication.translate("GradRes", u"\\uc624\\ub2f5 \\uc218", None))
        self.pushButton.setText(QCoreApplication.translate("GradRes", u"\\ubcf4\\uae30", None))
        self.label_7.setText(QCoreApplication.translate("GradRes", u"35", None))
        self.label_4.setText(QCoreApplication.translate("GradRes", u"\\uc0c1\\uc138", None))
        self.label.setText(QCoreApplication.translate("GradRes", u"\\uacfc\\ubaa9\\uba85", None))
        self.label_6.setText(QCoreApplication.translate("GradRes", u"\\uc624\\ub2f5 \\uc218", None))
        self.pushButton_2.setText(QCoreApplication.translate("GradRes", u"\\ub2eb\\uae30", None))
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
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy_FF.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy_FF)

        self.gridLayout_3.addWidget(self.pushButton, 2, 2, 1, 1)

        self.wid2 = QWidget(self.centralwidget)
        self.wid2.setObjectName(u"wid2")
        self.gridLayout = QGridLayout(self.wid2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_7 = QLabel(self.wid2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)

        self.label_8 = QLabel(self.wid2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 0, 1, 1, 1)

        self.label_9 = QLabel(self.wid2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 0, 3, 1, 1)

        self.label_2 = QLabel(self.wid2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy_FF.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy_FF)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.wid2, 1, 1, 1, 2)

        self.wid1 = QWidget(self.centralwidget)
        self.wid1.setObjectName(u"wid1")
        self.gridLayout_2 = QGridLayout(self.wid1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.wid1)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)

        self.label_4 = QLabel(self.wid1)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)

        self.label_5 = QLabel(self.wid1)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 3, 1, 1)

        self.label_6 = QLabel(self.wid1)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 4, 1, 1)

        self.label = QLabel(self.wid1)
        self.label.setObjectName(u"label")
        sizePolicy_FF.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy_FF)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.wid1, 0, 1, 1, 2)

        GradDetail.setCentralWidget(self.centralwidget)

        self.retranslateUi(GradDetail)

        QMetaObject.connectSlotsByName(GradDetail)
    # setupUi

    def retranslateUi(self, GradDetail):
        GradDetail.setWindowTitle(QCoreApplication.translate("GradDetail", u"\\uc0c1\\uc138", None))
        self.pushButton.setText(QCoreApplication.translate("GradDetail", u"\\ub2eb\\uae30", None))
        self.label_7.setText(QCoreApplication.translate("GradDetail", u"\\ub4dd\\uc810", None))
        self.label_8.setText(QCoreApplication.translate("GradDetail", u"\\ubc88\\ud638", None))
        self.label_9.setText(QCoreApplication.translate("GradDetail", u"\\uc815\\ub2f5", None))
        self.label_2.setText(QCoreApplication.translate("GradDetail", u"\\uc11c\\n"
"\\ub2f5\\n"
"\\ud615\\n"
"\\uc624\\n"
"\\ub2f5", None))
        self.label_3.setText(QCoreApplication.translate("GradDetail", u"\\ubc88\\ud638", None))
        self.label_4.setText(QCoreApplication.translate("GradDetail", u"\\uc751\\ub2f5", None))
        self.label_5.setText(QCoreApplication.translate("GradDetail", u"\\uc815\\ub2f5", None))
        self.label_6.setText(QCoreApplication.translate("GradDetail", u"\\ubc30\\uc810", None))
        self.label.setText(QCoreApplication.translate("GradDetail", u"\\uc120\\n"
"\\ud0dd\\n"
"\\ud615\\n"
"\\uc624\\n"
"\\ub2f5", None))
    # retranslateUi


class Ui_ExamInput(object):
    def setupUi(self, ExamInput):
        if not ExamInput.objectName():
            ExamInput.setObjectName(u"ExamInput")
        ExamInput.resize(341, 107)
        self.centralwidget = QWidget(ExamInput)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbTitleSubject = QLabel(self.centralwidget)
        self.lbTitleSubject.setObjectName(u"lbTitleSubject")
        sizePolicy_IP.setHeightForWidth(self.lbTitleSubject.sizePolicy().hasHeightForWidth())
        self.lbTitleSubject.setSizePolicy(sizePolicy_IP)
        self.lbTitleSubject.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbTitleSubject, 0, 0, 1, 1)

        self.lnGrd1 = QLineEdit(self.centralwidget)
        self.lnGrd1.setObjectName(u"lnGrd1")\
        sizePolicy_FF.setHeightForWidth(self.lnGrd1.sizePolicy().hasHeightForWidth())
        self.lnGrd1.setSizePolicy(sizePolicy_FF)
        self.lnGrd1.setMaximumSize(QSize(60, 16777215))
        self.lnGrd1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lnGrd1, 1, 2, 1, 1)

        self.lbNum = QLabel(self.centralwidget)
        self.lbNum.setObjectName(u"lbNum")
        sizePolicy_IP.setHeightForWidth(self.lbNum.sizePolicy().hasHeightForWidth())
        self.lbNum.setSizePolicy(sizePolicy_IP)
        self.lbNum.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbNum, 1, 1, 1, 1)

        self.lbScore = QLabel(self.centralwidget)
        self.lbScore.setObjectName(u"lbScore")
        sizePolicy_FP.setHeightForWidth(self.lbScore.sizePolicy().hasHeightForWidth())
        self.lbScore.setSizePolicy(sizePolicy_FP)
        self.lbScore.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbScore, 0, 2, 1, 1, Qt.AlignHCenter)

        self.lbSubject = QLabel(self.centralwidget)
        self.lbSubject.setObjectName(u"lbSubject")
        sizePolicy_IP.setHeightForWidth(self.lbSubject.sizePolicy().hasHeightForWidth())
        self.lbSubject.setSizePolicy(sizePolicy_IP)
        self.lbSubject.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbSubject, 1, 0, 1, 1)

        self.lnGrd2 = QLineEdit(self.centralwidget)
        self.lnGrd2.setObjectName(u"lnGrd2")
        sizePolicy_FF.setHeightForWidth(self.lnGrd2.sizePolicy().hasHeightForWidth())
        self.lnGrd2.setSizePolicy(sizePolicy_FF)
        self.lnGrd2.setMaximumSize(QSize(60, 16777215))
        self.lnGrd2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lnGrd2, 1, 3, 1, 1)

        self.lnGrd2_2 = QLineEdit(self.centralwidget)
        self.lnGrd2_2.setObjectName(u"lnGrd2_2")
        sizePolicy_FF.setHeightForWidth(self.lnGrd2_2.sizePolicy().hasHeightForWidth())
        self.lnGrd2_2.setSizePolicy(sizePolicy_FF)
        self.lnGrd2_2.setMaximumSize(QSize(60, 16777215))
        self.lnGrd2_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lnGrd2_2, 1, 4, 1, 1)

        self.lbTitleNum = QLabel(self.centralwidget)
        self.lbTitleNum.setObjectName(u"lbTitleNum")
        sizePolicy_IP.setHeightForWidth(self.lbTitleNum.sizePolicy().hasHeightForWidth())
        self.lbTitleNum.setSizePolicy(sizePolicy_IP)
        self.lbTitleNum.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbTitleNum, 0, 1, 1, 1)

        self.lbPerson = QLabel(self.centralwidget)
        self.lbPerson.setObjectName(u"lbPerson")
        sizePolicy_FP.setHeightForWidth(self.lbPerson.sizePolicy().hasHeightForWidth())
        self.lbPerson.setSizePolicy(sizePolicy_FP)
        self.lbPerson.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbPerson, 0, 4, 1, 1, Qt.AlignHCenter)

        self.lbRank = QLabel(self.centralwidget)
        self.lbRank.setObjectName(u"lbRank")
        sizePolicy_FP.setHeightForWidth(self.lbRank.sizePolicy().hasHeightForWidth())
        self.lbRank.setSizePolicy(sizePolicy_FP)
        self.lbRank.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbRank, 0, 3, 1, 1, Qt.AlignHCenter)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy_IF.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy_IF)

        self.gridLayout.addWidget(self.pushButton, 1, 5, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 5, 1, 1)

        self.widBot = QWidget(self.centralwidget)
        self.widBot.setObjectName(u"widBot")
        self.horizontalLayout = QHBoxLayout(self.widBot)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnAdd = QPushButton(self.widBot)
        self.btnAdd.setObjectName(u"btnAdd")
        sizePolicy_FF.setHeightForWidth(self.btnAdd.sizePolicy().hasHeightForWidth())
        self.btnAdd.setSizePolicy(sizePolicy_FF)

        self.horizontalLayout.addWidget(self.btnAdd)

        self.spH = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.spH)

        self.btnCancel = QPushButton(self.widBot)
        self.btnCancel.setObjectName(u"btnCancel")
        sizePolicy_FF.setHeightForWidth(self.btnCancel.sizePolicy().hasHeightForWidth())
        self.btnCancel.setSizePolicy(sizePolicy_FF)

        self.horizontalLayout.addWidget(self.btnCancel)

        self.btnSet = QPushButton(self.widBot)
        self.btnSet.setObjectName(u"btnSet")
        sizePolicy_FF.setHeightForWidth(self.btnSet.sizePolicy().hasHeightForWidth())
        self.btnSet.setSizePolicy(sizePolicy_FF)

        self.horizontalLayout.addWidget(self.btnSet)


        self.gridLayout.addWidget(self.widBot, 2, 0, 1, 6)

        ExamInput.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btnAdd, self.btnSet)
        QWidget.setTabOrder(self.btnSet, self.btnCancel)

        self.retranslateUi(ExamInput)

        QMetaObject.connectSlotsByName(ExamInput)
    # setupUi

    def retranslateUi(self, GradeInput):
        GradeInput.setWindowTitle(QCoreApplication.translate("GradeInput", u"(\\ucd5c\\uc885)\\uc131\\uc801\\uc785\\ub825", None))
        self.lbTitleSubject.setText(QCoreApplication.translate("GradeInput", u"\\uacfc\\ubaa9\\uba85", None))
        self.lnGrd1.setInputMask(QCoreApplication.translate("GradeInput", u"Ddd", None))
        self.lbNum.setText(QCoreApplication.translate("GradeInput", u"1", None))
        self.lbScore.setText(QCoreApplication.translate("GradeInput", u"\\uc6d0\\uc810\\uc218", None))
        self.lbSubject.setText(QCoreApplication.translate("GradeInput", u"\\uac00\\ub098\\ub2e4", None))
        self.lnGrd2.setInputMask(QCoreApplication.translate("GradeInput", u"Ddd", None))
        self.lnGrd2_2.setInputMask(QCoreApplication.translate("GradeInput", u"Ddd", None))
        self.lbTitleNum.setText(QCoreApplication.translate("GradeInput", u"\\ub2e8\\uc704\\uc218", None))
        self.lbPerson.setText(QCoreApplication.translate("GradeInput", u"\\uc218\\uac15\\uc778\\uc6d0", None))
        self.lbRank.setText(QCoreApplication.translate("GradeInput", u"\\uc11d\\ucc28", None))
        self.pushButton.setText(QCoreApplication.translate("GradeInput", u"X", None))
        self.label.setText(QCoreApplication.translate("GradeInput", u" \\uc0ad\\uc81c", None))
        self.btnAdd.setText(QCoreApplication.translate("GradeInput", u"\\ucd08\\uae30\\ud654", None))
        self.btnCancel.setText(QCoreApplication.translate("GradeInput", u"\\ucde8\\uc18c", None))
        self.btnSet.setText(QCoreApplication.translate("GradeInput", u"\\uc785\\ub825", None))
    # retranslateUi


class Ui_CutCalc(object):
    def setupUi(self, CutCalc):
        if not CutCalc.objectName():
            CutCalc.setObjectName(u"CutCalc")
        CutCalc.resize(208, 319)
        
        self.centralwidget = QWidget(CutCalc)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.glCent = QGridLayout(self.centralwidget)
        self.glCent.setObjectName(u"glCent")
        
        #top input widgets
        self.lbCount = QLabel(self.centralwidget)
        self.lbCount.setObjectName(u"lbCount")
        sizePolicy_IP.setHeightForWidth(self.lbCount.sizePolicy().hasHeightForWidth())
        self.lbCount.setSizePolicy(sizePolicy_IP)
        self.lbCount.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbCount, 0, 0, 1, 1)

        self.lnPerson = QLineEdit(self.centralwidget)
        self.lnPerson.setObjectName(u"lnPerson")
        sizePolicy_IF.setHeightForWidth(self.lnPerson.sizePolicy().hasHeightForWidth())
        self.lnPerson.setSizePolicy(sizePolicy_IF)
        self.lnPerson.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lnPerson, 0, 1, 1, 2)

        #top title labels
        self.lbGrade = QLabel(self.centralwidget)
        self.lbGrade.setObjectName(u"lbGrade")
        sizePolicy_IP.setHeightForWidth(self.lbGrade.sizePolicy().hasHeightForWidth())
        self.lbGrade.setSizePolicy(sizePolicy_IP)
        self.lbGrade.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbGrade, 1, 0, 1, 1)

        self.lbRatio = QLabel(self.centralwidget)
        self.lbRatio.setObjectName(u"lbRatio")
        sizePolicy_IP.setHeightForWidth(self.lbRatio.sizePolicy().hasHeightForWidth())
        self.lbRatio.setSizePolicy(sizePolicy_IP)
        self.lbRatio.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbRatio, 1, 1, 1, 1)

        self.lbCut = QLabel(self.centralwidget)
        self.lbCut.setObjectName(u"lbCut_2")
        sizePolicy_IP.setHeightForWidth(self.lbCut_2.sizePolicy().hasHeightForWidth())
        self.lbCut.setSizePolicy(sizePolicy_IP)
        self.lbCut.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbCut_2, 1, 2, 1, 1)

        #btns
        lbGrade=[]
        lbRatio=[]
        lbCut=[]
        for cut in range(9):
            grade = QLabel(centralwidget)
            grade.setObjectName(u"grade")
            grade.setText(str(k))
            sizePolicy_IP.setHeightForWidth(grade.sizePolicy().hasHeightForWidth())
            grade.setSizePolicy(sizePolicy_IP)
            grade.setAlignment(Qt.AlignCenter)
            glCent.addWidget(grade, 2, 0, 1, 1)

            ratio = QLabel(centralwidget)
            ratio.setObjectName(u"ratio")
            ratio.setText(str(CUTS[k]))
            sizePolicy_IP.setHeightForWidth(ratio.sizePolicy().hasHeightForWidth())
            ratio.setSizePolicy(sizePolicy_IP)
            ratio.setAlignment(Qt.AlignCenter)
            glCent.addWidget(ratio, 2, 1, 1, 1)

            cut = QLabel(centralwidget)
            cut.setObjectName(u"cut")
            sizePolicy_IP.setHeightForWidth(cut.sizePolicy().hasHeightForWidth())
            cut.setSizePolicy(sizePolicy_IP)
            cut.setAlignment(Qt.AlignCenter)
            glCent.addWidget(cut, 2, 2, 1, 1)
            
            lbGrade.append(grade)
            lbRatio.append(ratio)
            lbCut.append(cut)

        #bottom widgets
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
        
        
        self.gridLayout.addWidget(self.widBot, 11, 0, 1, 3)

        CutCalc.setCentralWidget(self.centralwidget)
        self.retranslateUi(CutCalc)
        QMetaObject.connectSlotsByName(CutCalc)
    # setupUi

    def retranslateUi(self, CutCalc):
        CutCalc.setWindowTitle(QCoreApplication.translate("CutCalc", u"\\ub4f1\\uae09\\ucef7 \\uacc4\\uc0b0", None))
        self.lbCount.setText(QCoreApplication.translate("CutCalc", u"\\uc778\\uc6d0", None))
        self.lnPerson.setInputMask(QCoreApplication.translate("CutCalc", u"Ddd", None))
        self.lbGrade.setText(QCoreApplication.translate("CutCalc", u"\\ub4f1\\uae09", None))
        self.lbRatio.setText(QCoreApplication.translate("CutCalc", u"\\ube44\\uc728", None))
        self.lbCut.setText(QCoreApplication.translate("CutCalc", u"\\uc778\\uc6d0\\uc218", None))
        self.btnClose.setText(QCoreApplication.translate("CutCalc", u"\\ub2eb\\uae30", None))
        self.btnCalc.setText(QCoreApplication.translate("CutCalc", u"\\uacc4\\uc0b0", None))
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

        self.lbSubject = QLabel(self.centralwidget)
        self.lbSubject.setObjectName(u"lbSubject")
        sizePolicy_FP.setHeightForWidth(self.lbSubject.sizePolicy().hasHeightForWidth())
        self.lbSubject.setSizePolicy(sizePolicy_FP)
        self.lbSubject.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbSubject, 0, 0, 1, 1)

        self.lbNum = QLabel(self.centralwidget)
        self.lbNum.setObjectName(u"lbNum")
        sizePolicy_FP.setHeightForWidth(self.lbNum.sizePolicy().hasHeightForWidth())
        self.lbNum.setSizePolicy(sizePolicy_FP)
        self.lbNum.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbNum, 0, 1, 1, 1)

        self.lbMid = QLabel(self.centralwidget)
        self.lbMid.setObjectName(u"lbMid")
        sizePolicy_FP.setHeightForWidth(self.lbMid.sizePolicy().hasHeightForWidth())
        self.lbMid.setSizePolicy(sizePolicy_FP)
        self.lbMid.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbMid, 0, 2, 1, 1, Qt.AlignHCenter)

        self.lbEnd = QLabel(self.centralwidget)
        self.lbEnd.setObjectName(u"lbEnd")
        sizePolicy_FP.setHeightForWidth(self.lbEnd.sizePolicy().hasHeightForWidth())
        self.lbEnd.setSizePolicy(sizePolicy_FP)
        self.lbEnd.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbEnd, 0, 3, 1, 1, Qt.AlignHCenter)

        self.lbSubject_2 = QLabel(self.centralwidget)
        self.lbSubject_2.setObjectName(u"lbSubject_2")
        sizePolicy_FP.setHeightForWidth(self.lbSubject_2.sizePolicy().hasHeightForWidth())
        self.lbSubject_2.setSizePolicy(sizePolicy_FP)
        self.lbSubject_2.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbSubject_2, 1, 0, 1, 1)

        self.lbNum_2 = QLabel(self.centralwidget)
        self.lbNum_2.setObjectName(u"lbNum_2")
        self.lbNum_2.setSizePolicy(sizePolicy_IP)
        sizePolicy_IP.setHeightForWidth(self.lbNum_2.sizePolicy().hasHeightForWidth())
        self.lbNum_2.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbNum_2, 1, 1, 1, 1)

        self.lnGrd1 = QLineEdit(self.centralwidget)
        self.lnGrd1.setObjectName(u"lnGrd1")
        sizePolicy_MF.setHeightForWidth(self.lnGrd1.sizePolicy().hasHeightForWidth())
        self.lnGrd1.setSizePolicy(sizePolicy_MF)
        self.lnGrd1.setMaximumSize(QSize(100, 16777215))
        self.lnGrd1.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lnGrd1, 1, 2, 1, 1)
        
        self.lnGrd2 = QLineEdit(self.centralwidget)
        self.lnGrd2.setObjectName(u"lnGrd2")
        sizePolicy_MF.setHeightForWidth(self.lnGrd2.sizePolicy().hasHeightForWidth())
        self.lnGrd2.setSizePolicy(sizePolicy_MF)
        self.lnGrd2.setMaximumSize(QSize(100, 16777215))
        self.lnGrd2.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lnGrd2, 1, 3, 1, 1)

        #bottom widgets
        self.widBot = QWidget(self.centralwidget)
        self.widBot.setObjectName(u"widBot")
        
        self.horizontalLayout = QHBoxLayout(self.widBot)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        
        self.btnAdd = QPushButton(self.widBot)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setSizePolicy(sizePolicy_FF)
        sizePolicy_FF.setHeightForWidth(self.btnAdd.sizePolicy().hasHeightForWidth())
        self.horizontalLayout.addWidget(self.btnAdd)

        self.spH = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.spH)

        self.btnCancel = QPushButton(self.widBot)
        self.btnCancel.setObjectName(u"btnCancel")
        sizePolicy_FF.setHeightForWidth(self.btnCancel.sizePolicy().hasHeightForWidth())
        self.btnCancel.setSizePolicy(sizePolicy_FF)
        self.horizontalLayout.addWidget(self.btnCancel)

        self.btnSet = QPushButton(self.widBot)
        self.btnSet.setObjectName(u"btnSet")
        sizePolicy_FF.setHeightForWidth(self.btnSet.sizePolicy().hasHeightForWidth())
        self.btnSet.setSizePolicy(sizePolicy_FF)
        self.horizontalLayout.addWidget(self.btnSet)


        self.glMain.addWidget(self.widBot, 2, 0, 1, 4)

        GradeCalc.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btnAdd, self.btnSet)
        QWidget.setTabOrder(self.btnSet, self.btnCancel)

        self.retranslateUi(GradeCalc)

        QMetaObject.connectSlotsByName(GradeCalc)
    # setupUi

    def retranslateUi(self, GradeCalc):
        GradeCalc.setWindowTitle(QCoreApplication.translate("GradeCalc", u"\\uc608\\uc0c1\\ub4f1\\uae09\\uacc4\\uc0b0", None))
        self.lnGrd2.setInputMask(QCoreApplication.translate("GradeCalc", u"d", None))
        self.lbMid.setText(QCoreApplication.translate("GradeCalc", u"\\ub4f1\\uae091", None))
        self.lnGrd1.setInputMask(QCoreApplication.translate("GradeCalc", u"D", None))
        self.lbSubject_2.setText(QCoreApplication.translate("GradeCalc", u"\\uac00\\ub098\\ub2e4", None))
        self.lbSubject.setText(QCoreApplication.translate("GradeCalc", u"\\uacfc\\ubaa9\\uba85", None))
        self.lbEnd.setText(QCoreApplication.translate("GradeCalc", u"\\ub4f1\\uae092", None))
        self.btnAdd.setText(QCoreApplication.translate("GradeCalc", u"\\uc778\\uc6d0\\uacc4\\uc0b0", None))
        self.btnCancel.setText(QCoreApplication.translate("GradeCalc", u"\\ucd08\\uae30\\ud654", None))
        self.btnSet.setText(QCoreApplication.translate("GradeCalc", u"\\ub2eb\\uae30", None))
        self.lbNum_2.setText(QCoreApplication.translate("GradeCalc", u"1", None))
        self.lbNum.setText(QCoreApplication.translate("GradeCalc", u"\\ub2e8\\uc704\\uc218", None))
    # retranslateUi
