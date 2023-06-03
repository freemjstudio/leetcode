# https://www.acmicpc.net/problem/6593


while True:
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        break # 탈출
    for _ in range(L):