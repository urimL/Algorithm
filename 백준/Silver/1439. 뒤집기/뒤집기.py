s = input()
i, cnt_0,cnt_1 = 0,0,0
n = i+1

while n<len(s): 
    if s[i]==s[n]:
        n+=1
    else:
        if s[i]=='0':
            cnt_0+=1
        else:
            cnt_1+=1
        i=n
        n+=1

if s[-1]=='0':
    cnt_0+=1
else:
    cnt_1+=1


print(min(cnt_0,cnt_1))
