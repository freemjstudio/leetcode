#  [1,2,3] -> [1,4,9] 와 같이, 제곱수를 오름차순 정렬로 반환하는 함수를 작성

def solve(arr):
    N = len(arr)
    left, right = 0, N - 1
    result = []
    while left <= right:
        if abs(arr[left]) < abs(arr[right]):
            result.append(arr[left] ** 2)
            left += 1
        else:
            result.append(arr[right] ** 2)
            right -= 1

    return result

test_case = [1, -2, -3]
print(solve(test_case))