#python algorithm
#주소 출력
class tools:  #사용자가 입력할 명령어들
    def __init__(self): 
        self.n=-1  #현재 주소의 위치
        
    def go(self,e): #현재 주소의 위치에 따른 주소 삽입
        if self.n==-1:
            addrList.append(e)        
            print(addrList[-1])
        else:
            del addrList[(self.n)+1:]
            addrList.append(e)        
            print(addrList[-1])
            n=-1
            

    def forward(self):
        if self.n==-1:
            return False
        else:
            self.n +=1
            print(addrList[self.n])
            return addrList[self.n]
                        

    def backward(self):
        if self.n==-len(addrList):
            return False
        else:
            self.n -=1
            print(addrList[self.n])
            return addrList[self.n]

    def history(self):
        k=-1
        for i in hisaddrList:
            print(hisaddrList[k])
            k-=1
        return

    def quit(self):
        return True

toolsList=['go','forward','backward','history','quit'] #사용자 입력 도구 구분
addrList=["www.hufs.ac.kr"]
hisaddrList=["www.hufs.ac.kr"] #history 함수를 위함

addr=tools()



v=0


while True:  #사용자가 quit을 입력할 때 까지 반복
    a=input()
    temp=a.split()
    if v==0:
        print(hisaddrList[0])
        v+=1
    if temp[0]=='go':
        addr.go(temp[1])
        if temp[1] in hisaddrList:
            hisaddrList.remove(temp[1])
            hisaddrList.append(temp[1])
        else:
            hisaddrList.append(temp[1])
    elif temp[0]=='forward':
        
        t=addr.forward()
        if t!=0:
            hisaddrList.remove(t)
            hisaddrList.append(t)           
        
    elif temp[0]=='backward':
        
        t=addr.backward()
        if t!=0:
            hisaddrList.remove(t)
            hisaddrList.append(t)
            
    elif temp[0]=='history':
       
        addr.history()
    elif temp[0]=='quit':
        break
        
        
    







