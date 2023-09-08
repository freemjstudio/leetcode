# https://www.acmicpc.net/problem/19238

n, m, fuel = map(int, input().split())
flag = False # -1
answer = int(1e9)

array = []

for i in range(n): # n*n 배열
    data = list(map(int, input().split()))
    array.append(data)

if flag:
    print(answer)
else:
    print(-1)