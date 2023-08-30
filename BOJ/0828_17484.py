# https://www.acmicpc.net/problem/17484

N, M = map(int, input().split())
array = []
for _ in range(N):
    data = list(map(int, input().split()))
    array.append(data)
for a in array:
    print(*a)