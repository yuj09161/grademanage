# -*- coding: utf-8 -*-
from PySide2.QtCore import Qt, QRect, QTimer, QCoreApplication, QMetaObject, Signal
from PySide2.QtGui import QFont, QIcon, QCloseEvent, QKeySequence
from PySide2.QtWidgets import *
import UI

import os,sys,json,traceback,re
from decimal import Decimal as dec
import numpy as np

#settings
ASK_ON_CLOSE     = True
COMBO_INIT_ORDER = (1,0,0)


#전역 불변 변수 정의
CURRENT_PATH = os.path.dirname(os.path.abspath('__file__'))+'\\'
PROGRAM_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))+'\\'
ESCAPE_SEQ   = QKeySequence.fromString('Escape')
CUT_RATIO    = (4,11,23,40,60,77,89,96,100)

#전역 변수 정의
current_exam    = '111'
last_file       = ''
saved           = True
current_num     = {}
result_semester = {}
current_wrong   = {}
current_result  = {}
result_exam     = {}

for a in range(1,4):
    for b in range(1,3):
        result_semester[str(10*a+b)]=[{},{}]
        for c in range(1,3):
            result_exam[str(100*a+10*b+c)]=[{},{}]

'''전역함수'''
#점수 계산
def get_score(subject=None):
    def calc(subject):
        if subject in current_wrong.keys(): #과목 존재?
            wrong=current_wrong[subject]
            score,err_cnt=dec(100),0
            #객관식 오답 계산
            wrong_sel=tuple(wrong[0].values())
            if wrong_sel:
                err_cnt+=len(wrong_sel)
                for j in range(len(wrong_sel)):
                    score-=dec(wrong_sel[j][2])
            #서술형 오답 계산
            wrong_exp=tuple(wrong[1].values())
            if wrong_exp:
                err_cnt+=len(wrong_exp)
                for j in range(len(wrong_exp)):
                    score-=dec(wrong_exp[j][1])-dec(wrong_exp[j][0])
            return score,err_cnt
        else:
            return None
    if subject:
        return calc(subject)
    else:
        result=[]
        for subject in current_subjects:
            result.append(calc(subject))
        return result


def get_current_num(*,name=False,dictionary=False):
    exam=int(current_exam[2])
    var=name*4+dictionary*2+(exam==3)#*1
    if var==5: #true: name, exam==3
        return tuple(current_num.keys())
    elif var==4: #true: name
        name=[]
        for subject in current_num:
            if current_num[subject][exam]:
                name.append(subject)
        return name
    elif var==3: #true: dictionary, exam==3
        tmp={}
        for subject in current_num:
            tmp[subject]=current_num[subject][0]
        return tmp
    elif var==2: #true: dictonary
        tmp={}
        for subject in current_num:
            if current_num[subject][exam]:
                tmp[subject]=current_num[subject][0]
        return tmp
    elif var==1: #true: exam==3
        return tuple(value[0] for value in current_num.values())
    elif var==0: #true: - (default)
        tmp=[]
        for value in current_num.values():
            if value[exam]:
                tmp.append(value[0])
        return tmp
    else:
        base_err=f'\nArguments:\nname:{name}\ndictionary:{dictionary}\nexam:{exam}'
        if var==6 or var==7:
            QMessageBox.warning(None,'Error','Error:\nname & dictonary == true')
        elif var<0:
            QMessageBox.critical(None,'Error',f'Unknown Error: var({var})<0'+base_err)
        elif var>5:
            QMessageBox.critical(None,'Error',f'Unknown Error: var({var})>5'+base_err)
        else:
            QMessageBox.critical(None,'Error',f'Unknown Error: var type: {type(var)}\nvalue: {var}'+base_err)


def resize_all(window,*wid):
    app.processEvents()
    for wid in reversed(wid):
        wid.resize(wid.sizeHint().width(),wid.sizeHint().height())
    window.resize(window.sizeHint().width(),window.sizeHint().height())
    app.processEvents()


def resize_height(window,*wid):
    app.processEvents()
    for wid in reversed(wid):
        wid.resize(wid.width(),wid.sizeHint().height())
    window.resize(window.width(),window.sizeHint().height())
    app.processEvents()


def center_geometry(win_size):
    x,y=screen_size
    w=win_size.width()
    h=win_size.height()
    return QRect((x-w)//2,(y-h)//2,w,h)


#읽기
def load(name=None,*,parent=None):
    def loader():
        global result_semester,result_exam,saved,last_file
        if name:
            try:
                global current_num,current_wrong,current_result
                with open(name,'r',encoding='utf-8') as file:
                    result_semester,result_exam=json.load(file)
                if current_exam[2]=='3': #학기말
                    current_num,current_result=result_semester[current_exam[:2]]
                else: #중간고사or기말고사
                    current_num=result_semester[current_exam[:2]][0]
                    current_wrong,current_result=result_exam[current_exam]
            except IOError as e:
                tmp=QMessageBox.critical(
                    parent,
                    'Load Error',
                    f'파일 읽기 오류 발생\nTraceBack:\n{e}\n재시도?',
                    QMessageBox.Retry|QMessageBox.Cancel
                )
                if tmp==QMessageBox.Retry:
                    load(name)
            except json.JSONDecodeError as e:
                QMessageBox.critical(parent,'Error','파일 형식 오류')
            except ValueError as e:
                QMessageBox.critical(parent,'Error','파일 내용 오류')
            else:
                saved=True
                last_file=name
            finally:
                pass
    if not name:
        name,_=QFileDialog.getOpenFileName(parent,'저장',CURRENT_PATH)
    if saved:
        loader()
    else:
        response=QMessageBox.question(
            parent,
            'Info',
            '저장 안됨\n저장?',
            QMessageBox.Save|QMessageBox.Discard|QMessageBox.Cancel
        )
        if response==QMessageBox.Save:
            save()
            loader()
        elif response==QMessageBox.Discard:
            loader()


#쓰기
def save(last=False,*,name=None,parent=None):
    global result_semester,result_exam,last_file,saved
    if last:
        name=last_file
    if not name:
        name,_=QFileDialog.getSaveFileName(parent,'저장',CURRENT_PATH)
    if name:
        if current_exam[2]=='3': #학기말
            result_semester[current_exam[:2]]=[current_num,current_result]
        else: #중간고사or기말고사
            result_semester[current_exam[:2]][0]=current_num
            result_exam[current_exam]=[current_wrong,current_result]
        try:
            with open(name,'w',encoding='utf-8') as file:
                json.dump((result_semester,result_exam),file,indent=4,ensure_ascii=False)
        except IOError as e:
                response=QMessageBox.warning(
                    self,
                    'Save Error',
                    f'데이터 저장 중 오류 발생\nTraceBack:\n{e}\n재시도?',
                    QMessageBox.Retry|QMessageBox.Cancel
                )
                if response==QMessageBox.Retry: 
                    save(name=name)
        else:
            last_file=name
            saved=True


'''창 클래스들'''

class DetailErr(QMessageBox):
    def __init__(self,parent,title,text,detail_text,icon=QMessageBox.Warning):
        super().__init__(parent)
        
        self.setWindowTitle(title)
        self.setText(text)
        self.setIcon(icon)
        
        if type(detail_text) is str:
            self.setDetailedText(detail_text)
        elif type(detail_text) is tuple:
            try:
                self.setDetailedText(''.join(traceback.format_exception(*detail_text)))
            except:
                err_win=DetailErr(
                    self,
                    'Error',
                    '타입 오류',
                    f'detail_text 타입 오류: {type(detail_text)}'
                )
        else:
            err_win=DetailErr(
                self,
                'Error',
                '타입 오류',
                f'detail_text 타입 오류: {type(detail_text)}'
            )

class Info(QMainWindow):
    def __init__(self,parent,title,info_text,display_qtinfo=False):
        self.__display_qtinfo=display_qtinfo
        
        super().__init__(parent)
        self.setupUI()
        
        self.retranslateUi(title,info_text)
        self.btnExit.clicked.connect(self.hide)
        
        if self.__display_qtinfo:
            self.btnQt.clicked.connect(lambda: QMessageBox.aboutQt(self))
    
    def setupUI(self):
        if not self.objectName():
            self.setObjectName(u"info")
        self.setFixedSize(400, 300)
        self.setWindowFlags(self.windowFlags()^Qt.WindowMinMaxButtonsHint)
        
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.glCentral = QGridLayout(self.centralwidget)
        self.glCentral.setObjectName(u"glCentral")
        
        self.pteInfo = QPlainTextEdit(self.centralwidget)
        self.pteInfo.setObjectName(u"pteInfo")
        self.pteInfo.setReadOnly(True)
        self.glCentral.addWidget(self.pteInfo, 0, 0, 1, 2)

        if self.__display_qtinfo:
            self.btnQt = QPushButton(self.centralwidget)
            self.btnQt.setObjectName(u"btnQt")
            self.glCentral.addWidget(self.btnQt, 1, 0, 1, 1, Qt.AlignLeft)

        self.btnExit = QPushButton(self.centralwidget)
        self.btnExit.setObjectName(u"btnExit")
        self.glCentral.addWidget(self.btnExit, 1, 1, 1, 1, Qt.AlignRight)

        self.setCentralWidget(self.centralwidget)
    
    def retranslateUi(self,title,info_text):
        self.setWindowTitle(QCoreApplication.translate("info", title, None))
        self.pteInfo.setPlainText(re.sub('\n +','\n',re.sub('\n{2,} *','\n\n',info_text)))
        self.btnExit.setText(QCoreApplication.translate("info", u"\ub2eb\uae30", None))
        if self.__display_qtinfo:
            self.btnQt.setText(QCoreApplication.translate("info", u"About Qt", None))

#Main Window class
class Main(QMainWindow,UI.Ui_Main):
    def __init__(self):
        def load_and_setexam(name=None):
            load(name)
            self.__set_exam(save=True)
        
        super().__init__()
        
        self.setupUI(self,COMBO_INIT_ORDER)
        load_and_setexam('save.json')
        
        #Define Variables
        self.__win=[]
        self.__opensource_notice_win = None
        self.__license_win           = None
        
        #Connect Slots (QComboBox)
        self.comboYear.currentIndexChanged.connect(self.__set_exam)
        self.comboSemester.currentIndexChanged.connect(self.__set_exam)
        self.comboExam.currentIndexChanged.connect(self.__set_exam)
        
        #Connect Slots (QButtons)
        self.btnSubject.clicked.connect(lambda: self.__show_window(Subject_In))
        self.btnGrading.clicked.connect(lambda: self.__win.append(Grading_Controller()))
        self.btnGradingRes.clicked.connect(lambda: self.__show_window(Grad_result))
        self.btnCalc.clicked.connect(lambda: self.__show_window(Grade_calc))
        self.btnInput.clicked.connect(lambda: self.__show_window(Exam_input))
        self.btnRes.clicked.connect(lambda: self.__show_window(Exam_result))
        #self.btnManage.clicked.connect()
        self.btnManage.setEnabled(False)
        
        #Connect Slots (QAction)
        self.save.triggered.connect(lambda: save(True))
        self.saveAs.triggered.connect(save)
        self.load.triggered.connect(load_and_setexam)
        self.exit.triggered.connect(self.close)
        self.cut_calc.triggered.connect(lambda: self.__show_window(Cut_calc))
        self.license.triggered.connect(self.__opensource_notice)
        self.about.triggered.connect(self.__license)

    def closeEvent(self,event):
        if ASK_ON_CLOSE and not saved:
            response=QMessageBox.question(
                self,
                'Info',
                '저장 안됨\n저장?',
                QMessageBox.Save|QMessageBox.Discard|QMessageBox.Cancel
            )
            if response==QMessageBox.Save:
                save(True)
                event.accept()
                sys.exit(0)
            elif response==QMessageBox.Discard:
                event.accept()
                sys.exit(0)
            elif response==QMessageBox.Cancel:
                event.ignore()
        else:
            event.accept()
            sys.exit(0)
    
    #시험 설정
    def __set_exam(self,*,save=False):
        global current_num,current_wrong,current_result,\
               current_exam,current_subjects,current_subject_cnt
        
        def save_old(): #시험 결과 저장
            global result_semester,result_exam
            if current_exam[2]=='3':
                result_semester[current_exam[:2]]=[current_num,current_result]
            else:
                result_semester[current_exam[:2]][0]=current_num
                result_exam[current_exam]=[current_wrong,current_result]
        
        semester=''
        for wid in (self.comboYear,self.comboSemester,self.comboExam): #과목 불러오기
            semester+=str(wid.currentIndex()+1)
        
        #시험 결과 저장/불러오기
        if save:
            save_old()
        if semester[2]=='3': #학기말
            current_exam=semester
            current_num,current_result=result_semester[current_exam[:2]]
        else: #중간고사or기말고사
            current_exam=semester
            current_num=result_semester[current_exam[:2]][0]
            current_wrong,current_result=result_exam[current_exam]
        
        #버튼 상태 설정
        self.update_btn()
        #get current subject
        current_subjects=get_current_num(name=True)
        current_subject_cnt=len(current_subjects)
    
    #버튼 상태 업데이트
    def update_btn(self):
        if current_num:
            if current_exam[2]=='3':
                self.btnGrading.setEnabled(False)
                self.btnGradingRes.setEnabled(False)
            else:
                self.btnGrading.setEnabled(True)
                if current_wrong:
                    self.btnGradingRes.setEnabled(True)
                else:
                    self.btnGradingRes.setEnabled(False)
            self.btnCalc.setEnabled(True)
            self.btnInput.setEnabled(True)
            if current_result:
                self.btnRes.setEnabled(True)
            else:
                self.btnRes.setEnabled(False)
        else:
            self.btnGrading.setEnabled(False)
            self.btnGradingRes.setEnabled(False)
            self.btnCalc.setEnabled(False)
            self.btnInput.setEnabled(False)
            self.btnRes.setEnabled(False)
    
    def __show_window(self,window):
        self.__win.append(window(None))
        self.__win[-1].show()
        self.__win[-1].setGeometry(center_geometry(self.__win[-1].geometry()))
    
    def __opensource_notice(self):
        if not self.__opensource_notice_win:
            if os.path.isfile(PROGRAM_PATH+'NOTICE'):
                with open(PROGRAM_PATH+'NOTICE','r',encoding='utf-8') as file:
                    self.__opensource_notice_win=Info(None,'오픈 소스 라이선스',file.read(),True)
            else:
                self.__opensource_notice_win=Info(None,'오픈 소스 라이선스','Notice File is Missed',True)
        self.__opensource_notice_win.show()
    
    def __license(self):
        if not self.__license_win:
            if os.path.isfile(PROGRAM_PATH+'LICENSE'):
                with open(PROGRAM_PATH+'LICENSE','r',encoding='utf-8') as file:
                    self.__license_win=Info(None,'정보',file.read())
            else:
                self.__license_win=Info(None,'정보','License File is Missed')
        self.__license_win.show()

#과목 입력
class Subject_In(QMainWindow,UI.Ui_SubjectIn):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUI(self)
        
        self.__inbox=[]
        
        #기존 값 불러오기
        if current_num:
            for subject in current_num:
                self.__add_subject(subject,current_num[subject])
        
        self.btnAdd.clicked.connect(lambda: self.__add_subject())
        self.btnCancel.clicked.connect(self.deleteLater)
        self.btnSet.clicked.connect(self.__set_subject)

    def __add_subject(self,subject='',value=(0,True,True)):
        n=len(self.__inbox)
        wids=self.addWidgets(n,subject,value)
        wids[4].clicked.connect(lambda: self.__del_subject(n))
        self.__inbox.append(wids)
        QTimer.singleShot(100,lambda: resize_height(self,self.centralwidget,self.widCent))

    def __del_subject(self,n):
        for a in range(5):
            self.glMain.removeWidget(self.__inbox[n][a])
            self.__inbox[n][a].setParent(None)
        self.__inbox[n]=None

    def __set_subject(self):
        global current_num,saved,current_subjects,current_subject_cnt
        current_num={}; current_subjects=[]
        try:
            for k in range(len(self.__inbox)):
                if self.__inbox[k]:
                    current_num[self.__inbox[k][0].text()]=(
                        int(self.__inbox[k][1].text()),
                        self.__inbox[k][2].isChecked(),
                        self.__inbox[k][3].isChecked()
                    )
                    saved=False
        except ValueError:
            QMessageBox.critical(self,'ERROR','잘못된 값 입력')
        else:
            current_subjects=get_current_num(name=True)
            current_subject_cnt=len(current_subjects)
            self.deleteLater()
            main.update_btn()

#가채점 입력
class Grading_Controller:
    def __init__(self,parent=None):
        self.__parent=parent
        
        self.__grd1=Grading1(parent,current_subjects)
        self.__grd2=Grading2(parent)
        self.__grd31=Grading31(parent)
        self.__grd32=Grading32(parent)
        
        self.__grd1.stat_sig.connect(self.__sig_1)
        self.__grd2.stat_sig.connect(self.__sig_2)
        self.__grd31.stat_sig.connect(self.__sig_31)
        self.__grd32.stat_sig.connect(self.__sig_32)
        
        self.__grd1.show()
    
    def __sig_1(self,response):
        if response[0]==-1:
            self.__grd1.deleteLater()
            self.__grd2.deleteLater()
            self.__grd31.deleteLater()
            self.__grd32.deleteLater()
        elif response[0]==0:
            self.__subject=response[1]
            self.__grd2.show(response[1:])
        else:
            raise ValueError
    
    def __sig_2(self,response):
        if response[0]==-1:
            self.__grd1.show(response[1:])
        elif response[0]==0:
            self.__grd31.show(response[1:])
        elif response[0]==1:
            self.__grd32.show(response[1:])
        elif response[0]==2:
            self.__write_result(response[1:])
        else:
            raise ValueError
    
    def __sig_31(self,response):
        if response[0]==-1:
            self.__grd2.show(response[1:])
        elif response[0]==0:
            self.__grd32.show(response[1:])
        elif response[0]==1:
            self.__write_result(response[1:])
        else:
            raise ValueError
    
    def __sig_32(self,response):
        if response[0]==-2:
            self.__grd2.show(response[1:])
        elif response[0]==-1:
            self.__grd31.show(response[1:])
        elif response[0]==0:
            self.__write_result(response[1:])
        else:
            raise ValueError
    
    def __write_result(self,data):
        global current_wrong,saved
        def callback(btn):
            btnRole=msgbox.buttonRole(btn)
            if btnRole==QMessageBox.YesRole:
                detail_win=Grad_detail(None,data[0])
                detail_win.show()
        
        msgbox=QMessageBox(self.__parent)
        msgbox.setWindowTitle('Result')
        msgbox.addButton('닫기',QMessageBox.NoRole)
        msgbox.buttonClicked.connect(callback)
        
        if data[1] or data[2]:
            msgbox.addButton('상세보기',QMessageBox.YesRole)
            score=100
            for err1 in data[1].values():
                score=score-dec(err1[2])
            for err2 in data[2].values():
                score=score-dec(err2[1])+dec(err2[0])
            msgbox.setText(f'오답 수: {len(data[1])+len(data[2])}\n점수: {score}' )
        else:
            msgbox.setText('만점!\n점수: 100')
        
        current_wrong[self.__subject]=(data[1],data[2])
        saved=False
        
        msgbox.exec_()


class Grading1(QMainWindow,UI.Ui_Grading1):
    stat_sig=Signal(tuple)
    def __init__(self,parent=None,subjects=None):
        super().__init__(parent)
        self.setupUI(self)
        
        self.comboSubject.addItems(subjects)
        try:
            self.comboSubject.setCurrentIndex(0)
        except IndexError:
            QMessageBox.critical(self,title='ERROR',message='과목 입력 안됨')
        
        self.btnBack.clicked.connect(self.__priv)
        self.btnNext.clicked.connect(self.__next)
    
    def __priv(self):
        self.stat_sig.emit((-1,))
    
    def __next(self):
        self.hide()
        self.stat_sig.emit((0,self.comboSubject.currentText()))


class Grading2(QMainWindow,UI.Ui_Grading2):
    stat_sig=Signal(tuple)
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUI(self)

        self.__inputs=(
            (
                (self.lnAns11,self.lnAns12,self.lnAns13),
                (self.lnAns21,self.lnAns22,self.lnAns23)
            ),
            (
                (self.lnCor11,self.lnCor12,self.lnCor13),
                (self.lnCor21,self.lnCor22,self.lnCor23)
            )
        )
        
        self.btnBack.clicked.connect(self.__priv)
        self.btnRe.clicked.connect(self.__del_all)
        self.btnNext.clicked.connect(self.__next)
    
    def show(self,data):
        super().setVisible(True)
        
        self.__subject=data[0]
    
    def __del_all(self):
        for k in range(2):
            for j in range(2):
                for i in range(3):
                    self.__inputs[k][j][i].setText('')
    
    def __get_input(self): #입력값 불러오기, 오류 검사
        ans,cor=[],[]
        try:
            for j in range(2):
                for k in range(3):
                    #응답,정답 불러오기
                    a=self.__inputs[0][j][k].text().replace(' ','')
                    b=self.__inputs[1][j][k].text().replace(' ','')
                    #응답,정답 오류검사->저장
                    if len(a)!=len(b):
                        raise ValueError(f'Error with input({j},{k}):\nLength of answer({len(a)})\nis not equal length of correct({len(b)})')
                    if a and b:
                        a=list(a); b=list(b)
                        for x in range(len(a)):
                            a[x]=int(a[x])
                            b[x]=int(b[x])
                            if 0<a[x]<6:
                                if b[x]<1 or b[x]>5:
                                    raise ValueError(f'\nError with input({j},{k},{x}):\nanswer({a[x]}) and correct({b[x]})')
                            elif a[x]==6 or a[x]==7:
                                if b[x]!=0:
                                    raise ValueError(f'\nError with input({j},{k},{x}):\nanswer({a[x]}) and correct({b[x]})')
                            else:
                                raise ValueError(f'\nError with input({j},{k},{x}):\nanswer({a[x]}) and correct({b[x]})')
                        ans+=a; cor+=b
        except ValueError:
            msgbox=DetailErr(
                self,
                'ERROR',
                '값 입력 오류',
                sys.exc_info()
            )
            msgbox.exec_()
        else:
            if len(ans)==len(cor):
                return ans,cor
            else:
                QMessageBox.critical(self,'ERROR','개수 오류')
    
    def __priv(self): #이전 창으로 진행
        self.setVisible(False)
        self.stat_sig.emit((-1,parent))
    
    def __next(self): #다음 창으로 진행
        
        self.__err1={}
        self.__err2={}
        
        x=self.__get_input()
        if x:
            for k in range(len(x[0])):
                if x[0][k]<=5 and x[0][k]!=x[1][k]:
                    self.__err1[k+1]=(x[0][k],x[1][k])
                elif x[0][k]==7:
                    self.__err2[k+1]=None
            response=QMessageBox.question(
                self,
                "오답 확인",
                f"<오답 개수>\n선택형: {len(self.__err1)}\n서답형: {len(self.__err2)}\n채점 진행?"
            )
            if response==QMessageBox.Yes:
                self.setVisible(False)
                if self.__err1:
                    self.stat_sig.emit((0,self.__subject,self.__err1,self.__err2))
                elif self.__err2:
                    self.stat_sig.emit((1,self.__subject,self.__err1,self.__err2))
                else:
                    self.stat_sig.emit((2,self.__subject,self.__err1,self.__err2))


class Grading31(QMainWindow,UI.Ui_Grading31):
    stat_sig=Signal(tuple)
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUI(self)
        
        self.btnBack.clicked.connect(self.__priv)
        self.btnNext.clicked.connect(self.__next)
    
    def show(self,data):
        super().setVisible(True)
        self.__subject,self.__err1,self.__err2=data
        
        self.__err_num=tuple(self.__err1.keys())
        
        self.__score=[]
        for k,err in enumerate(self.__err1):
            self.__score.append(self.addWidgets(k,err))
        
        resize_height(self,self.centralwidget,self.widCent)
    
    def __priv(self):
        self.stat_sig.emit((-1,self.__subject))
    
    def __next(self):
        self.hide()
        try:
            for subject,widget in zip(self.__err_num,self.__score):
                self.__err1[subject]+=(widget.text(),)
            if self.__err2:
                self.stat_sig.emit((0,self.__subject,self.__err1,self.__err2))
            else:
                response=QMessageBox.question(self,'채점 완료?','채점 완료?')
                if response==QMessageBox.Yes:
                    self.setVisible(False)
                    self.stat_sig.emit((1,self.__subject,self.__err1,self.__err2))
        except ValueError:
            QMessageBox.critical(self,'Error','값 입력 오류')


class Grading32(QMainWindow,UI.Ui_Grading32):
    stat_sig=Signal(tuple)
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUI(self)
        
        self.btnBack.clicked.connect(self.__priv)
        self.btnNext.clicked.connect(self.__next)
    
    def show(self,data):
        super().setVisible(True)
        self.__subject,self.__err1,self.__err2=data
        
        self.__score=[]
        for k,err in enumerate(self.__err2):
            self.__score.append(self.addWidgets(k,err))
        
        resize_height(self,self.centralwidget,self.widCent)
    
    def __priv(self):
        self.setVisible(False)
        if self.__err1:
            self.stat_sig.emit((-2,self.__subject,self.__err1,self.__err2))
        else:
            self.stat_sig.emit((-1,self.__subject,self.__err1,self.__err2))
    
    def __next(self):
        try:
            for subject,wids in zip(self.__err2,self.__score):
                t1=wids[0].text()
                t2=wids[1].text()
                assert float(t1)<=float(t2)
                self.__err2[subject]=(t1,t2)
            response=QMessageBox.question(self,'채점 완료?','채점 완료?')
            if response==QMessageBox.Yes:
                self.setVisible(False)
                self.stat_sig.emit((0,self.__subject,self.__err1,self.__err2))
        except (ValueError, AssertionError):
            QMessageBox.critical(self,'Error','값 입력 오류')


class Grad_result(QMainWindow,UI.Ui_GradResult):
    def __init__(self,parent=None):
        def do_connect(signal,func,*args):
            signal.connect(lambda: func(*args))
        
        super().__init__(parent)
        self.setupUI(self)
        
        self.__parent=parent
        self.__subject_win=[]
        self.__chk=[]
        
        for k,subject in enumerate(current_subjects):
            if subject in current_wrong:
                score,err_cnt=get_score(subject)
                is_error=False
                if (score==100 and err_cnt!=0) or score>100 or score<0:
                    is_error=True
                    response=QMessageBox.warning(
                        self,
                        'ERROR',
                        'Data Error:\n점수=100, 오답수!=0',
                        QMessageBox.Ignore|QMessageBox.Cancel
                    )
                if not is_error or response==QMessageBox.Ignore:
                    chkDel,btn=self.addWidgets(k,subject,score,err_cnt)
                    if btn:
                        do_connect(btn.clicked,self.__show_detail,parent,subject)
                    self.__chk.append(chkDel)
            else:
                self.addWidgets(k,subject,None,None)
                self.__chk.append(None)
        
        resize_all(self,self.centralwidget,self.widCent)
        QShortcut(ESCAPE_SEQ,self).activated.connect(self.deleteLater)
        self.btnClose.clicked.connect(self.deleteLater)
        self.btnDel.clicked.connect(self.__del_res)
    
    def __del_res(self):
        global current_wrong,saved
        response=QMessageBox.question(self,'삭제?','복원 불가\n삭제?')
        if response==QMessageBox.Yes:
            saved=False
            for chk,subject in zip(self.__chk,current_subjects):
                if chk:
                    if chk.isChecked() and subject in current_wrong.keys():
                        del current_wrong[subject]
            self.deleteLater()
            if current_wrong:
                grad_win=Grad_result()
                grad_win.show()
            else:
                self.__parent.update_btn()
    
    def __show_detail(self,parent,subject):
        self.__subject_win.append(Grad_detail(None,subject))
        self.__subject_win[-1].show()


class Grad_detail(QMainWindow,UI.Ui_GradDetail):
    def __init__(self,parent,subject):
        if subject in current_subjects:
            super().__init__(parent)
            self.setupUI(self)
            wrongs=current_wrong[subject]
            try:
                if wrongs[0]:
                    self.addSel(wrongs[0])
                    self.widSel.resize(
                        self.widSel.width(),
                        self.widSel.sizeHint().height()
                    )
                if wrongs[1]:
                    self.addSupply(wrongs[1])
                    self.widSupply.resize(
                        self.widSupply.width(),
                        self.widSupply.sizeHint().height()
                    )
            except Exception as e:
                msgbox=DetailErr(
                    self,
                    'ERROR',
                    '오류 발생',
                    sys.exc_info(),
                    QMessageBox.Critical
                )
                msgbox.exec_()
                self.deleteLater()
            else:
                resize_height(self,self.centralwidget)
            
            QShortcut(ESCAPE_SEQ,self).activated.connect(self.deleteLater)
            self.btnClose.clicked.connect(self.deleteLater)
        else:
            QMessageBox.critical(self,'Error','없는 과목')
            self.deleteLater()

#(예상)등급계산
class Grade_calc(QMainWindow,UI.Ui_GradeCalc):
    def __init__(self,parent,grades=None):
        def cut_calc():
            self.__cut_calc.append(Cut_calc())
            self.__cut_calc[-1].show()
        
        super().__init__(parent)
        if current_subject_cnt==0:
            QMessageBox.critical(self,'Error','과목 입력 안됨')
        else:
            self.setupUI(self)
            
            self.__cut_calc=[]
            
            self.__input=[]
            for k,subject in enumerate(current_subjects):
                self.__input.append(self.addWidgets(k,subject,current_num[subject][0]))
            
            QShortcut(ESCAPE_SEQ,self).activated.connect(self.deleteLater)
            self.btnCutCalc.clicked.connect(cut_calc)
            self.btnClear.clicked.connect(self.__del_all)
            self.btnCalc.clicked.connect(self.__calc)
            self.btnClose.clicked.connect(self.deleteLater)

    def __calc(self):
        total_num   = 0
        best_grade  = 0
        worst_grade = 0
        try:
            for (grd_in1,grd_in2,chk),num in zip(self.__input,get_current_num()):
                if chk.isChecked():
                    grd1=int(grd_in1.text().replace(' ',''))
                    assert 0<grd1<9, f'grade must be 0<grade<9, but grade is {grd1}'
                    tmp=grd_in2.text().replace(' ','')
                    if tmp:
                        grd2=int(tmp)
                        assert 0<grd2<9, f'grade must be 0<grade<9, but grade is {grd2}'
                        best_grade +=min(grd1,grd2)*num
                        worst_grade+=max(grd1,grd2)*num
                    else:
                        best_grade +=grd1*num
                        worst_grade+=grd1*num
                    total_num+=num
            if not total_num:
                raise ValueError
        except (ValueError,AssertionError) as e:
            DetailErr(self,'Error','잘못된 입력',sys.exc_info())
        else:
            QMessageBox.information(
                self,
                '예상등급',
                f'최상: {(best_grade/total_num):.4}\n최하: {(worst_grade/total_num):.4}'
            )

    def __del_all(self):
        for grd_in1,grd_in2,_ in self.__input:
            grd_in1.setText('')
            grd_in2.setText('')
    
    #not used, but remain for future
    '''
    def __calc_full(self,grd1,grd2):
        #파싱
        if current_subject_cnt==len(grd1):
            res,tmp=[],[]
            res.append([grd1[0]])
            if grd2[0]:
                res.append([grd2[0]])
            for k in range(1,current_subject_cnt):
                if not grd1[k]:
                    break
                tmp=deepcopy(res)
                for j in range(len(res)):
                    res[j].append(grd1[k])
                if grd2[k]:
                    for j in range(len(tmp)):
                        tmp[j].append(grd2[k])
                    res+=tmp
            #등급 계산
            tmp=[]
            for a in res:
                x=0; k=0
                for subject in current_subjects:
                    x+=a[k]*current_num[subject][0]
                    k+=1
                tmp.append(round(x/sum(get_current_num()),4))
            return max(tmp),min(tmp)
        else:
            QMessageBox.critical(self,'Error','개수 오류')
            return None,None
    '''

#성적 입력
class Exam_input(QMainWindow,UI.Ui_ExamInput):
    def __init__(self,parent=None):
        global current_result
        def connect(k,btn):
            btn.clicked.connect(lambda: self.__del_subject(k))
        
        super().__init__(parent)
        self.__parent=parent
        if current_subjects:
            subjects=get_current_num(dictionary=True)
            self.setupUI(self,subjects.keys(),subjects.values())
            
            if current_result:
                for k,subject in enumerate(current_subjects):
                    if subject in current_result:
                        score,rank,person=current_result[subject]
                        self.ent[k][0].setText(score)
                        if rank and person:
                            self.ent[k][1].setText(str(rank))
                            self.ent[k][2].setText(str(person))
            
            for k,btn in enumerate(self.del_btn):
                connect(k,btn)
            self.btnClear.clicked.connect(lambda: self.__del_subject())
            self.btnCancel.clicked.connect(self.deleteLater)
            self.btnSet.clicked.connect(self.__get_input_and_close)
            
            #resize_height(self,self.centralwidget)
        else:
            QMessageBox.warning(self,'Error','과목 입력 안됨')
    
    def __del_subject(self,n=-1):
        assert type(n) is int, 'type of n must be int'
        assert -2<n<current_subject_cnt, f'must -1<n<{current_subject_cnt}, n={n}'
        if n<0:
            for lbScore,lbRank,lbPerson in self.ent:
                lbScore.setText('')
                lbRank.setText('')
                lbPerson.setText('')
        else:
            self.ent[n][0].setText('')
            self.ent[n][1].setText('')
            self.ent[n][2].setText('')
    
    def __get_input_and_close(self):
        global saved
        all_score_inputed = True
        all_inputed       = True
        results={}
        try:
            for ent,subject in zip(self.ent,current_subjects):
                score_in  = ent[0].text()
                rank_in   = ent[1].text()
                person_in = ent[2].text()
                
                if score_in:
                    if rank_in and person_in:
                        rank   = int(rank_in)
                        person = int(person_in)
                        results[subject] =(score_in,rank,person)
                    else:
                        all_inputed=False
                        results[subject]=(score_in,None,None)
                else:
                    all_score_inputed=False
        except ValueError:
            err_win=DetailErr(self,'Error','입력 값 오류',sys.exc_info())
            err_win.exec_()
        else:
            if not results:
                QMessageBox.warning(self,'진행?','모든 성적 미입력')
            else:
                if not all_score_inputed:
                    response=QMessageBox.question(self,'진행?','점수 미입력\n성적입력?')
                elif not all_inputed:
                    response=QMessageBox.question(self,'진행?','빈 칸 존재\n성적입력?')
                if all_inputed or response==QMessageBox.Yes:
                    global current_result
                    saved=False
                    current_result=results
                    
                    self.deleteLater()
                    result_win=Exam_result()
                    result_win.show()

#시혐 결과
class Exam_result(QMainWindow,UI.Ui_ExamResult):
    def __init__(self,parent=None):
        super().__init__(parent)
        if current_result:
            inputed_subjects=list(current_result.keys())
            
            self.__grade_win = []
            self.__cut_win   = []
            
            nums     = []
            scores   = []
            ranks    = []
            rank_str = []
            grades   = []
            percents = []
            
            all_rank_inputed=True
                
            for k,subject in enumerate(current_subjects):
                if subject in inputed_subjects:
                    score,rank,person=current_result[subject]
                    nums.append(current_num[subject][0])
                    scores.append(score)
                    ranks.append(rank)
                    rank_str.append(f'{rank}/{person}')
                    
                    if rank and person:
                        grade,percent=self.__get_grade(rank,person)
                        percents.append(round(percent,2))
                        grades.append(grade)
                    else:
                        all_rank_inputed=False
                        percents.append(None)
                        grades.append(None)
                else:
                    all_rank_inputed=False
                    nums.append(current_num[subject][0])
                    scores.append(None)
                    grades.append(None)
                    rank_str.append(None)
                    percents.append(None)
            
            if all_rank_inputed:
                total_grade=self.__get_total_grade(nums,grades)
            else:
                total_grade=0
            
            self.setupUI(self,current_subjects,nums,scores,grades,rank_str,percents,total_grade)
            
            QShortcut(ESCAPE_SEQ,self).activated.connect(self.deleteLater)
            self.btnCutCalc.clicked.connect(self.__cutcalc)
            self.btnGradeCalc.clicked.connect(self.__gradecalc)
            self.btnClose.clicked.connect(self.deleteLater)
            
        elif current_subjects:
            QMessageBox.critical(self,'Error','성적 입력 안됨')
        else:
            QMessageBox.critical(self,'Error','과목 입력 안됨')
    

    def __get_grade(self,rank,person):
        percent=rank/person*100
        cuts=(np.array(CUT_RATIO)*person*0.01).round()
        return np.searchsorted(cuts,rank)+1,percent

    def __get_total_grade(self,num,grd):
        array_num=np.array(num)
        array_grd=np.array(grd)
        result=(array_num*array_grd).sum()
        n=array_num.sum()
        return round(result/n,4)

    def __cutcalc(self):
        self.__cut_win.append(Cut_calc(None))
        self.__cut_win[-1].show()
    
    def __gradecalc(self):
        self.__grade_win.append(Grade_calc(None))
        self.__grade_win[-1].show()


#등급인원계산
class Cut_calc(QMainWindow,UI.Ui_CutCalc):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUI(self)
        
        for k,(ratio,lbGrade,lbRatio) in enumerate(zip(CUT_RATIO,self.lbGrades,self.lbRatios)):
            lbGrade.setText(str(k+1))
            lbRatio.setText(f'{ratio}%')
        
        QShortcut(ESCAPE_SEQ,self).activated.connect(self.deleteLater)
        QShortcut(QKeySequence.fromString('Enter'),self).activated.connect(self.__set_cuts)
        self.btnClose.clicked.connect(self.deleteLater)
        self.btnCalc.clicked.connect(self.__set_cuts)

    def __set_cuts(self):
        try:
            a=int(self.lnPersonCount.text())
        except ValueError:
            QMessageBox.critical(self,'Error','인원수 오류')
        else:
            for ratio,lbCut in zip(CUT_RATIO,self.lbCuts):
                lbCut.setText(str(round(a*ratio/100)))


if __name__=='__main__':
    import ctypes
    myappid = 'hys.grademanage2'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    
    app=QApplication()
    app.setWindowIcon(QIcon(PROGRAM_PATH+'icon.png'))
    
    main=Main()
    
    tmp=app.desktop().screenGeometry(main)
    screen_size=(tmp.width(),tmp.height())
    
    main.setGeometry(center_geometry(main))
    main.show()
    
    sys.exit(app.exec_())