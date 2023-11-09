t = int(input())

for T in range(1,t+1):
    answer=0
    n=int(input())
    for i in range(-n,n+1):
        for j in range(-n,n+1):
            if i**2+j**2<=n**2:
                answer+=1

    print("#",T," ",answer,sep='')

    
    
        
