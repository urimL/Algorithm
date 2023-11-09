tc = int(input())
word = []

for t in range(1,tc+1):
    s = input()
    if s not in word:   
        word.append(s)
            

word.sort(key=lambda x:(len(x),x))


for i in word:
    print(i)
