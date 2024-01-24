from collections import defaultdict

def solution(ticket):
    answer = []
    ticket.sort(reverse = True)
    d = defaultdict(list)
    
    for s,e in ticket:
        d[s].append(e)

    st = ['ICN']
    path = []
    
    while st:
        now = st[-1]
        
        if not d[now] or len(d[now]) == 0:
            path.append(st.pop())
        else:
            st.append(d[now].pop())
    return path[::-1]