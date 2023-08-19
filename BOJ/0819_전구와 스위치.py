flag = False
answer = 0

N = int(input())
a = list(map(int, list(input())))
b = list(map(int, list(input())))
'''
0 : ON 
1 : OFF
직전에 누른 스위치는 누르지 않는다 ! 
'''
def check():
    if a == b:
        return True
    return False

# 이미 a == b 인 경우
if check():
    print(0)
    exit(0)

def dfs(switch, arr, cnt):
    if cnt == 100000:
        return -1
    # switch 넣었을 때 검토
    for next in range(N):
        if next



for i in range(N):
    result = dfs(i, a, 1)
    if result != -1:
        answer = min(answer, result)

if flag:
    print(answer)
else:
    print(-1)