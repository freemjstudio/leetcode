def solution(number, k):
    answer = ''
    arr = [int(i) for i in number]
    stack = []

    for i in range(len(arr)):
        if not stack:
            stack.append(arr[i])
            continue

            # pop 연산
        if k > 0:
            while stack and stack[-1] < arr[i] and k > 0:
                stack.pop()  # stack[-1] 제거
                k -= 1
        stack.append(arr[i])

    # 예외처리 999 같은 경우
    if k > 0:
        for s in stack[:k + 1]:
            answer += str(s)
    else:
        for s in stack:
            answer += str(s)

    return answer