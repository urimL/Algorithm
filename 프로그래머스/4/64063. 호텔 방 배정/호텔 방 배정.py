import sys
from collections import defaultdict
sys.setrecursionlimit(10**4)

def find(room, r):
    if room[r] == 0:
        room[r] = r+1
        return r
    else:
        room[r] = find(room,room[r])
        return room[r]

def solution(k, room_number):
    room = defaultdict(lambda: 0)
    answer = []
    for r in room_number:
        answer.append(find(room,r))
    return answer