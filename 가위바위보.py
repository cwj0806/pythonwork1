game=("가위","바위","보")
from random import choice
print("가위바위보 게임")
a=0
b=0
r=1

while a<3 and b<3 :
    print("(라운드 %d)"%r)
    com=choice(game)
    print("컴퓨터가 결정했습니다.")
    user=input("무엇을 내시겠습니까? ")
    if user==game[0] :
        if com==game[0] :
            continue
        elif com==game[1] :
            print("컴퓨터는 %s, 당신은 %s, 컴퓨터가 이겼습니다" %(com,user))
            b=b+1
            print("컴퓨터 : %d승 %d패, 당신 : %d승 %d패" %(b,a,a,b))
            r=r+1
        else :
            print("컴퓨터는 %s, 당신은 %s, 당신이 이겼습니다" %(com,user))
            a=a+1
            print("컴퓨터 : %d승 %d패, 당신 : %d승 %d패" %(b,a,a,b))
            r=r+1
    elif user==game[1] :
        if com==game[0] :
            print("컴퓨터는 %s, 당신은 %s, 당신이 이겼습니다" %(com,user)) 
            a=a+1
            print("컴퓨터 : %d승 %d패, 당신 : %d승 %d패" %(b,a,a,b))
            r=r+1
        elif com==game[1] :
            continue
        else :
            print("컴퓨터는 %s, 당신은 %s, 컴퓨터가 이겼습니다" %(com,user))
            b=b+1
            print("컴퓨터 : %d승 %d패, 당신 : %d승 %d패" %(b,a,a,b))
            r=r+1
    else :
        if com==game[0] :
            print("컴퓨터는 %s, 당신은 %s, 컴퓨터가 이겼습니다" %(com,user))
            b=b+1
            print("컴퓨터 : %d승 %d패, 당신 : %d승 %d패" %(b,a,a,b))
            r=r+1
        elif com==game[1] :
            print("컴퓨터는 %s, 당신은 %s, 당신이 이겼습니다" %(com,user)) 
            a=a+1
            print("컴퓨터 : %d승 %d패, 당신 : %d승 %d패" %(b,a,a,b))
            r=r+1
        else :
            continue
if a==3 :
 print("당신의 승리!!")
else :
 print("컴퓨터의 승리!!")
            
        
    
