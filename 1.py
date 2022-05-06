#python algorithm
#doubly linked list
class tools:
    def __init__(self):
        self.n=-1
        
    def go(self,e):
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

toolsList=['go','forward','backward','history','quit']
addrList=["www.hufs.ac.kr"]
hisaddrList=["www.hufs.ac.kr"]

addr=tools()

t=0

v=0


while True:
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
        
        
    







