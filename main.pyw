import tkinter as tk
from tkinter import messagebox as msgbox
from tkinter.ttk import Progressbar,Combobox

from tkinter.filedialog import askopenfilename as askopen
from tkinter.filedialog import asksaveasfilename as asksave

import json
from decimal import Decimal as dec
from copy import deepcopy

ASK_ON_CLOSE=True

CUTS=(4,11,23,40,60,77,89,96,100)

#초기화

#전역 변수 생성
current_exam='111'; last_file=''; saved=True
result_semester,result_exam={},{}
for a in range(1,4):
    for b in range(1,3):
        result_semester[str(10*a+b)]=[{},{}]
        for c in range(1,3):
            result_exam[str(100*a+10*b+c)]=[{},{}]
current_num={}
current_wrong={}
current_result={}

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
            prog=Progbar('Load','Loading...')
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
            except IOError:
                tmp=msgbox.askretrycancel('Error','읽기 에러')
                if tmp:
                    load(name)
            except json.JSONDecodeError as e:
                msgbox.showerror('Error','파일 형식 오류')
            except ValueError as e:
                msgbox.showerror('Error','파일 형식 오류')
            else:
                saved=True
                last_file=name
            finally:
                prog.destroy()
    if not name:
        name=askopen()
    if saved:
        loader()
    else:
        var=msgbox.askyesnocancel('Info','저장 안됨\n저장?')
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
        prog=Progbar('Save','Saving...')
        if current_exam[2]=='3': #학기말
            result_semester[current_exam[:2]]=[current_num,current_result]
        else: #중간고사or기말고사
            result_semester[current_exam[:2]][0]=current_num
            result_exam[current_exam]=[current_wrong,current_result]
        try:
            with open(name,'w',encoding='utf-8') as file:
                json.dump((result_semester,result_exam),file,indent=4,ensure_ascii=False)
        except IOError:
            sel=msgbox.askretrycancel('Error','쓰기 에러')
            if sel: 
               save(name=name)
        else:
            last_file=name
            saved=True
        finally:
            prog.destroy()


'''창 클래스들'''
#Main Window class
class Main(tk.Tk):
    def __init__(self):
        global main
        super().__init__()
        main=self
        self.resizable(False,False)
        self.title('성적계산기')
        
        '''중앙 버튼'''
        #메뉴 생성
        menu_bar=tk.Menu(self)
        menu_file=tk.Menu(menu_bar,tearoff=0)
        menu_tool=tk.Menu(menu_bar,tearoff=0)
        menu_info=tk.Menu(menu_bar,tearoff=0)
        #파일
        menu_file.add_command(label='불러오기',command=load)
        menu_file.add_command(label='저장',command=lambda: save(True))
        menu_file.add_command(label='다른 이름으로 저장',command=save)
        menu_file.add_separator()
        menu_file.add_command(label='종료',command=self.quit)
        #도구
        menu_tool.add_command(label='등급인원계산',command=Cut_calc)
        #정보
        menu_info.add_command(label='도움말',command=Help)
        menu_info.add_command(label='License',command=License)
        menu_info.add_separator()
        menu_info.add_command(label='정보',command=Info)
        #메뉴 등록
        menu_bar.add_cascade(label='파일',menu=menu_file)
        menu_bar.add_cascade(label='도구',menu=menu_tool)
        menu_bar.add_cascade(label='정보',menu=menu_info)

        '''고사 설정 바'''
        frame_top=tk.Frame(self)
        self.__option=(('1학년','2학년','3학년'),('1학기','2학기'),('중간고사','기말고사','학기말'))
        self.__exam=[]
        order=(2,0,1)
        for a in range(3):
            self.__exam.append(tk.StringVar())
            self.__exam[a].set(self.__option[a][order[a]])
            Combobox(frame_top,textvariable=self.__exam[a],values=self.__option[a],width=7).grid(row=0,column=a)
            self.__exam[a].trace('w',lambda *args:self.__changeBtn.config(fg='red'))
        self.__changeBtn=tk.Button(frame_top,text='변경',command=self.__set_exam)
        self.__changeBtn.grid(row=0,column=3)

        frame_top.grid(row=0,column=0,columnspan=2)

        '''메인 버튼'''
        #버튼 생성
        self.__btn=[[],[]]
        frame1=tk.Frame(self,relief='solid',borderwidth=1,padx=10,pady=10)
        frame2=tk.Frame(self,relief='solid',borderwidth=1,padx=10,pady=10)
        self.__btn[0].append(tk.Button(frame1,text='과목입력',command=Input_subject))
        self.__btn[0][0].grid(row=0,column=0,sticky='NSEW')
        self.__btn[0].append(tk.Button(frame1,text='가채점 입력',command=Grade_ing))
        self.__btn[0][1].grid(row=1,column=0,sticky='NSEW')
        self.__btn[0].append(tk.Button(frame1,text='가채점 결과\n삭제/초기화',command=Grad_result))
        self.__btn[0][2].grid(row=2,column=0,sticky='NSEW')
        self.__btn[1].append(tk.Button(frame2,text='등급계산',command=Grade_calc))
        self.__btn[1][0].grid(row=0,column=0,sticky='NSEW')
        self.__btn[1].append(tk.Button(frame2,text='성적입력',command=Exam_input))
        self.__btn[1][1].grid(row=1,column=0,sticky='NSEW')
        self.__btn[1].append(tk.Button(frame2,text='시험결과',command=Exam_res))
        self.__btn[1][2].grid(row=2,column=0,sticky='NSEW')
        self.__btn[1].append(tk.Button(frame2,text='성적분석',state='disable'))
        self.__btn[1][3].grid(row=3,column=0,sticky='NSEW')
        frame1.grid(row=1,column=0,padx=10,pady=10)
        frame2.grid(row=1,column=1,padx=10,pady=10)
        main.update_btn()

        #종료 시 저장 확인
        self.protocol("WM_DELETE_WINDOW",self.__on_close)
        #시작 시 데이터 로드
        load('save.json')
        #창 배치
        self.config(menu=menu_bar)
        
        #insert test code here
        '''
        a=()
        a.destroy()
        '''
        
        #메인루프
        self.mainloop()
    
    def __on_close(self):
        if ASK_ON_CLOSE and not saved:
            res=msgbox.askyesnocancel('저장','저장?')
            if res==True:
                save(True)
                self.destroy()
            elif res==False:
                self.destroy()
            else:
                return
        else:
            self.destroy()
    
    #시험 설정
    def __set_exam(self):
        global current_num,current_wrong,\
                current_result,current_exam,\
                current_subjects,current_subject_cnt
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
        self.__changeBtn['fg']='black'
        if current_num:
            if current_exam[2]=='3':
                self.__btn[0][1]['state']='disable'
                self.__btn[0][2]['state']='disable'
            else:
                self.__btn[0][1]['state']='active'
                if current_wrong:
                    self.__btn[0][2]['state']='active'
                else:
                    self.__btn[0][2]['state']='disable'
            self.__btn[1][0]['state']='active'
            self.__btn[1][1]['state']='active'
            if current_result:
                self.__btn[1][2]['state']='active'
            else:
                self.__btn[1][2]['state']='disable'
        else:
            self.__btn[0][1]['state']='disable'
            self.__btn[0][2]['state']='disable'
            self.__btn[1][0]['state']='disable'
            self.__btn[1][1]['state']='disable'
            self.__btn[1][2]['state']='disable'


#진행 바(연속형)
class Progbar(tk.Toplevel):
    def __init__(self,title,txt,leng=200,time=5):
        super().__init__(main)
        self.title(title)
        tk.Label(self,text=txt).pack()
        prog=Progressbar(self,mode='indeterminate',length=leng)
        prog.pack()
        prog.start(interval=time)


#과목 입력
class Input_subject(tk.Toplevel):
    def __init__(self):
        #초기화
        self.__inbox,self.__invar=[],[]
        super().__init__(main)
        self.resizable(False,False)
        self.title('과목 입력')
        self.__mid,self.__footer=tk.Frame(self),tk.Frame(self)
        #버튼 생성
        tk.Button(self,text='+추가',command=self.__add_subject).grid(row=1,column=0,sticky='w',padx=5)
        tk.Button(self.__footer,text='취소',command=self.destroy).grid(row=0,column=0,sticky='e')
        tk.Button(self.__footer,text='입력',command=self.__set_subject).grid(row=0,column=1,sticky='e')
        #메뉴 생성/배치
        menu_str=('과목명','시수','중간','기말','삭제')
        for k in range(5):
            tk.Label(self.__mid,text=menu_str[k]).grid(row=0,column=k)
        #메뉴,버튼 그룹 배치
        self.__mid.grid(row=0,column=0,columnspan=2)
        self.__footer.grid(row=1,column=1,rowspan=1,columnspan=1,sticky='e',padx=5)
        #기존 값 불러오기
        if current_num:
            for subject in current_num:
                self.__add_subject(subject,current_num[subject])
    def __add_subject(self,subject=None,value=None):
        n=len(self.__inbox)
        if subject:
            self.__invar.append((tk.StringVar(value=subject),tk.StringVar(value=value[0]),tk.BooleanVar(value=value[1]),tk.BooleanVar(value=value[2])))
        else:
            self.__invar.append((tk.StringVar(),tk.StringVar(),tk.BooleanVar(),tk.BooleanVar()))
        self.__inbox.append(
            (
                tk.Entry(self.__mid,width=15,textvariable=self.__invar[n][0]),
                tk.Entry(self.__mid,width=5,textvariable=self.__invar[n][1]),
                tk.Checkbutton(self.__mid,variable=self.__invar[n][2]),
                tk.Checkbutton(self.__mid,variable=self.__invar[n][3]),
                tk.Button(self.__mid,text='X',command=lambda:self.__del_subject(n))
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
            msgbox.showerror(title='ERROR',message='잘못된 값 입력')
        else:
            current_subjects=get_current_num(name=True)
            current_subject_cnt=len(current_subjects)
            self.destroy()
            main.update_btn()


#가채점 입력
class Grade_ing:
    def __init__(self):
        self.__err1,self.__err2={},{}
        self.__subject=tk.StringVar()
        self.__select()
    def __select(self):
        def next():
            top.destroy()
            self.__grading()
        try:
            self.__subject.set(list(current_subjects)[0])
        except IndexError:
            msgbox.showerror(title='ERROR',message='과목 입력 안됨')
        else:
            top=tk.Toplevel(main)
            top.resizable(False,False)
            top.title('과목 선택')
            frame_top=tk.Frame(top);frame_bottom=tk.Frame(top)
            drop=tk.OptionMenu(frame_top,self.__subject,*list(current_subjects))
            label=tk.Label(frame_top,text='과목: ')
            btn0=tk.Button(frame_bottom,text='취소',command=top.destroy)
            btn1=tk.Button(frame_bottom,text='다음→',command=next)
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
                msgbox.showerror(title='ERROR',message='값 입력 오류')
                return None
            else:
                if len(ans)==len(cor):
                    return ans,cor
                else:
                    msgbox.showerror(title='ERROR',message='개수 오류')
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
                var=msgbox.askyesno("오답 확인",
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
        top=tk.Toplevel(main)
        top.resizable(False,False)
        top.title('가채점')
        f_mid=tk.Frame(top)
        inputs=[]
        str_left=('범\n례','응\n답','정\n답')
        str_top=('1~5','6~10','11~15','16~20','21~25','26~30')
        tk.Label(top,text='과목: '+self.__subject.get()).grid(row=0,column=0,columnspan=3)
        for a in range(3):
            tk.Label(f_mid,text=str_left[a]).grid(row=2*a,column=0,rowspan=2)
        for a in range(2):
            for b in range(3):
                tk.Label(f_mid,text=str_top[a*3+b]).grid(row=a,column=b+1)
        for a in range(2):
            inputs.append([])
            for b in range(2):
                inputs[a].append([])
                for c in range(3):
                    inputs[a][b].append(tk.StringVar())
                    tk.Entry(f_mid,textvariable=inputs[a][b][c],width=10).grid(row=a*2+b+2,column=c+1)
        tk.Button(top,text='←이전',command=priv).grid(row=2,column=0,sticky='w',padx=10)
        tk.Button(top,text='다시',command=del_all).grid(row=2,column=1)
        tk.Button(top,text='다음→',command=next).grid(row=2,column=2,sticky='e',padx=10)
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
                    var=msgbox.askyesno('채점 완료?','채점 완료?')
                    if var:
                        top.destroy()
                        self.__result()
            except ValueError:
                msgbox.showerror('Error','값 입력 오류')
        top=tk.Toplevel(main)
        top.resizable(False,False)
        top.title('선택형 오답 배점입력')
        mid=tk.Frame(top)
        tk.Label(mid,text='번호').grid(row=0,column=0)
        tk.Label(mid,text='배점').grid(row=0,column=1)
        err_num=list(self.__err1.keys())
        score_in=[]
        for k in range(len(self.__err1)):
            tk.Label(mid,text=err_num[k]).grid(row=k+1,column=0)
            score_in.append(tk.Entry(mid,width=7))
            score_in[k].grid(row=k+1,column=1)
        mid.grid(row=0,column=0,columnspan=2)
        if self.__err1:
            str_btn='다음→'
        else:
            str_btn='채점'
        tk.Button(top,text='←이전',command=priv).grid(row=1,column=0,sticky='w',padx=10)
        tk.Button(top,text=str_btn,command=next).grid(row=1,column=1,sticky='e',padx=10)
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
                var=msgbox.askyesno('채점 완료?','채점 완료?')
                if var:
                    top.destroy()
                    self.__result()
            except ValueError:
                msgbox.showerror('Error','값 입력 오류')
        top=tk.Toplevel(main)
        top.resizable(False,False)
        top.title('서답형 오답 배점입력')
        mid=tk.Frame(top)
        top_str=('번호','득점','배점')
        for k in range(3):
            tk.Label(mid,text=top_str[k]).grid(row=0,column=k)
        num=list(self.__err2.keys())
        score_in,score_in2=[],[]
        for k in range(len(self.__err2)):
            tk.Label(mid,text=num[k]).grid(row=k+1,column=0)
            score_in.append(tk.Entry(mid,width=7))
            score_in2.append(tk.Entry(mid,width=7))
            score_in[k].grid(row=k+1,column=1)
            score_in2[k].grid(row=k+1,column=2)
        mid.grid(row=0,column=0,columnspan=2)
        tk.Button(top,text='←이전',command=priv).grid(row=1,column=0,sticky='w',padx=10)
        tk.Button(top,text='채점',command=next).grid(row=1,column=1,sticky='e',padx=10)
    def __result(self):
        def write():
            global current_wrong,saved
            current_wrong[self.__subject.get()]=(self.__err1,self.__err2)
            saved=False
        def next():
            Grad_detail(self.__subject.get())
        def close():
            top.destroy()
        top=tk.Toplevel(main)
        top.resizable(False,False)
        top.title('결과')
        if self.__err1 or self.__err2:
            score=100
            for err1 in self.__err1:
                score=score-dec(self.__err1[err1][2])
            for err2 in self.__err2:
                score=score-dec(self.__err2[err2][1])+dec(self.__err2[err2][0])
            tk.Label(top,text='오답 수: %s\n점수: %s' %(str(len(self.__err1)+len(self.__err2)),str(score))).grid(row=0,column=0,columnspan=2)
        else:
            tk.Label(top,text='만점!\n점수: 100').grid(row=0,column=0,columnspan=2)
        tk.Button(top,text='상세',command=next).grid(row=1,column=0,sticky='w',padx=10)
        tk.Button(top,text='닫기',command=close).grid(row=1,column=1,sticky='e',padx=10)
        write()


class Grad_result(tk.Toplevel):
    def __init__(self):
        def btn_make(subject,n):
            tk.Button(f_mid,text='상세?',command=lambda: Grad_detail(subject)).grid(row=n,column=3)
        
        def del_res(all_subject=False):
            global current_wrong
            var=msgbox.askyesno('삭제?','복원 불가\n삭제?')
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
            super().__init__(main)
            score=get_score()
            self.resizable(False,False)
            self.title('가채점결과')
            self_str=('과목명','오답 수','점수','상세','삭제?')
            f_mid,f_bot=tk.Frame(self),tk.Frame(self)
            lab,chk=[],[]
            for k in range(5):
                tk.Label(f_mid,text=self_str[k]).grid(row=0,column=k)
            for k in range(current_subject_cnt):
                tmp_btn=None
                tk.Label(f_mid,text=current_subjects[k]).grid(row=k+1,column=0)
                lab.append([])
                if score[k]:
                    lab[k].append(tk.Label(f_mid,text=score[k][1]))
                    lab[k][0].grid(row=k+1,column=1)
                    lab[k].append(tk.Label(f_mid,text=score[k][0]))
                    lab[k][1].grid(row=k+1,column=2,padx=5)
                    if score[k][0]!='100':
                        btn_make(current_subjects[k],k+1)
                else:
                    tk.Label(f_mid,text='채점 전').grid(row=k+1,column=1,columnspan=2,padx=5)
                chk.append(tk.BooleanVar())
                tk.Checkbutton(f_mid,variable=chk[k]).grid(row=k+1,column=4)
            tk.Button(f_bot,text='삭제',command=del_res).pack(side='left')
            tk.Button(f_bot,text='초기화',command=lambda:del_res(True)).pack(side='left')
            tk.Button(self,text='닫기',command=self.destroy).grid(row=1,column=1,sticky='e')
            f_mid.grid(row=0,column=0,columnspan=2)
            f_bot.grid(row=1,column=0,sticky='w')
        else:
            msgbox.showerror(title='ERROR',message='가채점 안됨')


class Grad_detail(tk.Toplevel):
    def __init__(self,subject):
        if subject in current_subjects:
            super().__init__(main)
            self.resizable(False,False)
            wrong=current_wrong[subject]
            if wrong[0]:
                err_sel=tk.Frame(self,relief='solid',borderwidth=1,padx=5,pady=5)
                top1=('번호','응답','정답','배점')
                err_num=list(wrong[0].keys())
                tk.Label(err_sel,text='선\n택\n형\n오\n답').grid(row=0,column=0,rowspan=5)
                for k in range(4):
                    tk.Label(err_sel,text=top1[k]).grid(row=0,column=k+1)
                for k in range(len(wrong[0])):
                    tk.Label(err_sel,text=err_num[k]).grid(row=k+1,column=1)
                    for j in range(3):
                        tk.Label(err_sel,text=wrong[0][err_num[k]][j]).grid(row=k+1,column=j+2)
                err_sel.grid(row=0,column=0,padx=5,pady=5,sticky='w')
            if wrong[1]:
                err_comp=tk.Frame(self,relief='solid',borderwidth=1,padx=5,pady=5)
                top2=('번호','득점','배점')
                err_num=list(wrong[1].keys())
                tk.Label(err_comp,text='서\n답\n형\n오\n답').grid(row=0,column=0,rowspan=5)
                for k in range(3):
                    tk.Label(err_comp,text=top2[k]).grid(row=0,column=k+1)
                for k in range(len(wrong[1])):
                    tk.Label(err_comp,text=err_num[k]).grid(row=k+1,column=1)
                    for j in range(2):
                        tk.Label(err_comp,text=wrong[1][err_num[k]][j]).grid(row=k+1,column=j+2)
                err_comp.grid(row=1,column=0,padx=5,pady=5,sticky='w')
            tk.Button(self,text='닫기',command=self.destroy).grid(row=2,column=0,sticky='e')
        else:
            msgbox.showerror('Error','없는 과목')


#(예상)등급계산
class Grade_calc(tk.Toplevel):
    def __init__(self):
        if current_subject_cnt==0:
            msgbox.showerror('Error','과목 입력 안됨')
        else:
            super().__init__(main)
            self.resizable(False,False)
            self.title('예상등급계산')
            f_mid,f_bot=tk.Frame(self),tk.Frame(self)
            str_self=('과목명','시수','등급1','등급2')
            for a in range(4):
                tk.Label(f_mid,text=str_self[a]).grid(row=0,column=a)
            self.__grade1,self.__grade2=[],[]
            k=0
            for subject in current_subjects:
                tk.Label(f_mid,text=subject).grid(row=k+1,column=0)
                tk.Label(f_mid,text=current_num[subject][0]).grid(row=k+1,column=1)
                self.__grade1.append(tk.StringVar())
                self.__grade2.append(tk.StringVar())
                tk.Entry(f_mid,width=7,textvariable=self.__grade1[-1]).grid(row=k+1,column=2)
                tk.Entry(f_mid,width=7,textvariable=self.__grade2[-1]).grid(row=k+1,column=3)
                k+=1
            f_mid.grid(row=0,column=0,columnspan=2)
            tk.Button(self,text='극간계산',command=Cut_calc).grid(row=1,column=0,sticky='w')
            tk.Button(f_bot,text='초기화',command=self.__del_all).grid(row=0,column=0,sticky='e')
            tk.Button(f_bot,text='계산',command=self.__calc).grid(row=0,column=1,sticky='e')
            tk.Button(f_bot,text='닫기',command=self.destroy).grid(row=0,column=2,sticky='e')
            f_bot.grid(row=1,column=1,sticky='e')
            k+=1
    
    def __calc(self):
        try:
            nums=get_current_num()
            total_num=sum(nums)
            max_grade=0
            min_grade=0
            for k in range(current_subject_cnt):
                in1=self.__grade1[k].get()
                in2=self.__grade2[k].get()
                grd1=int(in1)
                if 0<grd1>9:
                    raise ValueError
                if in2:
                    grd2=int(in2)
                    max_grade+=min(grd1,grd2)*nums[k]
                    min_grade+=max(grd1,grd2)*nums[k]
                else:
                    max_grade+=grd1*nums[k]
                    min_grade+=grd1*nums[k]
        except ValueError:
            msgbox.showerror('Error','잘못된 입력')
        else:
            msgbox.showinfo(
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
    
    '''
    #not used, but remain for future
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
            msgbox.showerror('Error','개수 오류')
            return None,None
    '''


#성적 입력
class Exam_input(tk.Toplevel):
    def __init__(self):
        global current_result
        def btn_make(n):
            tk.Button(f_mid,text='X',command=lambda: del_subject(n)).grid(row=n+1,column=5,padx=3)
        def del_subject(n):
            for k in range(3):
                self.__ent[n][k].set('')
        def del_all():
            for k in range(current_subject_cnt):
                del_subject(k)
        if current_subjects:
            super().__init__(main)
            self.resizable(False,False)
            self.title('성적 입력')
            f_mid=tk.Frame(self)
            self_str=('과목명','시수','원점수','석차','인원수')
            self.__ent=[]
            for k in range(5):
                tk.Label(f_mid,text=self_str[k]).grid(row=0,column=k)
            k=0
            for subject in current_subjects:
                tk.Label(f_mid,text=subject).grid(row=k+1,column=0)
                tk.Label(f_mid,text=current_num[subject][0]).grid(row=k+1,column=1)
                self.__ent.append([])
                for j in range(3):
                    self.__ent[-1].append(tk.StringVar())
                    if subject in current_result.keys():
                        value=current_result[subject][j]
                        self.__ent[-1][j].set(value if value else '')
                    tk.Entry(f_mid,textvariable=self.__ent[-1][j],width=7).grid(row=k+1,column=j+2)
                btn_make(k)
                k+=1
            #bottom buttons
            f_bot=tk.Frame(self)
            tk.Button(self,text='초기화',command=del_all).grid(row=1,column=0,sticky='w')
            tk.Button(f_bot,text='취소',command=self.destroy).grid(row=0,column=0)
            tk.Button(f_bot,text='입력',command=self.__end).grid(row=0,column=1)
            #grid frames
            f_mid.grid(row=0,column=0,columnspan=2)
            f_bot.grid(row=1,column=1,sticky='e')
        else:
            msgbox.showerror('Error','과목 입력 안됨')
    
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
            msgbox.showerror('Error','입력 값 오류')
        else:
            if not all_entered:
                proceed_blank=msgbox.askyesno('Info','빈 칸 존재\n성적입력?')
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
                Exam_res()


#시혐 결과
class Exam_res(tk.Toplevel):
    def __init__(self):
        def get_grade(rank,person):
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
        def calc(num,grd):
            result=0
            n=0
            for k in range(len(num)):
                result+=num[k]*grd[k]
                n+=num[k]
            return round(result/n,4)
        if current_result:
            super().__init__(main)
            self.resizable(False,False)
            self.title('시험 결과')
            f_mid=tk.Frame(self)
            self_str=('과목','시수','점수','석차','등급','백분위')
            for k in range(6):
                tk.Label(f_mid,text=self_str[k]).grid(row=0,column=k,padx=5)
            grades=[]
            all_rank_inputed=True
            k=0
            for subject in current_subjects:
                tk.Label(f_mid,text=subject).grid(row=k+1,column=0)
                tk.Label(f_mid,text=current_num[subject][0]).grid(row=k+1,column=1)
                if subject in current_result.keys():
                    score,rank,total_person=current_result[subject]
                    tk.Label(f_mid,text=score).grid(row=k+1,column=2)
                    if rank and total_person:
                        grade,percent=get_grade(rank,total_person)
                        tk.Label(f_mid,text='%d/%d' %(rank,total_person)).grid(row=k+1,column=3) #str(rank)+'/'+str(total_person)
                        tk.Label(f_mid,text=grade).grid(row=k+1,column=4)
                        tk.Label(f_mid,text=round(percent,2)).grid(row=k+1,column=5)
                        grades.append(grade)
                    else:
                        tk.Label(f_mid,text='등급 입력 전').grid(row=k+1,column=3,columnspan=3)
                        all_rank_inputed=False
                else:
                    tk.Label(f_mid,text='성적 입력 전').grid(row=k+1,column=2,columnspan=4)
                    all_rank_inputed=False
                k+=1
            f_mid.grid(row=0,column=0)
            if all_rank_inputed:
                tk.Label(self,text='등급: '+str(calc(get_current_num(),grades))).grid(row=1,column=0)
            tk.Button(self,text='닫기',command=self.destroy).grid(row=2,column=0,sticky='e')
        elif current_subjects:
            msgbox.showerror('Error','성적 입력 안됨')
        else:
            msgbox.showerror('Error','과목 입력 안됨')


#등급인원계산
class Cut_calc(tk.Toplevel):
    def __init__(self):
        result=['','','','','','','','','']
        super().__init__(main)
        self.resizable(False,False)
        self.title('등급인원계산')
        f_self=tk.Frame(self)
        self.__f_mid=tk.Frame(self)
        f_bot=tk.Frame(self)
        tk.Label(f_self,text='인원').grid(row=0,column=0)
        self.__ent=tk.Entry(f_self)
        self.__ent.bind('<Return>',self.__get)
        self.__ent.grid(row=0,column=1)
        str_self=('등급','누적비율','누적인원수')
        for k in range(3):
            tk.Label(self.__f_mid,text=str_self[k]).grid(row=0,column=k)
        for k in range(9):
            tk.Label(self.__f_mid,text=str(k+1)+'등급').grid(row=k+1,column=0)
            tk.Label(self.__f_mid,text=str(CUTS[k])+'%').grid(row=k+1,column=1)
            tk.Label(self.__f_mid,text='').grid(row=k+1,column=2)
        tk.Button(f_bot,text='닫기',command=self.destroy).grid(row=0,column=0)
        tk.Button(f_bot,text='계산',command=self.__get).grid(row=0,column=1)
        f_self.grid(row=0,column=0)
        self.__f_mid.grid(row=1,column=0)
        f_bot.grid(row=2,column=0)
    
    
    def __get(self):
        try:
            a=int(self.__ent.get())
        except ValueError:
            msgbox.showerror('Error','인원수 오류')
        else:
            result=[]
            for k in CUTS:
                result.append(round(a*k/100))
            for k in range(9):
                tk.Label(self.__f_mid,text=str(result[k])+'명').grid(row=k+1,column=2)


#안내 Root Class
class Notice(tk.Toplevel):
    def __init__(self,name,fileName,string):
        try:
            with open(fileName+'.txt','r') as file:
                txt=file.readlines()
        except:
            txt=string
        super().__init__(main)
        self.resizable(False,False)
        self.title(name)
        tk.Label(self,text=txt).pack()
        tk.Button(self,text='닫기',command=self.destroy).pack()
    def form(self,string):
        text=''
        for line in string.splitlines():
            if line:
                text+=line+'\n'
        return text[:-1]


#도움말
class Help(Notice):
    def __init__(self):
        text='''

'''
        txt=super().form(text)
        super().__init__('도움말','help',txt)


#라이선스
class License(Notice):
    def __init__(self):
        text='''

'''
        txt=super().form(text)
        super().__init__('License','license',txt)


#정보
class Info(Notice):
    def __init__(self):
        text='''
성적계산기
made by HYS
'''
        txt=super().form(text)
        super().__init__('프로그램 정보','info',txt)


if __name__=='__main__':
    import ctypes
    myappid = 'hys.grademanage'
    Main()