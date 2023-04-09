def solution(progresses, speeds):
    answer = []
    stack = []
    N = len(progresses)
    for i in range(N):
        progress = 100 - progresses[i]
        if progress % speeds[i] != 0:
            day = progress // speeds[i] + 1
        else:
            day = progress // speeds[i]

        if len(stack) == 0:
            stack.append(day)
        else:
            count = 1
            if stack[-1] > day:
                while stack:
                    if stack[-1] > day:
                        stack.pop()
                        count += 1
                    else:
                        break
                answer.append(count)
            else:
                stack.append(day)
    if stack:
        answer.append(1)

    return answer