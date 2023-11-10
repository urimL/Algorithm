import sys
input = sys.stdin.readline

s = input().rstrip()
word = []
for i in range(0,len(s)):
    word.append(s[i:])

for i in sorted(word):
    print(i)
