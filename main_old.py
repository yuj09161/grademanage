import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as msgbox
from tkinter.ttk import Progressbar

from tkinter.filedialog import askopenfilename as askopen
from tkinter.filedialog import asksaveasfilename as asksave

import copy,pickle,json,decimal

#초기화
win=tk.Tk()
win.resizable(False,False)
win.title('성적계산기')
#전역 변수 생성
current_exam='311'; file_name=''
result_semester,result_exam={},{}
for a in range(1,4):
    for b in range(1,3):
        result_semester[str(10*a+b)]=[{},{}]
        for c in range(1,3):
            result_exam[str(100*a+10*b+c)]=[{},{}]
current_num={}
current_wrong={}
current_result={}

'''전역함수(콜백 제외)'''

#점수 계산
def get_score(subject=None):
    def calc(subject):
        if subject in current_wrong.keys(): #과목 존재?
            wrong=current_wrong[subject]
            score,num=decimal.Decimal(100),0
            #객관식 오답 계산
            wrong_sel=tuple(wrong[0].values())
            if wrong_sel:
                num+=len(wrong_sel)
                for j in range(len(wrong_sel)):
                    score-=decimal.Decimal(str(wrong_sel[j][2]))
            #서술형 오답 계산
            wrong_exp=tuple(wrong[1].values())
            if wrong_exp:
                num+=len(wrong_exp)
                for j in range(len(wrong_exp)):
                    score-=decimal.Decimal(str(wrong_exp[j][1]))-decimal.Decimal(str(wrong_exp[j][0]))
            return score,num
        else:
            return None
    if subject:
        return calc(subject)
    else:
        global current_num
        subjects=tuple(current_num.keys())
        length=len(subjects)
        result=[]
        for k in range(length):
            result.append(calc(subjects[k]))
        return result


#버튼 상태 업데이트
def update_btn():
    global current_num,current_wrong,current_result
    changeBtn['fg']='black'
    if current_num:
        if current_exam[2]=='3':
            btn[0][1]['state']='disable'
            btn[0][2]['state']='disable'
        else:
            btn[0][1]['state']='active'
            if current_wrong:
                btn[0][2]['state']='active'
            else:
                btn[0][2]['state']='disable'
        btn[1][0]['state']='active'
        btn[1][1]['state']='active'
        if current_result:
            btn[1][2]['state']='active'
        else:
            btn[1][2]['state']='disable'
    else:
        btn[0][1]['state']='disable'
        btn[0][2]['state']='disable'
        btn[1][0]['state']='disable'
        btn[1][1]['state']='disable'
        btn[1][2]['state']='disable'

'''창 클래스들'''
#진행 바(연속형)
class progbar():
    def __init__(self,title,txt,leng=200,time=5):
        self.__top=tk.Toplevel(win)
        self.__top.title(title)
        tk.Label(self.__top,text=txt).pack()
        prog=Progressbar(self.__top,mode='indeterminate',length=leng)
        prog.pack()
        prog.start(interval=time)
    def __del__(self):
        self.__top.destroy()


#과목 입력
class input_subject():
    def __init__(self):
        global current_num
        #초기화
        self.__inbox,self.__invar=[],[]
        self.__top=tk.Toplevel(win)
        self.__top.resizable(False,False)
        self.__top.title('과목 입력')
        self.__mid,self.__footer=tk.Frame(self.__top),tk.Frame(self.__top)
        #버튼 생성
        tk.Button(self.__top,text='+추가',command=self.__add_subject).grid(row=1,column=0,sticky='w',padx=5)
        tk.Button(self.__footer,text='취소',command=self.__top.destroy).grid(row=0,column=0,sticky='e')
        tk.Button(self.__footer,text='입력',command=self.__set_subject).grid(row=0,column=1,sticky='e')
        #메뉴 생성/배치
        menu_str=('과목명','시수','삭제')
        for k in range(3):
            tk.Label(self.__mid,text=menu_str[k]).grid(row=0,column=k)
        #메뉴,버튼 그룹 배치
        self.__mid.grid(row=0,column=0,columnspan=2)
        self.__footer.grid(row=1,column=1,rowspan=1,columnspan=1,sticky='e',padx=5)
        #기존 값 불러오기
        if current_num:
            subject=list(current_num.keys())
            for k in range(len(current_num)):
                self.__add_subject(subject[k],current_num[subject[k]])
    def __add_subject(self,subject=None,num=None):
        n=len(self.__inbox)
        if subject:
            self.__invar.append((tk.StringVar(value=subject),tk.StringVar(value=num)))
        else:
            self.__invar.append((tk.StringVar(),tk.StringVar()))
        self.__inbox.append(
            (
                tk.Entry(self.__mid,width=15,textvariable=self.__invar[n][0]),
                tk.Entry(self.__mid,width=5,textvariable=self.__invar[n][1]),
                tk.Button(self.__mid,text='X',command=lambda:self.__del_subject(n))
            )
        )
        for a in range(len(self.__inbox)):
            if self.__inbox[a]:
                for b in range(3):
                    self.__inbox[a][b].grid(row=a+1,column=b)
    def __del_subject(self,n):
        for a in range(3):
            self.__inbox[n][a].grid_forget()
        self.__inbox[n]=None
    def __set_subject(self):
        global current_num
        current_num={}
        try:
            for k in range(len(self.__inbox)):
                if self.__inbox[k]:
                    current_num[self.__invar[k][0].get()]=int(self.__invar[k][1].get())
        except ValueError:
            msgbox.showerror(title='ERROR',message='잘못된 값 입력')
        else:
            self.__top.destroy()
            update_btn()


#가채점 입력
class grade_ing():
    def __init__(self):
        self.__err1,self.__err2={},{}
        self.__subject=tk.StringVar()
        self.__select()
    def __select(self):
        global current_num
        def next():
            top.destroy(); self.__grading()
        try:
            self.__subject.set(list(current_num.keys())[0])
        except IndexError:
            msgbox.showerror(title='ERROR',message='과목 입력 안됨')
        else:
            top=tk.Toplevel(win)
            top.resizable(False,False)
            top.title('과목 선택')
            frame_top=tk.Frame(top);frame_bottom=tk.Frame(top)
            drop=tk.OptionMenu(frame_top,self.__subject,*list(current_num.keys()))
            label=tk.Label(frame_top,text='과목: ')
            btn0=tk.Button(frame_bottom,text='취소',command=top.destroy)
            btn1=tk.Button(frame_bottom,text='다음→',command=next)
            label.grid(row=0,column=0); drop.grid(row=0,column=1)
            btn0.grid(row=0,column=0); btn1.grid(row=0,column=1)
            frame_top.grid(row=0,column=0)
            frame_bottom.grid(row=1,column=0)
    def __grading(self):
        subject=self.__subject.get() #과목 설정
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
                            a,b=list(a),list(b)
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
                    ans,cor=tuple(ans),tuple(cor)
                    return (ans,cor)
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
                        self.__err1[k+1]=[x[0][k],x[1][k]]
                    elif x[0][k]==7:
                        self.__err2[k+1]=[]
                n,m=len(self.__err1),len(self.__err2)
                var=msgbox.askyesno("오답 확인",
                    "<오답 개수>\n선택형: %s\n서답형: %s\n채점 진행?"
                    %(n,m)
                )
                if var:
                    if self.__err1:
                        top.destroy()
                        self.__err_sel()
                    elif self.__err2:
                        top.destroy()
                        self.__err_comp()
                    else:
                        var=msgbox.askyesno('채점 완료?','채점 완료?')
                        if var:
                            self.__result()
        #메인
        top=tk.Toplevel(win)
        top.resizable(False,False)
        top.title('가채점')
        f_mid=tk.Frame(top)
        inputs=[]
        str_left=('범\n례','응\n답','정\n답')
        str_top=('1~5','6~10','11~15','16~20','21~25','26~30')
        tk.Label(top,text='과목: '+subject).grid(row=0,column=0,columnspan=3)
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
                    self.__err1[num[k]]=tuple(self.__err1[num[k]]+[decimal.Decimal(score_in[k].get())])
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
        top=tk.Toplevel(win)
        top.resizable(False,False)
        top.title('선택형 오답 배점입력')
        mid=tk.Frame(top)
        tk.Label(mid,text='번호').grid(row=0,column=0)
        tk.Label(mid,text='배점').grid(row=0,column=1)
        num=list(self.__err1.keys())
        score_in=[]
        for k in range(len(self.__err1)):
            tk.Label(mid,text=num[k]).grid(row=k+1,column=0)
            score_in.append(tk.Entry(mid,width=7)); score_in[k].grid(row=k+1,column=1)
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
                    self.__err2[num[k]]=(decimal.Decimal(score_in[k].get()),decimal.Decimal(score_in2[k].get()))
                var=msgbox.askyesno('채점 완료?','채점 완료?')
                if var:
                    top.destroy()
                    self.__result()
            except ValueError:
                msgbox.showerror('Error','값 입력 오류')
        top=tk.Toplevel(win)
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
            score_in.append(tk.Entry(mid,width=7)); score_in[k].grid(row=k+1,column=1)
            score_in2.append(tk.Entry(mid,width=7)); score_in2[k].grid(row=k+1,column=2)
        mid.grid(row=0,column=0,columnspan=2)
        tk.Button(top,text='←이전',command=priv).grid(row=1,column=0,sticky='w',padx=10)
        tk.Button(top,text='채점',command=next).grid(row=1,column=1,sticky='e',padx=10)
    def __result(self):
        subject=self.__subject.get()
        def write():
            global current_wrong
            current_wrong[subject]=(self.__err1,self.__err2)
        def next():
            write()
            grad_res(subject)
        def close():
            write()
            top.destroy()
        top=tk.Toplevel(win)
        top.resizable(False,False)
        top.title('결과')
        score=100
        key_num=list(self.__err1.keys())
        for k in range(len(self.__err1)):
            score=score-self.__err1[key_num[k]][2]
        key_num=list(self.__err2.keys())
        for k in range(len(self.__err2)):
            score=score-self.__err2[key_num[k]][1]+self.__err2[key_num[k]][0]
        if self.__err2 or self.__err1:
            tk.Label(top,text='오답 수: %s\n점수: %s' %(str(len(self.__err1)+len(self.__err2)),score)).grid(row=0,column=0,columnspan=2)
        else:
            tk.Label(top,text='만점!\n점수: 100').grid(row=0,column=0,columnspan=2)
        tk.Button(top,text='상세',command=next).grid(row=1,column=0,sticky='w',padx=10)
        tk.Button(top,text='닫기',command=close).grid(row=1,column=1,sticky='e',padx=10)


#가채점결과
class grad_res():
    def __init__(self,subject=None):
        global current_num,current_wrong
        if current_wrong:
            if subject:
                if subject in current_num.keys():
                    self.__detail(subject)
                else:
                    msgbox.showerror('Error','없는 과목')
            else:
                self.__main()
        else:
            msgbox.showerror(title='ERROR',message='가채점 안됨')
    def __main(self):
        subjects=list(current_num.keys())
        score=get_score()
        def btn_make(subject,n):
            tk.Button(f_mid,text='상세?',command=lambda:
            self.__detail(subject)).grid(row=n,column=3)
        def del_res(mode=False):
            global current_wrong
            var=msgbox.askyesno('삭제?','복원 불가\n삭제?')
            if var:
                if mode:
                    for k in range(len(subjects)):
                        if subjects[k] in current_wrong.keys():
                            del current_wrong[subjects[k]]
                else:
                    for k in range(len(subjects)):
                        if chk[k].get() and (subjects[k] in current_wrong.keys()):
                            del current_wrong[subjects[k]]
                top.destroy()
                if current_wrong:
                    grad_res()
        top=tk.Toplevel(win)
        top.resizable(False,False)
        top.title('가채점결과')
        top_str=('과목명','오답 수','점수','상세','삭제?')
        f_mid,f_bot=tk.Frame(top),tk.Frame(top)
        lab,chk=[],[]
        for k in range(5):
            tk.Label(f_mid,text=top_str[k]).grid(row=0,column=k)
        for k in range(len(subjects)):
            tmp_btn=None
            tk.Label(f_mid,text=subjects[k]).grid(row=k+1,column=0)
            lab.append([])
            if score[k]:
                lab[k].append(tk.Label(f_mid,text=str(score[k][1])))
                lab[k][0].grid(row=k+1,column=1)
                lab[k].append(tk.Label(f_mid,text=str(score[k][0])))
                lab[k][1].grid(row=k+1,column=2,padx=5)
                if score[k][0]!=100:
                    btn_make(subjects[k],k+1)
            else:
                tk.Label(f_mid,text='채점 전').grid(row=k+1,column=1,columnspan=2,padx=5)
            chk.append(tk.BooleanVar())
            tk.Checkbutton(f_mid,variable=chk[k]).grid(row=k+1,column=4)
        tk.Button(f_bot,text='삭제',command=del_res).pack(side='left')
        tk.Button(f_bot,text='초기화',command=lambda:del_res(True)).pack(side='left')
        tk.Button(top,text='닫기',command=top.destroy).grid(row=1,column=1,sticky='e')
        f_mid.grid(row=0,column=0,columnspan=2)
        f_bot.grid(row=1,column=0,sticky='w')
    def __detail(self,subject):
        global current_wrong
        wrong=current_wrong[subject]
        top=tk.Toplevel(win)
        top.resizable(False,False)
        if wrong[0]:
            err_sel=tk.Frame(top,relief='solid',borderwidth=1,padx=5,pady=5)
            top_sel=('번호','응답','정답','배점')
            err_num=list(wrong[0].keys())
            tk.Label(err_sel,text='선\n택\n형\n오\n답').grid(row=0,column=0,rowspan=5)
            for k in range(4):
                tk.Label(err_sel,text=top_sel[k]).grid(row=0,column=k+1)
            for k in range(len(wrong[0])):
                tk.Label(err_sel,text=err_num[k]).grid(row=k+1,column=1)
                for j in range(3):
                    tk.Label(err_sel,text=wrong[0][err_num[k]][j]).grid(row=k+1,column=j+2)
            err_sel.grid(row=0,column=0,padx=5,pady=5,sticky='w')
        if wrong[1]:
            err_comp=tk.Frame(top,relief='solid',borderwidth=1,padx=5,pady=5)
            top_sel=('번호','득점','배점')
            err_num=list(wrong[1].keys())
            tk.Label(err_comp,text='서\n답\n형\n오\n답').grid(row=0,column=0,rowspan=5)
            for k in range(3):
                tk.Label(err_comp,text=top_sel[k]).grid(row=0,column=k+1)
            for k in range(len(wrong[1])):
                tk.Label(err_comp,text=err_num[k]).grid(row=k+1,column=1)
                for j in range(2):
                    tk.Label(err_comp,text=wrong[1][err_num[k]][j]).grid(row=k+1,column=j+2)
            err_comp.grid(row=1,column=0,padx=5,pady=5,sticky='w')
        tk.Button(top,text='닫기',command=top.destroy).grid(row=2,column=0,sticky='e')
#(예상)등급계산
class grade_calc():
    def __init__(self):
        global current_num
        subjects=list(current_num.keys())
        def get():
            grd1,grd2=[],[]
            try:
                for k in range(len(current_num)):
                    grd1.append(int(grade1[k].get()))
                    tmp=grade2[k].get()
                    if tmp:
                        grd2.append(int(tmp))
                    else:
                        grd2.append(None)
                max,min=self.__calc(subjects,list(current_num.values()),grd1,grd2)
                msgbox.showinfo('결과','최고: %s\n최저: %s' %(max,min))
            except ValueError:
                msgbox.showerror('Error','잘못된 값 입력')
        def del_all():
            for k in range(len(current_num)):
                grade1[k].set('')
                grade2[k].set('')
        if len(current_num)==0:
            msgbox.showerror('Error','과목 입력 안됨')
        else:
            top=tk.Toplevel(win)
            top.resizable(False,False)
            top.title('예상등급계산')
            f_mid,f_bot=tk.Frame(top),tk.Frame(top)
            str_top=('과목명','시수','등급1','등급2')
            for a in range(4):
                tk.Label(f_mid,text=str_top[a]).grid(row=0,column=a)
            nums=list(current_num.values())
            grade1,grade2=[],[]
            for k in range(len(current_num)):
                tk.Label(f_mid,text=subjects[k]).grid(row=k+1,column=0)
                tk.Label(f_mid,text=nums[k]).grid(row=k+1,column=1)
                grade1.append(tk.StringVar())
                grade2.append(tk.StringVar())
                tk.Entry(f_mid,width=7,textvariable=grade1[k]).grid(row=k+1,column=2)
                tk.Entry(f_mid,width=7,textvariable=grade2[k]).grid(row=k+1,column=3)
            f_mid.grid(row=0,column=0,columnspan=2)
            tk.Button(top,text='극간계산',command=cut_calc).grid(row=1,column=0,sticky='w')
            tk.Button(f_bot,text='초기화',command=del_all).grid(row=0,column=0,sticky='e')
            tk.Button(f_bot,text='계산',command=get).grid(row=0,column=1,sticky='e')
            tk.Button(f_bot,text='닫기',command=top.destroy).grid(row=0,column=2,sticky='e')
            f_bot.grid(row=1,column=1,sticky='e')
    def __calc(self,subjects,nums,grd1,grd2):
        #파싱
        if len(subjects)==len(nums)==len(grd1):
            length=len(subjects)
            res,tmp=[],[]
            res.append([grd1[0]])
            if grd2[0]:
                res.append([grd2[0]])
            for k in range(1,length):
                if not grd1[k]:
                    break
                tmp=copy.deepcopy(res)
                for j in range(len(res)):
                    res[j].append(grd1[k])
                if grd2[k]:
                    for j in range(len(tmp)):
                        tmp[j].append(grd2[k])
                    res+=tmp
            #등급 계산
            tmp=[]
            for a in res:
                x=0
                for j in range(length):
                    x+=a[j]*nums[j]
                tmp.append(round(x/sum(nums),4))
            return max(tmp),min(tmp)
        else:
            msgbox.showerror('Error','개수 오류')
            return None,None
#성적 입력
class exam_input():
    def __init__(self):
        global current_num,current_result
        def btn_make(n):
            tk.Button(f_mid,text='X',command=lambda:
            del_subject(n)).grid(row=n+1,column=5,padx=3)
        def del_subject(n):
            for k in range(3):
                ent[n][k].set('')
        def del_all():
            for k in range(length):
                del_subject(k)
        def exit():
            var_b,var_p,res=False,False,[]
            try:
                for k in range(length):
                    a,b,c=ent[k][0].get(),ent[k][1].get(),ent[k][2].get()
                    if a:
                        a=decimal.Decimal(a)
                    else:
                        a,var_b=None,True
                    if b:
                        b=int(b)
                    else:
                        b,var_b=None,True
                    if c:
                        c=int(c)
                    else:
                        c,var_b=None,True
                    res.append((a,b,c))
            except ValueError:
                msgbox.showerror('Error','입력 값 오류')
            else:
                if var_b:
                    tmp=msgbox.askyesno('Info','빈 칸 존재\n성적입력?')
                if (not var_b) or tmp:
                    for k in range(length):
                        if res[k][0] and res[k][1] and res[k][2]:
                            current_result[subjects[k]]=res[k]
                    top.destroy()
                    exam_res()
        if current_num:
            top=tk.Toplevel(win)
            top.resizable(False,False)
            top.title('성적 입력')
            f_mid,f_bot1,f_bot2=tk.Frame(top),tk.Frame(top),tk.Frame(top)
            subjects,nums=tuple(current_num.keys()),tuple(current_num.values())
            length=len(subjects)
            top_str=('과목명','시수','원점수','석차','인원수')
            btn,ent=[],[]
            for k in range(5):
                tk.Label(f_mid,text=top_str[k]).grid(row=0,column=k)
            for k in range(length):
                tk.Label(f_mid,text=subjects[k]).grid(row=k+1,column=0)
                tk.Label(f_mid,text=nums[k]).grid(row=k+1,column=1)
                ent.append([])
                if subjects[k] in current_result.keys():
                    tmp=current_result[subjects[k]]
                else:
                    tmp=None
                for j in range(3):
                    ent[k].append(tk.StringVar())
                    if tmp:
                        ent[k][j].set(tmp[j])
                    tk.Entry(f_mid,textvariable=ent[k][j],width=7).grid(row=k+1,column=j+2)
                btn_make(k)
            tk.Button(top,text='초기화',command=del_all).grid(row=1,column=0,sticky='w')
            tk.Button(f_bot2,text='취소',command=top.destroy).grid(row=0,column=0)
            tk.Button(f_bot2,text='입력',command=exit).grid(row=0,column=1)
            f_mid.grid(row=0,column=0,columnspan=2)
            f_bot2.grid(row=1,column=1,sticky='e')
        else:
            msgbox.showerror('Error','과목 입력 안됨')
#시혐 결과
class exam_res():
    def __init__(self):
        global current_result
        def grade(rank,person):
            percent=rank/person*100
            cuts=(4,11,23,40,60,77,89,96,100)
            grade=1
            for k in range(9):
                if percent<=cuts[k]:
                    grade=k+1
                    break
            return grade,percent
        def calc(subjects,num,grd):
            result=0
            n=0
            for k in range(len(subjects)):
                result+=num[k]*grd[k]
                n+=num[k]
            return round(result/n,4)
        if current_result:
            top=tk.Toplevel(win)
            top.resizable(False,False)
            top.title('시험 결과')
            f_mid=tk.Frame(top)
            global current_num
            top_str=('과목','시수','점수','석차','등급','백분위')
            for k in range(6):
                tk.Label(f_mid,text=top_str[k]).grid(row=0,column=k,padx=5)
            subjects=tuple(current_num.keys())
            grades,var=[],True
            for k in range(len(current_num)):
                tk.Label(f_mid,text=subjects[k]).grid(row=k+1,column=0)
                tk.Label(f_mid,text=current_num[subjects[k]]).grid(row=k+1,column=1)
                if subjects[k] in current_result.keys():
                    tmp=current_result[subjects[k]]
                    res=grade(tmp[1],tmp[2])
                    tk.Label(f_mid,text=tmp[0]).grid(row=k+1,column=2)
                    tk.Label(f_mid,text=str(tmp[1])+'/'+str(tmp[2])).grid(row=k+1,column=3)
                    tk.Label(f_mid,text=res[0]).grid(row=k+1,column=4)
                    tk.Label(f_mid,text=round(res[1],2)).grid(row=k+1,column=5)
                    grades.append(res[0])
                else:
                    tk.Label(f_mid,text='성적 입력 전').grid(row=k+1,column=2,columnspan=4)
                    var=False
            f_mid.grid(row=0,column=0)
            if var:
                tk.Label(top,text='등급: '+str(calc(subjects,tuple(current_num.values()),grades))).grid(row=1,column=0)
            tk.Button(top,text='닫기',command=top.destroy).grid(row=2,column=0,sticky='e')
        elif current_num:
            msgbox.showerror('Error','성적 입력 안됨')
        else:
            msgbox.showerror('Error','과목 입력 안됨')
#성적 추이
class change():
    def __init__(self):
        global current_result
        if current_result:
            top=tk.Toplevel(win)
            top.resizable(False,False)
            top.title('성적 추이')
        elif current_num:
            msgbox.showerror('Error','성적 입력 안됨')
        else:
            msgbox.showerror('Error','과목 입력 안됨')
#등급인원계산
class cut_calc():
    def __init__(self):
        result=['','','','','','','','','']
        cuts=(4,11,23,40,60,77,89,96,100)
        def get(*args):
            try:
                a=int(ent.get())
            except ValueError:
                msgbox.showerror('Error','인원수 오류')
            else:
                result=[]
                for k in cuts:
                    result.append(round(a*k/100))
                for k in range(9):
                    tk.Label(f_mid,text=str(result[k])+'명').grid(row=k+1,column=2)
        top=tk.Toplevel(win)
        top.resizable(False,False)
        top.title('등급인원계산')
        f_top,f_mid,f_bot=tk.Frame(top),tk.Frame(top),tk.Frame(top)
        tk.Label(f_top,text='인원').grid(row=0,column=0)
        ent=tk.Entry(f_top)
        ent.bind('<Return>',get)
        ent.grid(row=0,column=1)
        str_top=('등급','누적비율','누적인원수')
        for k in range(3):
            tk.Label(f_mid,text=str_top[k]).grid(row=0,column=k)
        for k in range(9):
            tk.Label(f_mid,text=str(k+1)+'등급').grid(row=k+1,column=0)
            tk.Label(f_mid,text=str(cuts[k])+'%').grid(row=k+1,column=1)
            tk.Label(f_mid,text='').grid(row=k+1,column=2)
        tk.Button(f_bot,text='닫기',command=top.destroy).grid(row=0,column=0)
        tk.Button(f_bot,text='계산',command=get).grid(row=0,column=1)
        f_top.grid(row=0,column=0)
        f_mid.grid(row=1,column=0)
        f_bot.grid(row=2,column=0)
#안내 Root Class
class notice():
    def __init__(self,name,fileName,string):
        try:
            with open(fileName+'.txt','r') as file:
                txt=file.readlines()
        except:
            txt=string
        self.__top=tk.Toplevel(win)
        self.__top.resizable(False,False)
        self.__top.title(name)
        tk.Label(self.__top,text=txt).pack()
        tk.Button(self.__top,text='닫기',command=self.__top.destroy).pack()
    def form(self,string):
        text=''
        for line in string.splitlines():
            if line:
                text+=line+'\n'
        return text[:-1]

#도움말
class help(notice):
    def __init__(self):
        text='''

'''
        txt=super().form(text)
        super().__init__('도움말','help',txt)
#라이선스
class license(notice):
    def __init__(self):
        text='''

'''
        txt=super().form(text)
        super().__init__('License','license',txt)
#정보
class info(notice):
    def __init__(self):
        text='''
성적계산기
made by HYS
'''
        txt=super().form(text)
        super().__init__('프로그램 정보','info',txt)

'''콜백 함수'''
#읽기
def load(name=None):
    global result_semester,result_exam
    if not name:
        name=askopen()
    if name:
        prog=progbar('Load','Loading...')
        try:
            #result_semester,result_exam=pickle.load(open(name,'rb'))
            with open(name,'r',encoding='utf-8') as file:
                result_semester,result_exam=json.load(file)
        except IOError:
            tmp=msgbox.askretrycancel('Error','읽기 에러')
            if tmp:
                load(name)
        #except pickle.UnpicklingError:
        except json.JSONDecodeError:
            msgbox.showerror('Error','파일 형식 오류')
        else:
            try:
                global current_num,current_wrong,current_result
                if current_exam[2]=='3': #학기말
                    current_num,current_result=result_semester[current_exam[:2]]
                else: #중간고사or기말고사
                    current_num=result_semester[current_exam[:2]][0]
                    current_wrong,current_result=result_exam[current_exam]
                update_btn()
            except ValueError:
                msgbox.showerror('Error','파일 형식 오류')
        finally:
            del(prog)
    else:
        tmp=msgbox.askretrycancel('Error','파일 지정 오류')
        if tmp:
            load()
#쓰기
def save(name=None):
    global result_semester,result_exam,file_name
    print(name)
    if not name:
        name=asksave()
    if name:
        prog=progbar('Save','Saving...')
        global current_num,current_wrong,current_result
        if current_exam[2]=='3': #학기말
            result_semester[current_exam[:2]]=[current_num,current_result]
        else: #중간고사or기말고사
            result_semester[current_exam[:2]][0]=current_num
            result_exam[current_exam]=[current_wrong,current_result]
        try:
            #pickle.dump((result_semester,result_exam),open(name,'wb'))
            with open(name,'w',encoding='utf-8') as file:
                json.dump((result_semester,result_exam),file,indent=4,ensure_ascii=False)
        except IOError:
            sel=msgbox.askretrycancel('Error','쓰기 에러')
            if sel: 
               save(name)
        finally:
            del(prog)
            file_name=name
    else:
        tmp=msgbox.askretrycancel('Error','파일 지정 오류')
        if tmp:
            load()
#시험 설정
def set_exam():
    global current_num,current_wrong,current_result
    global current_exam,result_semester,result_exam
    def saving(): #시험 결과 저장
        global current_num,current_wrong,current_result
        global current_exam,result_semester,result_exam
        if current_exam[2]=='3':
            result_semester[current_exam[:2]]=[current_num,current_result]
        else:
            result_semester[current_exam[:2]][0]=current_num
            result_exam[current_exam]=[current_wrong,current_result]
    semester=''
    for a in range(3): #과목 불러오기
        semester+=str(option[a].index(exam[a].get())+1)
    if semester[2]=='3': #학기말
        #시험 결과 저장/불러오기
        saving()
        current_exam=semester
        current_num,current_result=result_semester[current_exam[:2]]
        #버튼 상태 설정
        update_btn()
    else: #중간고사or기말고사
        #시험 결과 저장/불러오기
        saving()
        current_exam=semester
        current_num=result_semester[current_exam[:2]][0]
        current_wrong,current_result=result_exam[current_exam]
        #버튼 상태 설정
        update_btn()
        
def on_close():
    res=msgbox.askyesnocancel('저장','저장?')
    if res==True:
        save(file_name)
        win.destroy()
    elif res==False:
        win.destroy()
    else:
        return

def save_last():
    global file_name
    save(file_name)

'''중앙 버튼'''
#메뉴 생성
menu_bar=tk.Menu(win)
menu_file=tk.Menu(menu_bar,tearoff=0)
menu_tool=tk.Menu(menu_bar,tearoff=0)
menu_info=tk.Menu(menu_bar,tearoff=0)
#파일
menu_file.add_command(label='불러오기',command=load)
menu_file.add_command(label='저장',command=save_last)
#menu_file.add_command(label='다른 이름으로 저장',command=save)
menu_file.add_separator()
menu_file.add_command(label='종료',command=win.quit)
#도구
menu_tool.add_command(label='등급인원계산',command=cut_calc)
#정보
menu_info.add_command(label='도움말',command=help)
menu_info.add_command(label='License',command=license)
menu_info.add_separator()
menu_info.add_command(label='정보',command=info)
#메뉴 등록
menu_bar.add_cascade(label='파일',menu=menu_file)
menu_bar.add_cascade(label='도구',menu=menu_tool)
menu_bar.add_cascade(label='정보',menu=menu_info)

'''고사 설정 바'''
frame_top=tk.Frame(win)
option,exam=(('1학년','2학년','3학년'),('1학기','2학기'),('중간고사','기말고사','학기말')),[]
for a in range(3):
    exam.append(tk.StringVar())
    exam[a].set(option[a][0])
    ttk.Combobox(frame_top,textvariable=exam[a],values=option[a],width=7).grid(row=0,column=a)
    #tk.OptionMenu(frame_top,exam[a],*option[a]).grid(row=0,column=a)
    exam[a].trace('w',lambda *args:changeBtn.config(fg='red'))
changeBtn=tk.Button(frame_top,text='변경',command=set_exam)
changeBtn.grid(row=0,column=3)

frame_top.grid(row=0,column=0,columnspan=2)

'''메인 버튼'''
#버튼 생성
btn=[[],[]]
frame1=tk.Frame(win,relief='solid',borderwidth=1,padx=10,pady=10)
frame2=tk.Frame(win,relief='solid',borderwidth=1,padx=10,pady=10)
btn[0].append(tk.Button(frame1,text='과목입력',command=input_subject))
btn[0][0].grid(row=0,column=0,sticky='NSEW')
btn[0].append(tk.Button(frame1,text='가채점 입력',command=grade_ing))
btn[0][1].grid(row=1,column=0,sticky='NSEW')
btn[0].append(tk.Button(frame1,text='가채점 결과\n삭제/초기화',command=grad_res))
btn[0][2].grid(row=2,column=0,sticky='NSEW')
btn[1].append(tk.Button(frame2,text='등급계산',command=grade_calc))
btn[1][0].grid(row=0,column=0,sticky='NSEW')
btn[1].append(tk.Button(frame2,text='성적입력',command=exam_input))
btn[1][1].grid(row=1,column=0,sticky='NSEW')
btn[1].append(tk.Button(frame2,text='시험결과',command=exam_res))
btn[1][2].grid(row=2,column=0,sticky='NSEW')
btn[1].append(tk.Button(frame2,text='성적분석',state='disable'))
btn[1][3].grid(row=3,column=0,sticky='NSEW')
frame1.grid(row=1,column=0,padx=10,pady=10)
frame2.grid(row=1,column=1,padx=10,pady=10)

update_btn()

#종료 시 저장 확인
win.protocol("WM_DELETE_WINDOW",on_close)
#시작 시 데이터 로드
load('save.json')

#창 배치
win.config(menu=menu_bar)

win.mainloop()#메인루프