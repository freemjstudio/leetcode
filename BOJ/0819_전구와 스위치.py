import sys
sys.setrecursionlimit(10**7)
flag = False
answer = 0

N = int(input())
a = list(map(int, list(input())))
b = list(map(int, list(input())))

temp1 = a[:]
temp2 = a[:] # deep copy

def check(arr1, arr2):
    if arr1 == arr2:
        return True
    return False

# from index 0
def from_zero(arr):
    count = 1
    arr[0] = (not arr[0])
    arr[1] = (not arr[1])

    for i in range(1, N):
        if arr[i-1] != b[i-1]: # i-1, i, i+1 모두 동일해야 하므로 i-1 부터 체크
            count += 1
            arr[i-1] = (not arr[i-1])
            arr[i] = (not arr[i])
            if i != N-1:
                arr[i+1] = (not arr[i+1])

    if check(arr, b):
        return count
    return -1
# from index 1
def from_one(arr):
    count = 0
    for i in range(1, N):
        if arr[i-1] != b[i-1]:
            count += 1
            arr[i - 1] = (not arr[i - 1])
            arr[i] = (not arr[i])
            if i != N-1:
                arr[i+1] = (not arr[i+1])
    if check(arr, b):
        return count
    return -1

result1 = from_zero(temp1)
result2 = from_one(temp2)

if result1 != -1 and result2 == -1:
    print(result1)
elif result1 == -1 and result2 != -1:
    print(result2)
elif result1 == -1 and result2 == -1:
    print(-1)
else:
    print(min(result1, result2))
