import sys

input = sys.stdin.readline

n, m = map(int, input().split())
books = list(map(int, input().split()))
answer, checkpoint = 0, 0
minus,plus = [],[]

books.sort()

if abs(books[0]) > abs(books[-1]):
    books.sort(reverse=True)

for i in range(n-1):
    if books[i]*books[i+1] < 0:
        checkpoint = i+1

for i in range(0,checkpoint,m):
    answer+=abs(books[i])*2

for i in range(n-1,checkpoint-1,-m):
    if i==n-1:
        answer+=abs(books[-1])
    else:
        answer+=abs(books[i])*2

print(answer)
