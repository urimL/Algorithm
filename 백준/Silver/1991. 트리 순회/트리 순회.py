# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
input = sys.stdin.readline

n = int(input())
tree = {}

def preorder(now):
    if now=='.':
        return
    print(now,end='')
    preorder(tree[now][0])
    preorder(tree[now][1])

def inorder(now):
    if now=='.':
        return
    inorder(tree[now][0])
    print(now, end='')
    inorder(tree[now][1])

def postorder(now):
    if now=='.':
        return
    postorder(tree[now][0])
    postorder(tree[now][1])
    print(now, end='')

for i in range(n):
    root,left,right = input().split()
    tree[root] = [left,right]


preorder('A')
print()
inorder('A')
print()
postorder('A')