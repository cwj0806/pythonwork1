class Student:
    def __init__(self,stnum, name):
        self.stno = stnum   # 학번
        self.name = name   # 이름

class Course:    # 수업 
    def __init__(self):
        self.stnolist = []   # 수강자들을 파이썬 리스트로 구현
        self.stnamelist = []

    def register(self, stno, name):        # 수강 신청
        self.stnolist.append(stno)
        self.stnamelist.append(name)
        
    def withdraw(self,stno,name):      # 수강 취소        
        self.stnolist.remove(stno)
        self.stnamelist.remove(name)
        
    def Printone(self,stno):   #입력받은 학번을 가진 학생 정보 출력
        print(stno, studic[stno])

    def Printall(self):  #지금까지 입력받은 학생들 학번 오름차순으로 출력
        self.i=len(self.stnolist)
        print(self.i)
        for self.i in range(0,self.i):
            print(self.stnolist[self.i], studic[self.stnolist[self.i]])

    
   
studic={}

C=Course()

while True:
    u=input().split()
    
    if u[0]=="N":
        S=Student(int(u[1]),u[2])
        C.register(S.stno, S.name)
        studic[S.stno]=S.name
        
    elif u[0]=="C":
        
        C.withdraw(int(u[1]), studic[u[1]])
        del studic[S.stno]
        
    elif u[0]=="R":        
        C.Printone(int(u[1]))
        
    elif u[0]=="P":
        C.stnolist.sort()
        C.Printall()
        
    elif u[0]=="Q":
        break
        
    
