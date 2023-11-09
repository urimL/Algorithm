t = int(input())

for i in range(1,t+1):
    s = input()

    if len(s)%2==0:
        mid = len(s)//2
        answer = int("".join(s[0:mid]))+int("".join(s[mid:]))
        print('#',i,' ',answer,sep='')

    else:
        mid = len(s)//2
        a = int("".join(s[0:mid]))+int("".join(s[mid:]))
        b = int("".join(s[0:mid+1]))+int("".join(s[mid+1:]))

        if a<=b:
            answer = a
        else:
            answer = b

        print('#',i,' ',answer,sep='')
