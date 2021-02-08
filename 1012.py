
from collections import deque
from sys import stdin
# 테스트 케이스의 개수 T
T = int(input())
# 이동 방향 
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(n,m,x,y,visit):
    queue = deque()
    queue.append((x,y))
    while queue:
        qx, qy = queue.popleft()
        for i in range(4):
            nx = qx +dx[i]
            ny = qy +dy[i]
            if 0<= nx and nx < m and 0<=ny and ny<n and graph[ny][nx] == 1 :
                if visit[ny][nx] == 0 : 
                    visit[ny][nx] = 1
                    queue.append((nx,ny))

for _ in range(T):
    count = 0
    # 가로길이 M(1 ≤ M ≤ 50) && 세로길이 N(1 ≤ N ≤ 50) 
    # 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)
    M,N,K = map(int,stdin.readline().split())
    # 그래프 = 배추밭 
    graph = [[0]*M for _ in range(N)]
    # 배추가 심어진 위치:
    target = deque()
    for _ in range(K):
        # 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)
        X,Y= map(int,stdin.readline().split())
        graph[Y][X] = 1
        target.append((X,Y))
    # 방문한 곳 
    visit = [[0]*M for _ in range(N)]
    while target:
        sx,sy = target.popleft()
        if visit[sy][sx] == 0: 
            bfs(N,M,sx,sy,visit)
            count += 1
    print (count)
