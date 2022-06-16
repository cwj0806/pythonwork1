import random

def lotto_generator():
    L=[]
    while len(L)<=5:
        n=random.randrange(1,46)
        if n not in L:
            L.append(n)
           
            
    return L        
        
a=int(input("원하는 숫자를 선택하세요. (1~100) "))
for i in range(a):
    selectednum=lotto_generator()
    print(i+1,"회:",selectednum,sep="")

print("이번주의 로또 번호입니다.",end=" ")
for i in selectednum:
    print(i,end=" ")
print("")    
print("이 번호가 맞으면 교수님과 50:50")
