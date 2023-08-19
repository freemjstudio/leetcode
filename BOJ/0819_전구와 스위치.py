import sys
sys.setrecursionlimit(10**7)
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
def check(arr1, arr2):
    if arr1 == arr2:
        return True
    return False

# 이미 a == b 인 경우
if check(a, b):
    print(0)
    exit(0)

def dfs(switch, arr, cnt):
    if cnt == 10000:
        return -1
    # switch 넣었을 때 검토
    if switch == 0:
        arr[0] = (not arr[1])
        arr[1] = (not arr[0])
    elif switch == N-1:
        arr[N-1] = (not arr[N-1])
        arr[N-2] = (not arr[N-2])
    else:
        arr[switch-1] = (not arr[switch-1])
        arr[switch] = (not arr[switch])
        arr[switch+1] = (not arr[switch+1])

    if check(arr, b):
        return cnt

    for next in range(N):
        if next == switch:
            continue
        dfs(next, arr, cnt+1)

for i in range(N):
    result = dfs(i, a, 1)
    if result != -1:
        flag = True
        answer = min(answer, result)

if flag:
    print(answer)
else:
    print(-1)