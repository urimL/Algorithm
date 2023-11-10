import sys
input = sys.stdin.readline

for i in range(int(input())):
    answer,pos = 0,0
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()

    for i in a:
        while True:
            if pos==m or i<=b[pos]:
                answer+=pos
                break
            else:
                pos+=1

                

    print(answer)
                
            
