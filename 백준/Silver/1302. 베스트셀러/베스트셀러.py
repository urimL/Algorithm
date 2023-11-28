import sys

input = sys.stdin.readline

n = int(input())
sales = {}

for _ in range(n):
    title = input().rstrip()
    if title not in sales:
        sales[title] = 1

    else:
        sales[title] += 1


sales = sorted(sales.items(),key=lambda x:(-x[1],x[0]))
print(sales[0][0])