# https://www.acmicpc.net/problem/2304
N = int(input()) # 기둥 개수
answer = 0

stack = []
bars = []
for _ in range(N):
    L, H = map(int, input().split())
    bars.append([L, H])

bars.sort() # [[2, 4], [4, 6], [5, 3], [8, 10], [11, 4], [13, 6], [15, 8]]
for l, h in bars:
    # 자기 자신 height 보다 높은거 나오면 stack 에 넣고 낮은거 나오면 pop 하는 방식으로 구하기

    print(l, h)
print(answer)
