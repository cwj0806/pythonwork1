
while True :
    user=input("문장을 입력하세요 : ")
    a=user.split(".")
    b=a[0].split(" ")
    if len(b)==3 :
        if "합니다" in b :
            c=b[1].replace("이라고","")
            print("이름 : %s" %c)
        else :
            c=b[2].replace("입니다","")
            print("이름 : %s" %c)
    else :
        c=b[1].replace("입니다","")
        print("이름 : %s" %c)
    print("")                   
