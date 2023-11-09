tc = int(input())
card = {}

for i in range(tc):
    n = int(input())
    if n not in card.keys():
        card[n]=1
    else:
        card[n]+=1

result = sorted(card.items(),key=lambda x:(-x[1],x[0]))
print(result[0][0])

