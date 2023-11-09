tc = int(input())
people = []

for t in range(1,tc+1):
    age,name = map(str,input().split())
    people.append([int(age),name,t])
            

people.sort(key=lambda x:(x[0],x[2]))

for i in people:
    print(i[0],i[1])
