def solution(id_list, report, k):
    answer = []
    dic = dict()
    mail = dict()
    
    for id in id_list:
        mail[id] = 0
    
    for r in report:
        x,y = r.split(" ")
        if y not in dic:
            tmp = set()
            tmp.add(x)
            dic[y] = tmp
            continue
        dic[y].add(x)
    
    for d in dic:
        if len(dic[d]) >= k:
            for i in dic[d]:
                mail[i] += 1

    answer = list(mail.values())
    return answer