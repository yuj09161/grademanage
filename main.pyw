# -*- coding: utf-8 -*-
from PySide2.QtCore import Qt, QRect, QTimer, QCoreApplication, QMetaObject
from PySide2.QtGui import QFont, QIcon, QCloseEvent, QKeySequence
from PySide2.QtWidgets import *
import UI

import os,sys,json
from decimal import Decimal as dec
from copy import deepcopy

ASK_ON_CLOSE=True

CUTS=(4,11,23,40,60,77,89,96,100)

#초기화

#전역 변수 정의
CURRENT_PATH = os.path.dirname(os.path.abspath('__file__'))+'\\'
PROGRAM_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))+'\\'

current_exam    = '111'
last_file       = ''
saved           = True
result_semester = {}
result_exam     = {}
current_num     = {}
current_wrong   = {}
current_result  = {}

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
            return str(score),str(err_cnt)
        else:
            return None
    if subject:
        return calc(subject)
    else:
        result=[]
        for subject in current_subjects:
            result.append(calc(subject))
        return result


def cut(person):
    cuts=(4,11,23,40,60,77,89,96,100); result=[]
    for cut in cuts:
        result.append(round(person*cut*0.01))
    return result


def get_current_num(*,name=False,dictionary=False):
    exam=int(current_exam[2])
    if name:
        if exam==3:
            return tuple(current_num.keys())
        else:
            name=[]
            for subject in current_num:
                if current_num[subject][exam]:
                    name.append(subject)
            return name
    else:
        if exam==3:
            if dictionary:
                tmp={}
                for subject in current_num:
                    tmp[subject]=current_num[subject][0]
                return tmp
            else:
                return tuple(value[0] for value in current_num.values())
        else:
            if dictionary:
                tmp={}
                for subject in current_num:
                    if current_num[subject][exam]:
                        tmp[subject]=current_num[subject][0]
                return tmp
            else:
                tmp=[]
                for value in current_num.values():
                    if value[exam]:
                        tmp.append(value[0])
                return tmp


#읽기
def load(name=None):
    def loader():
        global result_semester,result_exam,saved,last_file
        if name:
            #prog=Progbar('Load','Loading...')
            try:
                global current_num,current_wrong,current_result
                with open(name,'r',encoding='utf-8') as file:
                    result_semester,result_exam=json.load(file)
                if current_exam[2]=='3': #학기말
                    current_num,current_result=result_semester[current_exam[:2]]
                else: #중간고사or기말고사
                    current_num=result_semester[current_exam[:2]][0]
                    current_wrong,current_result=result_exam[current_exam]
                main.update_btn()
            except IOError as e:
                tmp=QMessageBox.warning(
                    self,
                    'Load Error',
                    f'데이터 불러오기 오류 발생\nTraceBack:\n{e}\n재시도?',
                    QMessageBox.Retry|QMessageBox.Cancel
                )
                if tmp==QMessageBox.Retry:
                    load(name)
            except json.JSONDecodeError as e:
                QMessageBox.critical('Error','파일 형식 오류')
            except ValueError as e:
                QMessageBox.critical('Error','파일 형식 오류')
            else:
                saved=True
                last_file=name
            finally:
                prog.destroy()
    if not name:
        name=QFileDialog.getOpenFileName(self,'저장',CURRENT_PATH)
    if saved:
        loader()
    else:
        var=QMessageBox.askcancel('Info','저장 안됨\n저장?')
        if var:
            save()
            loader()
        elif var==False:
            loader()


#쓰기
def save(last=False,*,name=None):
    global result_semester,result_exam,last_file,saved
    if last:
        name=last_file
    if not name:
        name=asksave()
    if name:
        #prog=Progbar('Save','Saving...')
        if current_exam[2]=='3': #학기말
            result_semester[current_exam[:2]]=[current_num,current_result]
        else: #중간고사or기말고사
            result_semester[current_exam[:2]][0]=current_num
            result_exam[current_exam]=[current_wrong,current_result]
        try:
            with open(name,'w',encoding='utf-8') as file:
                json.dump((result_semester,result_exam),file,indent=4,ensure_ascii=False)
        except IOError as e:
                tmp=QMessageBox.warning(
                    self,
                    'Save Error',
                    f'데이터 저장 중 오류 발생\nTraceBack:\n{e}\n재시도?',
                    QMessageBox.Retry|QMessageBox.Cancel
                )
                if tmp==QMessageBox.Retry: 
                    save(name=name)
        else:
            last_file=name
            saved=True
        finally:
            prog.destroy()


'''창 클래스들'''

#Main Window class
class Main(QMainWindow,UI.Ui_Main):
    def __init__(self):
        super().__init__()
        
        #pre-define Variables
        order=(2,0,2)
        
        self.setupUI(self)
        
        #Define Variables
        
        #Connect Slots (QComboBox)
        self.comboYear.currentIndexChanged.connect(lambda: self.btnSet.setStyleSheet('color:red'))
        self.comboSemester.currentIndexChanged.connect(lambda: self.btnSet.setStyleSheet('color:red'))
        self.comboExam.currentIndexChanged.connect(lambda: self.btnSet.setStyleSheet('color:red'))
        
        #Connect Slots (QButtons)
        self.btnSubject.clicked.connect(Subject_In)
        self.btnGrading.clicked.connect(Grade_ing)
        self.btnGradingRes.clicked.connect(Grad_result)
        self.btnCalc.clicked.connect(Grade_calc)
        self.btnInput.clicked.connect(Exam_input)
        self.btnRes.clicked.connect(Exam_result)
        self.btnSet.clicked.connect(self.__set_exam)
        #self.btnManage.clicked.connect()
        self.btnManage.setEnabled(False)
        
        #Connect Slots (QAction)
        self.save.triggered.connect(save)
        self.load.triggered.connect(load)
        self.exit.triggered.connect(self.close)
        self.cut_calc.triggered.connect(Cut_calc)
        #self.license.triggered.connect()
        #self.about.triggered.connect()
    

    def closeEvent(self,event):
        print('close')
        if ASK_ON_CLOSE and not saved:
            res=QMessageBox.askcancel('저장','저장?')
            if res==True:
                save(True)
                event.accept()
            elif res==False:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()
    
    #시험 설정

    def __set_exam(self):
        global current_num,current_wrong,current_result,\
               current_exam,current_subjects,current_subject_cnt
        def saving(): #시험 결과 저장
            global result_semester,result_exam
            if current_exam[2]=='3':
                result_semester[current_exam[:2]]=[current_num,current_result]
            else:
                result_semester[current_exam[:2]][0]=current_num
                result_exam[current_exam]=[current_wrong,current_result]
        semester=''
        for a in range(3): #과목 불러오기
            semester+=str(self.__option[a].index(self.__exam[a].get())+1)
        if semester[2]=='3': #학기말
            #시험 결과 저장/불러오기
            saving()
            current_exam=semester
            current_num,current_result=result_semester[current_exam[:2]]
        else: #중간고사or기말고사
            #시험 결과 저장/불러오기
            saving()
            current_exam=semester
            current_num=result_semester[current_exam[:2]][0]
            current_wrong,current_result=result_exam[current_exam]
        
        #버튼 상태 설정
        main.update_btn()
        #get current subject
        current_subjects=get_current_num(name=True)
        current_subject_cnt=len(current_subjects)
    
    #버튼 상태 업데이트

    def update_btn(self):
        self.__changeBtn.setStyleSheet('color:black')
        if current_num:
            if current_exam[2]=='3':
                self.__btn[0][1].setEnabled(False)
                self.__btn[0][2].setEnabled(False)
            else:
                self.__btn[0][1].setEnabled(True)
                if current_wrong:
                    self.__btn[0][2].setEnabled(True)
                else:
                    self.__btn[0][2].setEnabled(False)
            self.__btn[1][0].setEnabled(True)
            self.__btn[1][1].setEnabled(True)
            if current_result:
                self.__btn[1][2].setEnabled(True)
            else:
                self.__btn[1][2].setEnabled(False)
        else:
            self.__btn[0][1].setEnabled(False)
            self.__btn[0][2].setEnabled(False)
            self.__btn[1][0].setEnabled(False)
            self.__btn[1][1].setEnabled(False)
            self.__btn[1][2].setEnabled(False)

'''
#진행 바(연속형)
class Progbar(QMainWindow,UI.Ui_Progbar):
    def __init__(self,title,txt,leng=200,time=5):
        super().__init__(self)
        self.setupUI(self)

        prog=Progressbar(self,mode='indeterminate',length=leng)
        prog.pack()
        prog.start(interval=time)
'''

#과목 입력
class Subject_In(QMainWindow,UI.Ui_SubjectIn):
    def __init__(self):
        super().__init__()
        self.setupUI(self)
        #초기화
        self.__inbox=[]
        self.__invar=[]
        #기존 값 불러오기
        if current_num:
            for subject in current_num:
                self.__add_subject(subject,current_num[subject])

    def __add_subject(self,subject=None,value=None):
        n=len(self.__inbox)
        if subject:
            pass
        else:
            pass
        self.__inbox.append(
            (



            )
        )
        for a in range(len(self.__inbox)):
            if self.__inbox[a]:
                for b in range(5):
                    self.__inbox[a][b].grid(row=a+1,column=b)

    def __del_subject(self,n):
        for a in range(5):
            self.__inbox[n][a].grid_forget()
        self.__inbox[n]=None

    def __set_subject(self):
        global current_num,saved,current_subjects,current_subject_cnt
        current_num={}; current_subjects=[]
        try:
            for k in range(len(self.__inbox)):
                if self.__inbox[k]:
                    current_num[self.__invar[k][0].get()]=(int(self.__invar[k][1].get()),self.__invar[k][2].get(),self.__invar[k][3].get())
                    saved=False
        except ValueError:
            QMessageBox.critical(title='ERROR',message='잘못된 값 입력')
        else:
            current_subjects=get_current_num(name=True)
            current_subject_cnt=len(current_subjects)
            self.destroy()
            main.update_btn()

#가채점 입력
class Grade_ing:
    def __init__(self):
        super().__init__()
        self.setupUI(self)
        self.__err1,self.__err2={},{}

        self.__select()

    def __select(self):
        def next():
            top.destroy()
            self.__grading()
        try:
            self.__subject.set(list(current_subjects)[0])
        except IndexError:
            QMessageBox.critical(title='ERROR',message='과목 입력 안됨')
        else:
            top=QMainWindow(main)
            top.resizable(False,False)
        self.setupUI(self)



        label.grid(row=0,column=0); drop.grid(row=0,column=1)
        btn0.grid(row=0,column=0); btn1.grid(row=0,column=1)
        frame_top.grid(row=0,column=0)
        frame_bottom.grid(row=1,column=0)

    def __grading(self):
        def get_input(): #입력값 불러오기, 오류 검사
            ans,cor=[],[]
            try:
                for j in range(2):
                    for k in range(3):
                        #응답,정답 불러오기
                        a=inputs[0][j][k].get()
                        b=inputs[1][j][k].get()
                        #응답,정답 오류검사->저장
                        if len(a)!=len(b) or len(a)>5 or len(b)>5:
                            raise ValueError
                        if a and b:
                            a=list(a); b=list(b)
                            for x in range(len(a)):
                                a[x]=int(a[x])
                                b[x]=int(b[x])
                                if 0<a[x]<6:
                                    if b[x]<1 or b[x]>5:
                                        raise ValueError
                                elif a[x]==6 or a[x]==7:
                                    if b[x]!=0:
                                        raise ValueError
                                else:
                                    raise ValueError
                            ans+=a; cor+=b
            except ValueError:
                QMessageBox.critical(title='ERROR',message='값 입력 오류')
                return None
            else:
                if len(ans)==len(cor):
                    return ans,cor
                else:
                    QMessageBox.critical(title='ERROR',message='개수 오류')
                    return None
        def priv(): #이전 창으로 진행
            top.destroy()
            self.__select()
        def del_all():
            for k in range(2):
                for j in range(2):
                    for i in range(3):
                        inputs[k][j][i].set('')
        def next(): #다음 창으로 진행
            x=get_input()
            if x:
                for k in range(len(x[0])):
                    if x[0][k]<=5 and x[0][k]!=x[1][k]:
                        self.__err1[k+1]=(x[0][k],x[1][k])
                    elif x[0][k]==7:
                        self.__err2[k+1]=None
                n,m=len(self.__err1),len(self.__err2)
                var=QMessageBox.ask("오답 확인",
                    "<오답 개수>\n선택형: %s\n서답형: %s\n채점 진행?"
                    %(n,m)
                )
                if var:
                    top.destroy()
                    if self.__err1:
                        self.__err_sel()
                    elif self.__err2:
                        self.__err_comp()
                    else:
                        self.__result()
        #메인
        top=QMainWindow(main)
        top.resizable(False,False)
        self.setupUI(self)

        inputs=[]
        str_left=('범\n례','응\n답','정\n답')
        str_top=('1~5','6~10','11~15','16~20','21~25','26~30')

        for a in range(3):
            pass
        for a in range(2):
            for b in range(3):
                pass
        for a in range(2):
            inputs.append([])
            for b in range(2):
                inputs[a].append([])
                for c in range(3):
                    pass



        f_mid.grid(row=1,column=0,columnspan=3)

    def __err_sel(self):
        def priv():
            top.destroy()
            self.__grading()
        def next():
            try:
                for k in range(len(score_in)):
                    self.__err1[err_num[k]]+=(score_in[k].get(),)
                if self.__err2:
                    top.destroy()
                    self.__err_comp()
                else:
                    var=QMessageBox.ask('채점 완료?','채점 완료?')
                    if var:
                        top.destroy()
                        self.__result()
            except ValueError:
                QMessageBox.critical('Error','값 입력 오류')
        top=QMainWindow(main)
        top.resizable(False,False)
        self.setupUI(self)


        err_num=list(self.__err1.keys())
        score_in=[]
        for k in range(len(self.__err1)):

            score_in[k].grid(row=k+1,column=1)
        mid.grid(row=0,column=0,columnspan=2)
        if self.__err1:
            str_btn='다음→'
        else:
            str_btn='채점'


    def __err_comp(self):
        def priv():
            top.destroy()
            if self.__err1:
                self.__err_sel()
            else:
                self.__grading()
        def next():
            try:
                for k in range(len(score_in)):
                    self.__err2[num[k]]=(score_in[k].get(),score_in2[k].get())
                var=QMessageBox.ask('채점 완료?','채점 완료?')
                if var:
                    top.destroy()
                    self.__result()
            except ValueError:
                QMessageBox.critical('Error','값 입력 오류')
        top=QMainWindow(main)
        top.resizable(False,False)
        self.setupUI(self)

        top_str=('번호','득점','배점')
        for k in range(3):
            pass
        num=list(self.__err2.keys())
        score_in,score_in2=[],[]
        for k in range(len(self.__err2)):
            

            score_in[k].grid(row=k+1,column=1)
            score_in2[k].grid(row=k+1,column=2)
        mid.grid(row=0,column=0,columnspan=2)


    def __result(self):
        def write():
            global current_wrong,saved
            current_wrong[self.__subject.get()]=(self.__err1,self.__err2)
            saved=False
        def next():
            Grad_detail(self.__subject.get())
        def close():
            top.destroy()
        top=QMainWindow(main)
        top.resizable(False,False)
        self.setupUI(self)
        if self.__err1 or self.__err2:
            score=100
            for err1 in self.__err1:
                score=score-dec(self.__err1[err1][2])
            for err2 in self.__err2:
                score=score-dec(self.__err2[err2][1])+dec(self.__err2[err2][0])

        else:
            pass

        write()

class Grad_result(QMainWindow,UI.Ui_GradResult):
    def __init__(self):
        super().__init__()
        self.setupUI(self)
        def btn_make(subject,n):
            pass
        
        def del_res(all_subject=False):
            global current_wrong
            var=QMessageBox.ask('삭제?','복원 불가\n삭제?')
            if var:
                if all_subject:
                    for k in range(current_subject_cnt):
                        if current_subjects[k] in current_wrong.keys():
                            del current_wrong[current_subjects[k]]
                else:
                    for k in range(current_subject_cnt):
                        if chk[k].get() and (current_subjects[k] in current_wrong.keys()):
                            del current_wrong[current_subjects[k]]
                top.destroy()
                if current_wrong:
                    Grad_result()
        
        if current_wrong:
            super().__init__(self)
            score=get_score()
        self.setupUI(self)
        if True:
            self_str=('과목명','오답 수','점수','상세','삭제?')

            lab,chk=[],[]
            for k in range(5):
                pass
            for k in range(current_subject_cnt):
                tmp_btn=None

                lab.append([])
                if score[k]:

                    lab[k][0].grid(row=k+1,column=1)

                    lab[k][1].grid(row=k+1,column=2,padx=5)
                    if score[k][0]!='100':
                        btn_make(current_subjects[k],k+1)
                else:
                    pass



            f_mid.grid(row=0,column=0,columnspan=2)
            f_bot.grid(row=1,column=0,sticky='w')
        else:
            QMessageBox.critical(title='ERROR',message='가채점 안됨')

class Grad_detail(QMainWindow,UI.Ui_GradDetail):
    def __init__(self,subject):
        if subject in current_subjects:
            super().__init__(self)
            wrong=current_wrong[subject]
            if wrong[0]:

                top1=('번호','응답','정답','배점')
                err_num=list(wrong[0].keys())

                for k in range(4):
                    pass
                for k in range(len(wrong[0])):

                    for j in range(3):
                        pass
                err_sel.grid(row=0,column=0,padx=5,pady=5,sticky='w')
            if wrong[1]:

                top2=('번호','득점','배점')
                err_num=list(wrong[1].keys())

                for k in range(3):
                    pass
                for k in range(len(wrong[1])):

                    for j in range(2):
                        pass
                err_comp.grid(row=1,column=0,padx=5,pady=5,sticky='w')

        else:
            QMessageBox.critical('Error','없는 과목')

#(예상)등급계산
class Grade_calc(QMainWindow,UI.Ui_GradeCalc):
    def __init__(self,grades=None):
        if current_subject_cnt==0:
            QMessageBox.critical('Error','과목 입력 안됨')
        else:
            super().__init__(self)
        self.setupUI(self)
        if True:
            str_self=('과목명','시수','등급1','등급2','포함?')
            for a in range(5):
                pass
            self.__grade1=[]
            self.__grade2=[]
            self.__chk=[]
            k=0
            for subject in current_subjects:





                k+=1
            f_mid.grid(row=0,column=0,columnspan=2)



            f_bot.grid(row=1,column=1,sticky='e')
            k+=1
    

    def __calc(self):
        try:
            nums=get_current_num()
            total_num=0
            max_grade=0
            min_grade=0
            for k in range(current_subject_cnt):
                if self.__chk[k].get():
                    in2=self.__grade2[k].get()
                    grd1=int(self.__grade1[k].get()) #in1=self.__grade1[k].get()
                    if 0<grd1>9:
                        raise ValueError
                    total_num+=nums[k]
                    if in2:
                        grd2=int(in2)
                        max_grade+=min(grd1,grd2)*nums[k]
                        min_grade+=max(grd1,grd2)*nums[k]
                    else:
                        max_grade+=grd1*nums[k]
                        min_grade+=grd1*nums[k]
            if not total_num:
                raise ValueError
        except ValueError:
            QMessageBox.critical('Error','잘못된 입력')
        else:
            QMessageBox.info(
                '결과',
                '최고: %s\n최저: %s' %(
                    round(max_grade/total_num,4),
                    round(min_grade/total_num,4)
                )
            )
    

    def __del_all(self):
        for k in range(current_subject_cnt):
            self.__grade1[k].set('')
            self.__grade2[k].set('')
    
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
            QMessageBox.critical('Error','개수 오류')
            return None,None
    '''

#성적 입력
class Exam_input(QMainWindow,UI.Ui_ExamInput):
    def __init__(self):
        super().__init__()
        self.setupUI(self)
        global current_result
        def btn_make(n):
            pass
        def del_subject(n):
            for k in range(3):
                self.__ent[n][k].set('')
        def del_all():
            for k in range(current_subject_cnt):
                del_subject(k)
        if current_subjects:
            super().__init__(self)
        self.setupUI(self)
        if True:
            self_str=('과목명','시수','원점수','석차','인원수')
            self.__ent=[]
            for k in range(5):
                pass
            k=0
            for subject in current_subjects:

                self.__ent.append([])
                for j in range(3):

                    if subject in current_result.keys():
                        value=current_result[subject][j]
                        self.__ent[-1][j].set(value if value else '')

                btn_make(k)
                k+=1
            #bottom buttons



            #grid frames
            f_mid.grid(row=0,column=0,columnspan=2)
            f_bot.grid(row=1,column=1,sticky='e')
        else:
            QMessageBox.critical('Error','과목 입력 안됨')
    

    def __end(self):
        global saved
        all_entered=True; results=[]
        try:
            for k in range(current_subject_cnt):
                score=self.__ent[k][0].get()
                grade=self.__ent[k][1].get()
                count=self.__ent[k][2].get()
                if not score:
                    score=None
                    all_entered=False
                if grade:
                    grade=int(grade)
                else:
                    grade=None
                    all_entered=False
                if count:
                    count=int(count)
                else:
                    count=None
                    all_entered=False
                results.append((score,grade,count))
        except ValueError:
            QMessageBox.critical('Error','입력 값 오류')
        else:
            if not all_entered:
                proceed_blank=QMessageBox.ask('Info','빈 칸 존재\n성적입력?')
            if all_entered or proceed_blank:
                k=0
                for result in results:
                    if all(result):
                        current_result[current_subjects[k]]=result
                        saved=False
                    elif result[0]:
                        current_result[current_subjects[k]]=(result[0],None,None)
                    k+=1
                self.destroy()
                Exam_result()

#시혐 결과
class Exam_result(QMainWindow,UI.Ui_ExamResult):
    def __init__(self):
        super().__init__()
        self.setupUI(self)
        if current_result:
            super().__init__(self)
        self.setupUI(self)
        if True:
            self_str=('과목','시수','점수','석차','등급','백분위')
            for k in range(6):
                pass
            self.__grades=[]
            all_rank_inputed=True
            k=0
            for subject in current_subjects:

                if subject in current_result.keys():
                    score,rank,total_person=current_result[subject]

                    if rank and total_person:
                        grade,percent=self.__get_grade(rank,total_person)


                        self.__grades.append(grade)
                    else:

                        all_rank_inputed=False
                        self.__grades.append(None)
                else:

                    all_rank_inputed=False
                k+=1
            f_mid.grid(row=0,column=0,columnspan=2)
            if all_rank_inputed:
                pass

        elif current_subjects:
            QMessageBox.critical('Error','성적 입력 안됨')
        else:
            QMessageBox.critical('Error','과목 입력 안됨')
    

    def __get_grade(self,rank,person):
        percent=rank/person*100
        cuts=cut(person)
        grade=0
        for k in range(9):
            if rank<=cuts[k]:
                grade=k+1
                break
        '''
        if not grade:
            grade=9
        '''
        return grade,percent
    

    def __calc(self,num,grd):
        result=0
        n=0
        for k in range(len(num)):
            result+=num[k]*grd[k]
            n+=num[k]
        return round(result/n,4)
    

    def __to_grading(self):
        self.destroy()
        Grade_calc(self.__grades)

#등급인원계산
class Cut_calc(QMainWindow,UI.Ui_CutCalc):
    def __init__(self):
        super().__init__()
        self.setupUI(self)
        result=['','','','','','','','','']
        super().__init__(self)
        self.setupUI(self)



        self.__ent.bind('<Return>',self.__get)
        self.__ent.grid(row=0,column=1)
        str_self=('등급','누적비율','누적인원수')
        for k in range(3):
            pass
        for k in range(9):
            pass



        f_self.grid(row=0,column=0)
        self.__f_mid.grid(row=1,column=0)
        f_bot.grid(row=2,column=0)
    
    

    def __get(self):
        try:
            a=int(self.__ent.get())
        except ValueError:
            QMessageBox.critical('Error','인원수 오류')
        else:
            result=[]
            for k in CUTS:
                result.append(round(a*k/100))
            for k in range(9):
                pass
"""
#안내 Root Class
class Notice(QMainWindow,UI.Ui_Notice):
    def __init__(self,name,fileName,string):
        try:
            with open(fileName+'.txt','r') as file:
                txt=file.readlines()
        except:
            txt=string
        super().__init__()
        self.setupUI(self)


    def form(self,string):
        text=''
        for line in string.splitlines():
            if line:
                text+=line+'\n'
        return text[:-1]

#도움말
class Help(Notice):
    def __init__(self):
        super().__init__()
        self.setupUI(self)
        text='''

'''
        txt=super().form(text)
        super().__init__()

#라이선스
class License(Notice):
    def __init__(self):
        super().__init__()
        self.setupUI(self)
        text='''

'''
        txt=super().form(text)
        super().__init__()

#정보
class Info(Notice):
    def __init__(self):
        super().__init__()
        self.setupUI(self)
        text='''
성적계산기
made by HYS
'''
        txt=super().form(text)
        super().__init__()
"""
if __name__=='__main__':
    import ctypes
    myappid = 'hys.grademanage'
    
    app=QApplication()
    
    main=Main()
    main.show()
    
    sys.exit(app.exec_())