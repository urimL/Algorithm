import operator

def solution(N, stages):
    answer = []
    dic_Stage = {}
    
    for i in range(1,N+1):
        cnt=0
        stage_num=stages.count(i)
        
        if stage_num != 0:
            for j in stages:
                if i<=j:
                    cnt+=1
            dic_Stage[i]=stage_num/cnt
        else:
            dic_Stage[i]=0
        
        print(dic_Stage[i])
        
    
    answer = sorted(dic_Stage,key=lambda x:dic_Stage[x],reverse=True)
    
    
    return answer