# 1. 일찍 끝나는 회의 순으로 정렬한 뒤
# 2. 일찍 시작하는 회의 순으로 정렬한다.
# 끝나는 번호를 증가시키면서 이어나감

from sys import stdin 
from collections import deque

N = int(stdin.readline())
possible = []
for _ in range(N):
    a,b = map(int,stdin.readline().split())
    possible.append([a,b])

possible = sorted(possible, key = lambda x: (x[1],x[0]))
count = end = 0
for s,e in possible:
    if s >= end :
        count += 1
        end = e
print(count)