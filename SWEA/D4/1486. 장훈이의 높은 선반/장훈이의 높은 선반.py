from itertools import combinations
tc = int(input())

for t in range(1,tc+1):
    n,b = map(int,input().split())
    total = b
    h = list(map(int,input().split()))

    for i in range(1,len(h)+1):
        comb = combinations(h,i)
        for i in comb:
            if 0<= sum(i)-b < total:
                total = sum(i)-b

    print("#",t," ",total,sep='')
        
