from sys import stdin
#첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 
N = int(stdin.readline())
#둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100) 
A = list(map(int,stdin.readline().split()))
# 셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 
# 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다. 
add,sub,mul,div = map(int,stdin.readline().split())

maxValue = -1e9
minValue = 1e9

def dfs(i,now):
  global add,sub,mul,div,maxValue,minValue

  if i == N :
    minValue = min(minValue,now)
    maxValue = max(maxValue,now)

  else:
    if add > 0 :
      add -= 1
      dfs(i+1, now+ A[i])
      add += 1
    if sub > 0 :
      sub -= 1
      dfs(i+1, now - A[i])
      sub += 1
    if mul > 0 :
      mul -= 1
      dfs(i+1, now * A[i])
      mul += 1
    if div > 0 : 
      div -= 1
      dfs(i+1, int(now / A[i]))
      div += 1

dfs (1,A[0])

print(maxValue)

print(minValue)


