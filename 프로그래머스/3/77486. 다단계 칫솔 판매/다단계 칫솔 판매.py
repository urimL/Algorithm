from collections import deque

def solution(enroll, referral, seller, amount):
    answer = []
    graph = dict()
    result = dict()
    
    #[참여자 : 추천인]
    for i, j in zip(enroll, referral):
        graph[i] = j
        result[i] = 0
    
    def bfs(x,a):
        q = deque()
        q.append((x,a))
        
        while q:
            now, total = q.popleft()

            tmp = total//10
            if tmp < 1:
                return
            else:
                result[now] -= tmp
                if graph[now] == '-':
                    break
                result[graph[now]] += tmp
                q.append((graph[now],tmp))

    for i, j in zip(seller, amount):
        result[i] += j*100
        bfs(i,j*100)

    answer = list(result.values())
    return answer