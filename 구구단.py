import time,random
scoreboard=[]
while True :
    r=1
    score=0
    while r<=10 :
        a=random.randrange(1,10)
        b=random.randrange(1,10)
        print("%d) %d * %d = " %(r,a,b), end="")
        start=time.time()    
        user=int(input())
        t=time.time()-start
    
        if t>=3 :
            print("(제한시간이 지났습니다.) %1f초 소요:Score=%d" %(round(t*1000)/1000,score))
        elif user!=a*b:
            print("(틀렸습니다.) %f초 소요:Score=%d" %(round(t*1000)/1000,score))
        else:
            score=score+int(3000-round(1000*t))
            print("(맞았습니다.) %1f초 소요:Score=%d" %(round(t*1000)/1000,score))
        r=r+1        
    scoreboard.append(score)
    scoreboard.sort()
    if score==scoreboard[-1]:
        print("최고 기록 갱신")
