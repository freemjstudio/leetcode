N = int(input())
data = list(map(int, input().split()))
answer = [0, 0]


answer.sort() # 오름차순
print(*answer)