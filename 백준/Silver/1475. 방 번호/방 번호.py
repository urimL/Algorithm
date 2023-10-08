n = input()
count = 0
num = [0]*11

for i in n:
    pos = int(i)

    if pos==9 or pos==6:
        if num[6] < num[9]:
            num[6]+=1
        else:
            num[9]+=1

    else:
        num[pos]+=1

print(max(num))
