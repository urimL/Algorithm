s=input()
result = [0 for i in range(26)]

for i in s:
    result[ord(i)-97]+=1

for i in result:
    print(i,end=' ')
    

