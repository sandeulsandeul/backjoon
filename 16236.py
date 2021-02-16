{\rtf1\ansi\ansicpg949\cocoartf2578
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red255\green255\blue254;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\cssrgb\c100000\c100000\c99608;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl420\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 from collections import deque\cb1 \
\cb3 from sys import stdin \cb1 \
\cb3 INF = 1e9\cb1 \
\cb3 N = int(stdin.readline())\cb1 \
\cb3 graph = []\cb1 \
\cb3 count = 0\cb1 \
\cb3 size = 2\cb1 \
\cb3 loc_x,loc_y = 0 ,0 \cb1 \
\cb3 dx = [1,0,-1,0]\cb1 \
\cb3 dy = [0,1,0,-1]\cb1 \
\
\cb3 for i in range(N):\cb1 \
\cb3     fish = list(map(int,stdin.readline().split()))\cb1 \
\cb3     for j in range(len(fish)) :\cb1 \
\cb3         if fish[j] == 9 :\cb1 \
\cb3             loc_y = i\cb1 \
\cb3             loc_x = j\cb1 \
\cb3     graph.append(fish)\cb1 \
\cb3 graph[loc_y][loc_x] = 0 \cb1 \
\
\cb3 def bfs():\cb1 \
\cb3     dist = [[-1] * N for _ in range(N)]\cb1 \
\cb3     q = deque([(loc_x,loc_y)])\cb1 \
\cb3     dist[loc_y][loc_x] = 0\cb1 \
\cb3     while q :\cb1 \
\cb3         x, y = q.popleft()\cb1 \
\cb3         for i in range(4):\cb1 \
\cb3             nx = x + dx[i] \cb1 \
\cb3             ny = y + dy[i]\cb1 \
\cb3             if 0 <= nx and nx < N and 0 <= ny and ny < N :\cb1 \
\cb3                 if dist[ny][nx] == -1 and graph[ny][nx] <= size :\cb1 \
\cb3                     dist[ny][nx] = dist[y][x] + 1 \cb1 \
\cb3                     q.append((nx,ny))\cb1 \
\
\cb3     return dist \cb1 \
\
\cb3 def find(dist):\cb1 \
\cb3     x,y = 0,0 \cb1 \
\cb3     min_dist = INF\cb1 \
\cb3     for i in range(N):\cb1 \
\cb3         for j in range(N):\cb1 \
\cb3             if dist[i][j] != -1 and 1<= graph[i][j] and graph[i][j] < size :\cb1 \
\cb3                 if dist[i][j] < min_dist :\cb1 \
\cb3                     min_dist = dist[i][j] \cb1 \
\cb3                     y = i\cb1 \
\cb3                     x = j\cb1 \
\cb3     if min_dist == INF:\cb1 \
\cb3         return None\cb1 \
\cb3     else :\cb1 \
\cb3         return x,y,min_dist\cb1 \
\cb3     \cb1 \
\cb3 result = 0\cb1 \
\cb3 ate = 0\cb1 \
\
\cb3 while True :\cb1 \
\cb3     value = find(bfs())\cb1 \
\cb3     if value == None:\cb1 \
\cb3         print (result)\cb1 \
\cb3         break\cb1 \
\cb3     else:\cb1 \
\cb3         loc_x , loc_y = value[0], value[1]\cb1 \
\cb3         result += value[2]\cb1 \
\cb3         graph[loc_y][loc_x] = 0\cb1 \
\cb3         ate += 1\cb1 \
\cb3         if ate >= size :\cb1 \
\cb3             size += 1 \cb1 \
\cb3             ate = 0\cb1 \
\cb3     \cb1 \
\
\
\
}