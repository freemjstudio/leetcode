# https://www.acmicpc.net/problem/6593

while True:
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        break # 탈출
    flag = False
    answer = 0 # 최소 시간
    for _ in range(L):

    if flag:
        print(f"Escaped in {answer} minute(s).")
    else:
        print("Trapped!")

