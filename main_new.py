



import copy,pickle,json,decimal

CUTS=(4,11,23,40,60,77,89,96,100)

#초기화

win.resizable(False,False)
win.title('성적계산기')
#전역 변수 생성
current_exam='111'; file_name=''
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
            score,err_cnt=decimal.Decimal(100),0
            #객관식 오답 계산
            wrong_sel=tuple(wrong[0].values())
            if wrong_sel:
                err_cnt+=len(wrong_sel)
                for j in range(len(wrong_sel)):
                    score-=decimal.Decimal(str(wrong_sel[j][2]))
            #서술형 오답 계산
            wrong_exp=tuple(wrong[1].values())
            if wrong_exp:
                err_cnt+=len(wrong_exp)
                for j in range(len(wrong_exp)):
                    score-=decimal.Decimal(str(wrong_exp[j][1]))-decimal.Decimal(str(wrong_exp[j][0]))
            return str(score),str(err_cnt)
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
            btn[0][1].setEnabled(False)
            btn[0][2].setEnabled(False)
        else:
            btn[0][1].setEnabled(True)
            if current_wrong:
                btn[0][2].setEnabled(True)
            else:
                btn[0][2].setEnabled(False)
        btn[1][0].setEnabled(True)
        btn[1][1].setEnabled(True)
        if current_result:
            btn[1][2].setEnabled(True)
        else:
            btn[1][2].setEnabled(False)
    else:
        btn[0][1].setEnabled(False)
        btn[0][2].setEnabled(False)
        btn[1][0].setEnabled(False)
        btn[1][1].setEnabled(False)
        btn[1][2].setEnabled(False)

def cut(person):
    cuts=(4,11,23,40,60,77,89,96,100); result=[]
    for cut in cuts:
        result.append(round(person*cut*0.01))
    return result

'''창 클래스들'''
#진행 바(연속형)
class progbar():
    def __init__(self,title,txt,leng=200,time=5):
        pass


        prog=Progressbar(self.__top,mode='indeterminate',length=leng)

        prog.start(interval=time)
    def __del__(self):
        self.__top.destroy()


#과목 입력
class input_subject():
    def __init__(self):
        super().__init__()
        self.setupUi(self,SCALE)
        global current_num
        #초기화
        self.__inbox,self.__invar=[],[]




        #버튼 생성



        #메뉴 생성/배치
        menu_str=('과목명','시수','삭제')
        for k in range(3):
            pass
        #메뉴,버튼 그룹 배치


        #기존 값 불러오기
        if current_num:
            subject=list(current_num.keys())
            for k in range(len(current_num)):
                self.__add_subject(subject[k],current_num[subject[k]])
    def __add_subject(self,subject=None,num=None):
        n=len(self.__inbox)


        self.__inbox.append(
            (



            )
        )
        for a in range(len(self.__inbox)):
            if self.__inbox[a]:
                for b in range(3):
                    pass
    def __del_subject(self,n):
        for a in range(3):
            pass
        self.__inbox[n]=None
    def __set_subject(self):
        global current_num
        current_num={}
        try:
            for k in range(len(self.__inbox)):
                if self.__inbox[k]:
                    current_num[self.__invar[k][0].get()]=int(self.__invar[k][1].get())
        except ValueError:
            QMessageBox.critical(self,'ERROR','잘못된 값 입력')
        else:
            self.__top.destroy()
            update_btn()


#가채점 입력
class grade_ing():
    def __init__(self):
        super().__init__()
        self.setupUi(self,SCALE)
        self.__err1,self.__err2={},{}

        self.__select()

    def __select(self):
        global current_num
        def next():
            top.destroy(); self.__grading()
        try:
            self.__subject.set(list(current_num.keys())[0])
        except IndexError:
            QMessageBox.critical(self,'ERROR','과목 입력 안됨')
        else:
            pass











    def __grading(self):
        subject=self.__subject.get() #과목 설정
        def get_input():
            #입력값 불러오기, 오류 검사
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
                QMessageBox.critical(self,'ERROR','값 입력 오류')
                return None
            else:
                if len(ans)==len(cor):
                    ans,cor=tuple(ans),tuple(cor)
                    return (ans,cor)
                else:
                    QMessageBox.critical(self,'ERROR','개수 오류')
                    return None
        def priv():
            #이전 창으로 진행
            top.destroy()
            self.__select()
        def del_all():
            for k in range(2):
                for j in range(2):
                    for i in range(3):
                        inputs[k][j][i].set('')
        def next():
            #다음 창으로 진행
            x=get_input()
            if x:
                for k in range(len(x[0])):
                    if x[0][k]<=5 and x[0][k]!=x[1][k]:
                        self.__err1[k+1]=[x[0][k],x[1][k]]
                    elif x[0][k]==7:
                        self.__err2[k+1]=[]
                n,m=len(self.__err1),len(self.__err2)
                var=QMessageBox.question(
                    self,
                    '오답 확인',
                    '<오답 개수>\n선택형: %s\n서답형:%s\n채점 진행?' %(n,m)
                )
                if var:
                    if self.__err1:
                        top.destroy()
                        self.__err_sel()
                    elif self.__err2:
                        top.destroy()
                        self.__err_comp()
                    else:
                        var=QMessageBox.question(self,'채점 완료?','채점 완료?')
                        if var:
                            self.__result()
        #메인




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





    def __err_sel(self):
        def priv():
            top.destroy()
            self.__grading()
        def next():
            try:
                for k in range(len(score_in)):
                    self.__err1[num[k]]=tuple(self.__err1[num[k]]+[float(score_in[k].get())])
                if self.__err2:
                    top.destroy()
                    self.__err_comp()
                else:
                    var=QMessageBox.question(self,'채점 완료?','채점 완료?')
                    if var:
                        top.destroy()
                        self.__result()
            except ValueError:
                QMessageBox.critical(self,'Error','값 입력 오류')






        num=list(self.__err1.keys())
        score_in=[]
        for k in range(len(self.__err1)):
            pass


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
                    self.__err2[num[k]]=(float(score_in[k].get()),float(score_in2[k].get()))
                var=QMessageBox.question(self,'채점 완료?','채점 완료?')
                if var:
                    top.destroy()
                    self.__result()
            except ValueError:
                QMessageBox.critical(self,'Error','값 입력 오류')




        top_str=('번호','득점','배점')
        for k in range(3):
            pass
        num=list(self.__err2.keys())
        score_in,score_in2=[],[]
        for k in range(len(self.__err2)):
            pass





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



        score=100
        key_num=list(self.__err1.keys())
        for k in range(len(self.__err1)):
            score=score-self.__err1[key_num[k]][2]
        key_num=list(self.__err2.keys())
        for k in range(len(self.__err2)):
            score=score-self.__err2[key_num[k]][1]+self.__err2[key_num[k]][0]
        if self.__err2 or self.__err1:
            pass
        else:
            pass


#가채점결과
class grad_res():
    def __init__(self,subject=None):
        global current_num,current_wrong
        if current_wrong:
            if subject:
                if subject in current_num.keys():
                    self.__detail(subject)
                else:
                    QMessageBox.critical(self,'Error','없는 과목')
            else:
                self.__main()
        else:
            QMessageBox.critical(self,'ERROR','가채점 안됨')
    def __main(self):
        subjects=list(current_num.keys())
        score=get_score()
        def btn_make(subject,n):
            pass
        def del_res(mode=False):
            global current_wrong
            var=QMessageBox.question(self,'삭제?','복원 불가\n삭제?')
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



        top_str=('과목명','오답 수','점수','상세','삭제?')

        lab,chk=[],[]
        for k in range(5):
            pass
        for k in range(len(subjects)):
            tmp_btn=None

            lab.append([])
            if score[k]:
                pass



                if score[k][0]!=100:
                    btn_make(subjects[k],k+1)
            else:
                pass







    def __detail(self,subject):
        global current_wrong
        wrong=current_wrong[subject]


        if wrong[0]:
            pass
            top_sel=('번호','응답','정답','배점')
            err_num=list(wrong[0].keys())

            for k in range(4):
                pass
            for k in range(len(wrong[0])):
                pass
                for j in range(3):
                    pass

        if wrong[1]:
            pass
            top_sel=('번호','득점','배점')
            err_num=list(wrong[1].keys())

            for k in range(3):
                pass
            for k in range(len(wrong[1])):
                pass
                for j in range(2):
                    pass


#(예상)등급계산
class grade_calc():
    def __init__(self):
        super().__init__()
        self.setupUi(self,SCALE)
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
                QMessageBox.infomation(self,'결과','최고: %s\n최저: %s' %(max,min))
            except ValueError:
                QMessageBox.critical(self,'Error','잘못된 값 입력')
        def del_all():
            for k in range(len(current_num)):
                grade1[k].set('')
                grade2[k].set('')
        if len(current_num)==0:
            QMessageBox.critical(self,'Error','과목 입력 안됨')
        else:
            pass



            str_top=('과목명','시수','등급1','등급2')
            for a in range(4):
                pass
            nums=list(current_num.values())
            grade1,grade2=[],[]
            for k in range(len(current_num)):
                pass











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
            QMessageBox.critical(self,'Error','개수 오류')
            return None,None
#성적 입력
class exam_input():
    def __init__(self):
        super().__init__()
        self.setupUi(self,SCALE)
        global current_num,current_result
        def btn_make(n):
            pass
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
                        a=float(a)
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
                QMessageBox.critical(self,'Error','입력 값 오류')
            else:
                if var_b:
                    tmp=QMessageBox.question(self,'Info','빈 칸 존재\n성적입력?')
                if (not var_b) or tmp:
                    for k in range(length):
                        if res[k][0] and res[k][1] and res[k][2]:
                            current_result[subjects[k]]=res[k]
                    top.destroy()
                    exam_res()
        if current_num:
            pass



            subjects,nums=tuple(current_num.keys()),tuple(current_num.values())
            length=len(subjects)
            top_str=('과목명','시수','원점수','석차','인원수')
            btn,ent=[],[]

            for k in range(length):
                pass

                ent.append([])
                if subjects[k] in current_result.keys():
                    tmp=current_result[subjects[k]]
                else:
                    tmp=None
                for j in range(3):
                    pass
                    if tmp:
                        ent[k][j].set(tmp[j])

                btn_make(k)





        else:
            QMessageBox.critical(self,'Error','과목 입력 안됨')
#시혐 결과
class exam_res():
    def __init__(self):
        super().__init__()
        self.setupUi(self,SCALE)
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
            pass



            global current_num
            top_str=('과목','시수','점수','석차','등급','백분위')
            for k in range(6):
                pass
            subjects=tuple(current_num.keys())
            grades,var=[],True
            for k in range(len(current_num)):
                pass

                if subjects[k] in current_result.keys():
                    tmp=current_result[subjects[k]]
                    res=grade(tmp[1],tmp[2])




                    grades.append(res[0])
                else:
                    pass
                    var=False



        elif current_num:
            QMessageBox.critical(self,'Error','성적 입력 안됨')
        else:
            QMessageBox.critical(self,'Error','과목 입력 안됨')
#성적 추이
class change():
    def __init__(self):
        super().__init__()
        self.setupUi(self,SCALE)
        global current_result
        if current_result:
            pass


        elif current_num:
            QMessageBox.critical(self,'Error','성적 입력 안됨')
        else:
            QMessageBox.critical(self,'Error','과목 입력 안됨')
#등급인원계산
class cut_calc():
    def __init__(self):
        super().__init__()
        self.setupUi(self,SCALE)
        result=['','','','','','','','','']
        cuts=(4,11,23,40,60,77,89,96,100)
        def get():
            try:
                a=int(ent.get())
            except ValueError:
                QMessageBox.critical(self,'Error','인원수 오류')
            else:
                result=[]
                for k in cuts:
                    result.append(round(a*k/100))









        str_top=('등급','누적비율','누적인원수')
        for k in range(3):
            pass
        for k in range(9):
            pass


#도움말
class help(QWidget,):
    def __init__(self):
        super().__init__()
        self.setupUi(self,SCALE)


#라이선스
class license(QWidget,):
    def __init__(self):
        super().__init__()
        self.setupUi(self,SCALE)


#정보
class info(QWidget,):
    def __init__(self):
        super().__init__()
        self.setupUi(self,SCALE)


'''콜백 함수'''
#읽기
def load(name=None):
    global result_semester,result_exam
    if not name:
        name=askopen()
    if name:
        prog=progbar('Load','Loading...')
        try:
            with open(name,'r',encoding='utf-8') as file:
                result_semester,result_exam=json.load(file)
        except IOError:
            tmp=QMessageBox.question(self,'Error','읽기 에러',QMessageBox.Retry|QMessageBox.Cancel)
            if tmp:
                load(name)
        except json.JSONDecodeError:
            QMessageBox.critical(self,'Error','파일 형식 오류')
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
                QMessageBox.critical(self,'Error','파일 형식 오류')
        finally:
            del(prog)
    else:
        tmp=QMessageBox.question(self,'Error','파일 지정 오류',QMessageBox.Retry|QMessageBox.Cancel)
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
        if current_exam[2]=='3': #학기말
            result_semester[current_exam[:2]]=[current_num,current_result]
        else: #중간고사or기말고사
            result_semester[current_exam[:2]][0]=current_num
            result_exam[current_exam]=[current_wrong,current_result]
        try:
            with open(name,'w',encoding='utf-8') as file:
                json.dump((result_semester,result_exam),file,indent=4,ensure_ascii=False)
        except IOError:
            sel=QMessageBox.question(self,'Error','쓰기 에러',QMessageBox.Retry|QMessageBox.Cancel)
            if sel: 
               save(name)
        finally:
            del(prog)
            file_name=name
    else:
        tmp=QMessageBox.question(self,'Error','파일 지정 오류',QMessageBox.Retry|QMessageBox.Cancel)
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
    res=QMessageBox.question('저장','저장?',QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
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




#파일
menu_file.add_command(label='불러오기',command=load)
menu_file.add_command(label='저장',command=save)
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

option,exam=(('1학년','2학년','3학년'),('1학기','2학기'),('중간고사','기말고사','학기말')),[]
for a in range(3):
    pass
    exam[a].set(option[a][0])


    exam[a].trace('w',lambda *args: changeBtn.config(fg='red'))





'''메인 버튼'''
#버튼 생성
btn=[[],[]]



















update_btn()

#창 배치
win.config(menu=menu_bar)

win.mainloop()#메인루프