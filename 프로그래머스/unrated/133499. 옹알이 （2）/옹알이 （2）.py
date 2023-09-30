def solution(babbling):
    answer = 0
    ch = True
    can = ["aya", "ye", "woo", "ma"]
    tmp = []
    
    for i in babbling:
        i=i.replace("aya","1")
        i=i.replace("ye","2")
        i=i.replace("woo","3")
        i=i.replace("ma","4")
        
        for j in range(len(i)-1):
            if i[j]==i[j+1] or (i[j]<"1" or i[j]>"4"):
                ch = False
                print("E")
                
        if i[-1]<"1" or i[-1]>"4":
            ch=False
            print("Y")

        print(i)
        print(ch)
        if ch:
            answer+=1
        
        ch=True


    return answer